"""
career_controller_fixed.py - Fixed version of career_controller.py
"""

from PyQt6.QtCore import QObject, pyqtSignal
from src.controllers.dice_controller import DiceController
from src.data.careers import get_career, check_career_requirements, get_starting_gear


class CareerController(QObject):
    """Controller for career progression and selection"""

    # Signals
    careersUpdated = pyqtSignal(list)  # List of available careers
    careerSelected = pyqtSignal(str, str)  # Category, career name
    promotionResult = pyqtSignal(bool)  # True if promoted
    warBrokenOut = pyqtSignal()  # Emitted when war breaks out
    careerCompleted = pyqtSignal(dict)  # Emitted when a career is completed, passes career data

    def __init__(self, character=None):
        """Initialize the career controller

        Args:
            character: Optional character object to use
        """
        super().__init__()
        self.character = character
        self.dice_controller = DiceController()
        self.war_broken_out = False
        self.current_career = None  # Track the current career

    def set_character(self, character):
        """Set the character to use

        Args:
            character: Character object
        """
        self.character = character

    def get_available_careers(self, is_first_career=False):
        """Get list of careers available to the character

        Args:
            is_first_career: Whether this is the character's first career

        Returns:
            List of dictionaries with career info (category, name, meets_requirements)
        """
        from src.data.careers import get_career_categories, get_careers_in_category

        available_careers = []

        for category in get_career_categories():
            careers = get_careers_in_category(category)

            for career_name, career_data in careers.items():
                # Check if character meets requirements
                meets_requirements = check_career_requirements(self.character, category, career_name)

                # Add career to list
                available_careers.append({
                    "category": category,
                    "name": career_name,
                    "data": career_data,
                    "meets_requirements": meets_requirements
                })

        # Sort by whether character meets requirements (True first)
        available_careers.sort(key=lambda c: not c["meets_requirements"])

        self.careersUpdated.emit(available_careers)
        return available_careers

    def select_career(self, category, career_name):
        """Select a career for the character

        Args:
            category: Career category
            career_name: Career name

        Returns:
            Dictionary with career data or None if not found
        """
        career = get_career(category, career_name)
        if not career:
            return None

        # Check if character meets requirements
        if not check_career_requirements(self.character, category, career_name):
            return None

        # Save the current career
        self.current_career = {
            "category": category,
            "name": career_name,
            "data": career
        }

        # Signal career selection
        self.careerSelected.emit(category, career_name)

        return career

    def roll_random_career(self, eligible_only=True):
        """Roll for a random career

        Args:
            eligible_only: Whether to only consider careers the character is eligible for

        Returns:
            Dictionary with career data or None if no eligible careers
        """
        import random

        # Get available careers
        available_careers = self.get_available_careers()

        if eligible_only:
            # Filter to only eligible careers
            eligible_careers = [c for c in available_careers if c["meets_requirements"]]

            if not eligible_careers:
                return None

            # Select random eligible career
            career = random.choice(eligible_careers)
        else:
            # Select random career from all available
            career = random.choice(available_careers)

        # Save the current career
        self.current_career = career

        # Signal career selection
        self.careerSelected.emit(career["category"], career["name"])

        return career

    def complete_career(self):
        """Complete the current career and add it to the character

        Returns:
            Career data dictionary or None if no current career
        """
        if not self.current_career or not self.character:
            return None

        category = self.current_career["category"]
        career_name = self.current_career["name"]

        # Get career data
        career_data = self.current_career["data"]

        # Add career to character
        self.character.add_career(
            career_type=category,
            branch=career_name,
            rank=career_data.get("starting_rank", None),
            promotion=False  # Default to no promotion
        )

        # Emit signal with career data
        self.careerCompleted.emit(self.current_career)

        # Clear current career
        current_career = self.current_career
        self.current_career = None

        return current_career

    def get_career_specialties(self, category, career_name):
        """Get specialties for a career

        Args:
            category: Career category
            career_name: Career name

        Returns:
            List of specialties for the career
        """
        career = get_career(category, career_name)
        if not career:
            return []

        return career.get("specialties", [])

    def select_specialty(self, specialty):
        """Select a specialty for the current career

        Args:
            specialty: Specialty name

        Returns:
            True if successful, False otherwise
        """
        if not self.character:
            return False

        self.character.add_specialty(specialty)
        return True

    def roll_for_promotion(self):
        """Roll for promotion

        Returns:
            True if promoted, False otherwise
        """
        # Roll D6, promotion on 6
        roll = self.dice_controller.roll_d6()
        promoted = roll >= 6

        # Signal promotion result
        self.promotionResult.emit(promoted)

        return promoted

    def check_war_breakout(self):
        """Check if war breaks out

        Returns:
            True if war breaks out, False otherwise
        """
        if self.war_broken_out:
            return True

        # War breaks out on 7 or less on 2D6
        roll = self.dice_controller.roll_2d6()
        war_breaks_out = roll <= 7

        if war_breaks_out:
            self.war_broken_out = True
            self.warBrokenOut.emit()

        return war_breaks_out

    def add_career_to_character(self, category, career_name, specialty, promotion=False):
        """Add a career to the character

        Args:
            category: Career category
            career_name: Career name
            specialty: Selected specialty
            promotion: Whether character was promoted

        Returns:
            Dictionary with career data
        """
        if not self.character:
            return None

        # Get career data
        career = get_career(category, career_name)
        if not career:
            return None

        # Add career to character
        self.character.add_career(
            career_type=category,
            branch=career_name,
            rank=career.get("starting_rank", None),
            promotion=promotion
        )

        # Add specialty
        self.character.add_specialty(specialty)

        # Add skills from career
        for skill in career.get("skills", []):
            if skill != "Varies by job":
                self.character.add_skill(skill, 'D')  # D is the default starting level for skills

        # If promoted, improve Coolness Under Fire
        if promotion:
            # CUF improves by one letter (e.g., D -> C)
            current_cuf = self.character.cuf
            if current_cuf == "D":
                self.character.cuf = "C"
            elif current_cuf == "C":
                self.character.cuf = "B"
            elif current_cuf == "B":
                self.character.cuf = "A"

        # Prepare career data to return
        career_data = {
            "category": category,
            "name": career_name,
            "specialty": specialty,
            "promotion": promotion,
            "data": career
        }

        # Emit signal that career is completed
        self.careerCompleted.emit(career_data)

        return career_data

    def get_career_starting_gear(self, category, career_name):
        """Get starting gear for a career

        Args:
            category: Career category
            career_name: Career name

        Returns:
            List of starting gear items
        """
        return get_starting_gear(category, career_name)

    def set_war_career(self, at_war_career):
        """Set the character's role during the war

        Args:
            at_war_career: Career during the war

        Returns:
            True if successful, False otherwise
        """
        if not self.character:
            return False

        self.character.set_war_experience(at_war_career)
        self.war_broken_out = True

        return True

    def add_war_skills(self, skills):
        """Add skills gained during the war

        Args:
            skills: Dictionary mapping skill names to levels

        Returns:
            True if successful, False otherwise
        """
        if not self.character:
            return False

        for skill, level in skills.items():
            self.character.add_skill(skill, level)

        return True

    def roll_random_specialty(self):
        """Roll for a random specialty for the current career

        Returns:
            Specialty name or None if no current career
        """
        if not self.current_career:
            return None

        category = self.current_career["category"]
        career_name = self.current_career["name"]

        # Get specialties
        specialties = self.get_career_specialties(category, career_name)

        if not specialties:
            return None

        # Roll random specialty
        import random
        return random.choice(list(specialties))