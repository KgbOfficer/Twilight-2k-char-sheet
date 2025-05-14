"""
character_controller.py - Controller for character operations
"""

from PyQt6.QtCore import QObject, pyqtSignal
from src.models.character import Character
from src.models.attribute import Attribute, AttributeSet
from src.models.skill import Skill, SkillSet, Specialty, SpecialtySet
from src.controllers.dice_controller import DiceController


class CharacterController(QObject):
    """Controller for character-specific operations"""

    # Signals
    attributeChanged = pyqtSignal(str, str)  # Attribute name, new value
    skillChanged = pyqtSignal(str, str)  # Skill name, new level
    specialtyAdded = pyqtSignal(str)  # Specialty name
    careerAdded = pyqtSignal(dict)  # Career data
    characterUpdated = pyqtSignal(object)  # Character object

    def __init__(self, character=None):
        """Initialize the character controller

        Args:
            character: Optional character object to control
        """
        super().__init__()
        self.character = character or Character()
        self.dice_controller = DiceController()

    def set_character(self, character):
        """Set the character to control

        Args:
            character: Character object
        """
        self.character = character
        self.characterUpdated.emit(self.character)

    def get_character(self):
        """Get the current character

        Returns:
            Character object
        """
        return self.character

    def set_basic_info(self, name, nationality):
        """Set character's basic information

        Args:
            name: Character name
            nationality: Character nationality
        """
        self.character.name = name
        self.character.nationality = nationality
        self.characterUpdated.emit(self.character)

    def set_attribute(self, attribute, letter):
        """Set an attribute value

        Args:
            attribute: Attribute name (STR, AGL, INT, EMP)
            letter: Attribute letter (A, B, C, D)

        Returns:
            True if successful, False otherwise
        """
        if attribute in self.character.attributes and letter in ["A", "B", "C", "D"]:
            self.character.set_attribute_letter(attribute, letter)
            self.attributeChanged.emit(attribute, letter)
            self.characterUpdated.emit(self.character)
            return True
        return False

    def modify_attribute(self, attribute, steps):
        """Modify an attribute by a number of steps

        Args:
            attribute: Attribute name (STR, AGL, INT, EMP)
            steps: Number of steps to modify (positive = improve, negative = decrease)

        Returns:
            True if successful, False otherwise
        """
        if attribute not in self.character.attributes:
            return False

        current_letter = self.character.get_attribute_letter(attribute)
        current_ord = ord(current_letter)

        # Calculate new letter (A = 65, B = 66, C = 67, D = 68)
        new_ord = current_ord - steps  # Negative steps because A is better than D

        # Ensure new letter is in valid range
        if new_ord < 65:  # A
            new_ord = 65
        elif new_ord > 68:  # D
            new_ord = 68

        new_letter = chr(new_ord)
        return self.set_attribute(attribute, new_letter)

    def add_skill(self, skill, level):
        """Add or improve a skill

        Args:
            skill: Skill name
            level: Skill level (A, B, C, D or F)

        Returns:
            True if skill was added or improved, False otherwise
        """
        current_level = self.character.skills.get(skill, "F")

        # Only update if new level is better
        if self._compare_levels(level, current_level) < 0:
            self.character.skills[skill] = level
            self.skillChanged.emit(skill, level)
            self.characterUpdated.emit(self.character)
            return True
        return False

    def _compare_levels(self, level1, level2):
        """Compare two skill levels

        Returns:
            -1 if level1 is better than level2
            0 if they are equal
            1 if level2 is better than level1
        """
        # Convert to numeric values (A=0, B=1, C=2, D=3, F=4)
        level_map = {"A": 0, "B": 1, "C": 2, "D": 3, "F": 4}

        level1_value = level_map.get(level1, 4)
        level2_value = level_map.get(level2, 4)

        if level1_value < level2_value:
            return -1
        elif level1_value > level2_value:
            return 1
        else:
            return 0

    def improve_skill(self, skill, steps=1):
        """Improve a skill by a number of steps

        Args:
            skill: Skill name
            steps: Number of steps to improve

        Returns:
            True if skill was improved, False otherwise
        """
        current_level = self.character.skills.get(skill, "F")

        # Convert to numeric value
        level_map = {"A": 0, "B": 1, "C": 2, "D": 3, "F": 4}
        level_rev = {0: "A", 1: "B", 2: "C", 3: "D", 4: "F"}

        current_value = level_map.get(current_level, 4)
        new_value = max(0, current_value - steps)  # Negative steps because A is better than F
        new_level = level_rev[new_value]

        if new_value == current_value:
            return False  # No change

        return self.add_skill(skill, new_level)

    def add_specialty(self, specialty):
        """Add a specialty

        Args:
            specialty: Specialty name

        Returns:
            True if specialty was added, False if already had it
        """
        if self.character.has_specialty(specialty):
            return False

        self.character.add_specialty(specialty)
        self.specialtyAdded.emit(specialty)
        self.characterUpdated.emit(self.character)
        return True

    def add_career(self, career_type, branch=None, rank=None, promotion=False):
        """Add a career to the character's history

        Args:
            career_type: Type of career
            branch: Branch or specific career
            rank: Military rank or position
            promotion: Whether character was promoted

        Returns:
            Career data dictionary
        """
        career = {
            "type": career_type,
            "branch": branch,
            "rank": rank,
            "promotion": promotion,
            "age": self.character.age
        }

        self.character.careers.append(career)

        # Increment age by 6 (each career term is 6 years)
        self.character.age += 6

        # If promoted, improve CUF
        if promotion:
            current_cuf = self.character.cuf
            if current_cuf == "D":
                self.character.cuf = "C"
            elif current_cuf == "C":
                self.character.cuf = "B"
            elif current_cuf == "B":
                self.character.cuf = "A"

        self.careerAdded.emit(career)
        self.characterUpdated.emit(self.character)
        return career

    def set_war_experience(self, at_war_career):
        """Set character's war experience

        Args:
            at_war_career: Career during the war

        Returns:
            True if successful, False otherwise
        """
        self.character.set_war_experience(at_war_career)
        self.characterUpdated.emit(self.character)
        return True

    def set_radiation(self, radiation_points):
        """Set character's radiation exposure

        Args:
            radiation_points: Number of radiation points

        Returns:
            True if successful, False otherwise
        """
        if radiation_points < 0 or radiation_points > 5:
            return False

        self.character.radiation = radiation_points
        self.characterUpdated.emit(self.character)
        return True

    def set_character_details(self, moral_code, big_dream, buddy, how_you_met, appearance):
        """Set character's additional details

        Args:
            moral_code: Character's moral code
            big_dream: Character's big dream
            buddy: Character's buddy
            how_you_met: How character met other PCs
            appearance: Character's appearance

        Returns:
            True if successful, False otherwise
        """
        self.character.moral_code = moral_code
        self.character.big_dream = big_dream
        self.character.buddy = buddy
        self.character.how_you_met = how_you_met
        self.character.appearance = appearance
        self.characterUpdated.emit(self.character)
        return True

    def add_gear(self, gear):
        """Add gear to the character's inventory

        Args:
            gear: Gear item or list of gear items

        Returns:
            True if successful, False otherwise
        """
        if isinstance(gear, list):
            for item in gear:
                self.character.add_gear(item)
        else:
            self.character.add_gear(gear)

        self.characterUpdated.emit(self.character)
        return True

    def roll_attributes(self):
        """Roll initial attributes randomly

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
                self.modify_attribute(attr, 1)

        # Calculate derived attributes
        self.character.calculate_derived_attributes()
        self.characterUpdated.emit(self.character)

        return {attr: self.character.get_attribute_letter(attr) for attr in attributes}

    def calculate_derived_attributes(self):
        """Calculate derived attributes (hit and stress capacity)

        Returns:
            Dictionary with hit_capacity and stress_capacity
        """
        self.character.calculate_derived_attributes()
        self.characterUpdated.emit(self.character)

        return {
            "hit_capacity": self.character.hit_capacity,
            "stress_capacity": self.character.stress_capacity
        }

    def roll_for_skill(self, skill):
        """Roll to see if a skill improves during a career

        Args:
            skill: Skill to check

        Returns:
            True if skill improved, False otherwise
        """
        # Roll D6, succeed on 5+
        roll = self.dice_controller.roll_d6()
        if roll >= 5:
            self.improve_skill(skill)
            return True
        return False

    def roll_for_specialty(self, specialties):
        """Roll for a random specialty

        Args:
            specialties: List of specialties to choose from

        Returns:
            Randomly selected specialty
        """
        import random
        specialty = random.choice(specialties)
        self.add_specialty(specialty)
        return specialty

    def get_character_sheet_data(self):
        """Get complete character data for displaying or exporting

        Returns:
            Dictionary of character data
        """
        return self.character.to_dict()

    def save_character(self, filename):
        """Save character to file

        Args:
            filename: File name to save to

        Returns:
            True if successful, False otherwise
        """
        import json

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
            filename: File name to load from

        Returns:
            True if successful, False otherwise
        """
        import json

        try:
            # Read from file
            with open(filename, "r") as f:
                character_dict = json.load(f)

            # Create character from dictionary
            self.character = Character.from_dict(character_dict)
            self.characterUpdated.emit(self.character)

            return True
        except Exception as e:
            print(f"Error loading character: {e}")
            return False


# Create a global instance for easy access
character_controller = CharacterController()