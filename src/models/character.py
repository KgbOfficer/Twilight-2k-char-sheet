"""
character.py - Character model
"""


class Character:
    """Model for a player character"""

    def __init__(self):
        """Initialize a new character"""
        # Basic info
        self.name = ""
        self.nationality = ""
        self.age = 18

        # Attributes (all start at C - Average)
        self.attributes = {
            "STR": "C",  # Strength
            "AGL": "C",  # Agility
            "INT": "C",  # Intelligence
            "EMP": "C",  # Empathy
        }

        # Derived attributes
        self.hit_capacity = 0  # Physical health
        self.stress_capacity = 0  # Mental health

        # Skills - dictionary mapping skill names to levels (A, B, C, D or F)
        self.skills = {}

        # Specialties - dictionary mapping specialty names to boolean (has/doesn't have)
        self.specialties = {}

        # Background
        self.childhood = ""
        self.childhood_specialty = ""

        # Career history - list of dictionaries with career info
        self.careers = []

        # Coolness Under Fire (CUF)
        self.cuf = "D"  # Start at D (default for age 18)

        # Moral code
        self.moral_code = ""

        # Big dream
        self.big_dream = ""

        # Buddy
        self.buddy = ""

        # How you met other PCs
        self.how_you_met = ""

        # Appearance
        self.appearance = ""

        # War experience
        self.war_experience = False
        self.at_war_career = ""

        # Gear
        self.gear = []

        # Permanent radiation
        self.radiation = 0

    def get_attribute_letter(self, attribute):
        """Get the letter rating for an attribute"""
        if attribute in self.attributes:
            return self.attributes[attribute]
        return "C"  # Default to C if not found

    def set_attribute_letter(self, attribute, letter):
        """Set the letter rating for an attribute"""
        if attribute in self.attributes and letter in ["A", "B", "C", "D"]:
            self.attributes[attribute] = letter

    def get_attribute_die(self, attribute):
        """Get the die type for an attribute"""
        # A = D12, B = D10, C = D8, D = D6
        die_map = {"A": "D12", "B": "D10", "C": "D8", "D": "D6"}
        return die_map.get(self.get_attribute_letter(attribute), "D8")

    def get_attribute_die_size(self, attribute):
        """Get the numeric die size for an attribute"""
        # A = 12, B = 10, C = 8, D = 6
        die_map = {"A": 12, "B": 10, "C": 8, "D": 6}
        return die_map.get(self.get_attribute_letter(attribute), 8)

    def reset_attributes(self):
        """Reset all attributes to C"""
        for attr in self.attributes:
            self.attributes[attr] = "C"

    def calculate_derived_attributes(self):
        """Calculate derived attributes (hit and stress capacity)"""
        # Hit capacity = (STR die size + AGL die size) / 4, rounded up
        hit_capacity = (self.get_attribute_die_size("STR") + self.get_attribute_die_size("AGL")) / 4
        self.hit_capacity = int(hit_capacity + 0.5)  # Round up

        # Stress capacity = (INT die size + EMP die size) / 4, rounded up
        stress_capacity = (self.get_attribute_die_size("INT") + self.get_attribute_die_size("EMP")) / 4
        self.stress_capacity = int(stress_capacity + 0.5)  # Round up

    def add_skill(self, skill, level):
        """Add or improve a skill

        Args:
            skill: Skill name
            level: Skill level (A, B, C, D or F)
        """
        # Check if already has skill at better level
        current_level = self.skills.get(skill, "F")

        # Only update if new level is better (A > B > C > D > F)
        if self._compare_levels(level, current_level) < 0:
            self.skills[skill] = level

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

    def add_specialty(self, specialty):
        """Add a specialty

        Args:
            specialty: Specialty name
        """
        self.specialties[specialty] = True

    def has_specialty(self, specialty):
        """Check if character has a specialty

        Args:
            specialty: Specialty name

        Returns:
            True if character has the specialty, False otherwise
        """
        return self.specialties.get(specialty, False)

    def add_career(self, career_type, branch=None, rank=None, promotion=False):
        """Add a career to the character's history

        Args:
            career_type: Type of career (e.g., "Military", "Civilian")
            branch: Branch or specific career (e.g., "Army", "Police")
            rank: Military rank or position
            promotion: Whether character was promoted during this career
        """
        career = {
            "type": career_type,
            "branch": branch,
            "rank": rank,
            "promotion": promotion,
            "age": self.age
        }

        self.careers.append(career)

        # Increment age by 6 (each career term is 6 years)
        self.age += 6

    def add_gear(self, gear):
        """Add gear to the character's inventory

        Args:
            gear: Gear name or description
        """
        self.gear.append(gear)

    def set_war_experience(self, career):
        """Set character's war experience

        Args:
            career: Career during the war
        """
        self.war_experience = True
        self.at_war_career = career

    def to_dict(self):
        """Convert character to dictionary for saving"""
        return {
            "name": self.name,
            "nationality": self.nationality,
            "age": self.age,
            "attributes": self.attributes.copy(),
            "hit_capacity": self.hit_capacity,
            "stress_capacity": self.stress_capacity,
            "skills": self.skills.copy(),
            "specialties": self.specialties.copy(),
            "childhood": self.childhood,
            "childhood_specialty": self.childhood_specialty,
            "careers": self.careers.copy(),
            "cuf": self.cuf,
            "moral_code": self.moral_code,
            "big_dream": self.big_dream,
            "buddy": self.buddy,
            "how_you_met": self.how_you_met,
            "appearance": self.appearance,
            "war_experience": self.war_experience,
            "at_war_career": self.at_war_career,
            "gear": self.gear.copy(),
            "radiation": self.radiation
        }

    @classmethod
    def from_dict(cls, data):
        """Create character from dictionary

        Args:
            data: Dictionary with character data

        Returns:
            Character object
        """
        character = cls()

        # Set basic properties
        character.name = data.get("name", "")
        character.nationality = data.get("nationality", "")
        character.age = data.get("age", 18)

        # Set attributes
        if "attributes" in data:
            character.attributes = data["attributes"].copy()

        # Set derived attributes
        character.hit_capacity = data.get("hit_capacity", 0)
        character.stress_capacity = data.get("stress_capacity", 0)

        # Set skills and specialties
        if "skills" in data:
            character.skills = data["skills"].copy()

        if "specialties" in data:
            character.specialties = data["specialties"].copy()

        # Set background
        character.childhood = data.get("childhood", "")
        character.childhood_specialty = data.get("childhood_specialty", "")

        # Set careers
        if "careers" in data:
            character.careers = data["careers"].copy()

        # Set other properties
        character.cuf = data.get("cuf", "D")
        character.moral_code = data.get("moral_code", "")
        character.big_dream = data.get("big_dream", "")
        character.buddy = data.get("buddy", "")
        character.how_you_met = data.get("how_you_met", "")
        character.appearance = data.get("appearance", "")

        # Set war experience
        character.war_experience = data.get("war_experience", False)
        character.at_war_career = data.get("at_war_career", "")

        # Set gear
        if "gear" in data:
            character.gear = data["gear"].copy()

        # Set radiation
        character.radiation = data.get("radiation", 0)

        return character