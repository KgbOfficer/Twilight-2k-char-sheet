"""
game_controller.py - Game state controller for Twilight 2000 character creator
"""

from PyQt6.QtCore import QObject, pyqtSignal
import json
import os

from src.models.character import Character
from src.controllers.dice_controller import DiceController
from src.controllers.career_controller import CareerController


class GameController(QObject):
    """Controller for managing game state and character creation"""

    # Signals
    characterChanged = pyqtSignal(object)  # Character object
    warBrokenOut = pyqtSignal()
    characterCompleted = pyqtSignal()

    def __init__(self):
        """Initialize the game controller"""
        super().__init__()
        self.character = Character()
        self.dice_controller = DiceController()
        self.career_controller = CareerController(self.character)
        self.war_broken_out = False
        self.character_completed = False

        # Connect to career controller signals
        self.career_controller.warBrokenOut.connect(self._on_war_broken_out)
        self.career_controller.careerCompleted.connect(self._on_career_completed)

    def reset(self):
        """Reset the game state"""
        self.character = Character()
        self.career_controller.set_character(self.character)
        self.war_broken_out = False
        self.character_completed = False
        self.characterChanged.emit(self.character)

    def set_basic_info(self, name, nationality):
        """Set character's basic information

        Args:
            name: Character name
            nationality: Character nationality
        """
        self.character.name = name
        self.character.nationality = nationality
        self.characterChanged.emit(self.character)

    def set_attributes(self, attributes):
        """Set character's attributes

        Args:
            attributes: Dictionary of attribute letters
        """
        for attr, letter in attributes.items():
            self.character.set_attribute_letter(attr, letter)

        # Calculate derived attributes
        self.character.calculate_derived_attributes()
        self.characterChanged.emit(self.character)

    def set_childhood(self, childhood, specialty):
        """Set character's childhood background

        Args:
            childhood: Childhood background
            specialty: Childhood specialty
        """
        self.character.childhood = childhood
        self.character.childhood_specialty = specialty
        self.characterChanged.emit(self.character)

    def add_career(self, career_type, branch, rank=None, promotion=False):
        """Add a career to the character's history

        Args:
            career_type: Type of career
            branch: Branch or specific career
            rank: Military rank or position
            promotion: Whether character was promoted
        """
        self.character.add_career(
            career_type=career_type,
            branch=branch,
            rank=rank,
            promotion=promotion
        )
        self.characterChanged.emit(self.character)

    def add_skills(self, skills):
        """Add skills to the character

        Args:
            skills: Dictionary mapping skill names to levels
        """
        for skill, level in skills.items():
            self.character.add_skill(skill, level)
        self.characterChanged.emit(self.character)

    def add_specialty(self, specialty):
        """Add a specialty to the character

        Args:
            specialty: Specialty name
        """
        self.character.add_specialty(specialty)
        self.characterChanged.emit(self.character)

    def set_war_experience(self, at_war_career):
        """Set character's war experience

        Args:
            at_war_career: Career during the war
        """
        self.character.set_war_experience(at_war_career)
        self.war_broken_out = True
        self.warBrokenOut.emit()
        self.characterChanged.emit(self.character)

    def set_radiation(self, radiation_points):
        """Set character's radiation exposure

        Args:
            radiation_points: Number of radiation points
        """
        self.character.radiation = radiation_points
        self.characterChanged.emit(self.character)

    def set_character_details(self, moral_code, big_dream, buddy, how_you_met, appearance):
        """Set character's additional details

        Args:
            moral_code: Character's moral code
            big_dream: Character's big dream
            buddy: Character's buddy
            how_you_met: How character met other PCs
            appearance: Character's appearance
        """
        self.character.moral_code = moral_code
        self.character.big_dream = big_dream
        self.character.buddy = buddy
        self.character.how_you_met = how_you_met
        self.character.appearance = appearance
        self.characterChanged.emit(self.character)

    def add_gear(self, gear):
        """Add gear to the character's inventory

        Args:
            gear: Gear item or list of gear items
        """
        if isinstance(gear, list):
            for item in gear:
                self.character.add_gear(item)
        else:
            self.character.add_gear(gear)
        self.characterChanged.emit(self.character)

    def check_war_breakout(self):
        """Check if war breaks out

        Returns:
            True if war breaks out, False otherwise
        """
        return self.career_controller.check_war_breakout()

    def _on_war_broken_out(self):
        """Handle war breaking out"""
        self.war_broken_out = True
        self.warBrokenOut.emit()

    def _on_career_completed(self, career_data):
        """Handle career completion

        Args:
            career_data: Career data dictionary
        """
        # Update character
        self.characterChanged.emit(self.character)

    def complete_character(self):
        """Mark character as completed"""
        self.character_completed = True
        self.characterCompleted.emit()

    def save_character(self, filename):
        """Save character to file

        Args:
            filename: File path to save to

        Returns:
            True if successful, False otherwise
        """
        try:
            # Convert character to dictionary
            character_dict = self.character.to_dict()

            # Write to file
            with open(filename, "w") as f:
                json.dump(character_dict, f, indent=4)

            return True
        except Exception as e:
            print(f"Error saving character: {e}")
            return False

    def load_character(self, filename):
        """Load character from file

        Args:
            filename: File path to load from

        Returns:
            True if successful, False otherwise
        """
        try:
            # Read from file
            with open(filename, "r") as f:
                character_dict = json.load(f)

            # Create character from dictionary
            self.character = Character.from_dict(character_dict)

            # Update career controller
            self.career_controller.set_character(self.character)

            # Set state based on loaded character
            self.war_broken_out = self.character.war_experience
            self.character_completed = True

            # Emit signals
            self.characterChanged.emit(self.character)
            if self.war_broken_out:
                self.warBrokenOut.emit()
            self.characterCompleted.emit()

            return True
        except Exception as e:
            print(f"Error loading character: {e}")
            return False

    def export_to_pdf(self, filename):
        """Export character to PDF

        Args:
            filename: File path to save to

        Returns:
            True if successful, False otherwise
        """
        from src.utils.pdf_exporter import PDFExporter, check_file_extension

        # Ensure filename has .pdf extension
        filename = check_file_extension(filename, ".pdf")

        # Create exporter
        exporter = PDFExporter(self.character)

        # Export character sheet
        return exporter.export_to_pdf(filename)

    def roll_attributes(self):
        """Roll random attributes

        Returns:
            Dictionary of attribute letters
        """
        # Reset attributes to all C
        self.character.reset_attributes()

        # Roll 2D3-2 for number of attribute increases (0-4)
        num_increases = min(4, max(0, (self.dice_controller.roll_die(3) + self.dice_controller.roll_die(3) - 2)))

        # Apply random increases
        attributes = ["STR", "AGL", "INT", "EMP"]
        import random

        for _ in range(num_increases):
            # Select random attribute
            attr = random.choice(attributes)

            # Improve it if not already at A
            if self.character.get_attribute_letter(attr) != "A":
                current_letter = self.character.get_attribute_letter(attr)
                new_letter = chr(ord(current_letter) - 1)  # A is better than B
                self.character.set_attribute_letter(attr, new_letter)

        # Calculate derived attributes
        self.character.calculate_derived_attributes()

        # Update character
        self.characterChanged.emit(self.character)

        return {attr: self.character.get_attribute_letter(attr) for attr in attributes}

    def roll_for_radiation(self):
        """Roll for radiation exposure

        Returns:
            Number of radiation points
        """
        radiation = self.dice_controller.roll_for_radiation()
        self.character.radiation = radiation
        self.characterChanged.emit(self.character)
        return radiation

    def get_starting_gear(self, career_category, career_name):
        """Get starting gear for a career

        Args:
            career_category: Career category
            career_name: Career name

        Returns:
            List of starting gear items
        """
        from src.data.gear import get_starting_gear
        return get_starting_gear(career_category, career_name)

    def get_nationality_gear(self, nationality, military=True):
        """Get nationality-specific gear

        Args:
            nationality: Character nationality
            military: Whether to get military or civilian gear

        Returns:
            List of nationality-specific gear
        """
        from src.data.nationalities import get_nationality_gear
        return get_nationality_gear(nationality, military)

    def select_career(self, category, career_name):
        """Select a career for the character

        Args:
            category: Career category
            career_name: Career name

        Returns:
            Dictionary with career data or None if not found
        """
        return self.career_controller.select_career(category, career_name)

    def select_specialty(self, specialty):
        """Select a specialty for the current career

        Args:
            specialty: Specialty name

        Returns:
            True if successful, False otherwise
        """
        return self.career_controller.select_specialty(specialty)

    def roll_for_promotion(self):
        """Roll for promotion

        Returns:
            True if promoted, False otherwise
        """
        return self.career_controller.roll_for_promotion()

    def complete_career(self):
        """Complete the current career and add it to the character

        Returns:
            Career data dictionary or None if no current career
        """
        return self.career_controller.complete_career()

    def get_available_careers(self, is_first_career=False):
        """Get list of careers available to the character

        Args:
            is_first_career: Whether this is the character's first career

        Returns:
            List of dictionaries with career info
        """
        return self.career_controller.get_available_careers(is_first_career)

    def get_career_specialties(self, category=None, career_name=None):
        """Get specialties for a career

        Args:
            category: Career category
            career_name: Career name

        Returns:
            List of specialties for the career
        """
        return self.career_controller.get_career_specialties(category, career_name)

    def roll_random_career(self, eligible_only=True):
        """Roll for a random career

        Args:
            eligible_only: Whether to only consider careers the character is eligible for

        Returns:
            Dictionary with career data or None if no eligible careers
        """
        return self.career_controller.roll_random_career(eligible_only)

    def roll_random_specialty(self):
        """Roll for a random specialty for the current career

        Returns:
            Specialty name or None if no current career
        """
        return self.career_controller.roll_random_specialty()


# Create a global instance for easy access
game_controller = GameController()