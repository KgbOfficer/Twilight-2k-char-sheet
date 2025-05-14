"""
skill.py - Skill and Specialty models for Twilight 2000 character creator
"""


class Skill:
    """Model for a character skill"""

    def __init__(self, name, level="F", attribute=None):
        """Initialize a new skill

        Args:
            name: Skill name
            level: Skill level (A, B, C, D, or F)
            attribute: Associated attribute (STR, AGL, INT, EMP)
        """
        self.name = name
        self.level = level if level in ["A", "B", "C", "D", "F"] else "F"
        self.attribute = attribute

    def get_level(self):
        """Get the skill level

        Returns:
            Skill level letter (A, B, C, D, or F)
        """
        return self.level

    def set_level(self, level):
        """Set the skill level

        Args:
            level: Skill level (A, B, C, D, or F)

        Returns:
            True if level was set, False if invalid level
        """
        if level in ["A", "B", "C", "D", "F"]:
            self.level = level
            return True
        return False

    def improve(self, steps=1):
        """Improve the skill by a number of steps

        Args:
            steps: Number of steps to improve (1 = D to C)

        Returns:
            Number of steps actually improved
        """
        level_map = {"A": 0, "B": 1, "C": 2, "D": 3, "F": 4}
        level_rev = {0: "A", 1: "B", 2: "C", 3: "D", 4: "F"}

        current_value = level_map.get(self.level, 4)  # Default to F
        new_value = max(0, current_value - steps)  # Lower value is better (A = 0)

        actual_steps = current_value - new_value

        self.level = level_rev[new_value]

        return actual_steps

    def get_die_type(self):
        """Get the die type for this skill

        Returns:
            Die type (D12, D10, D8, D6, or None)
        """
        die_map = {"A": "D12", "B": "D10", "C": "D8", "D": "D6", "F": "None"}
        return die_map.get(self.level, "None")

    def get_die_size(self):
        """Get the numeric die size for this skill

        Returns:
            Die size (12, 10, 8, 6, or 0)
        """
        size_map = {"A": 12, "B": 10, "C": 8, "D": 6, "F": 0}
        return size_map.get(self.level, 0)

    def to_dict(self):
        """Convert skill to dictionary for saving

        Returns:
            Dictionary representation of the skill
        """
        return {
            "name": self.name,
            "level": self.level,
            "attribute": self.attribute
        }

    @classmethod
    def from_dict(cls, data):
        """Create skill from dictionary

        Args:
            data: Dictionary with skill data

        Returns:
            Skill object
        """
        return cls(
            name=data.get("name", ""),
            level=data.get("level", "F"),
            attribute=data.get("attribute")
        )

    def __str__(self):
        """String representation of the skill

        Returns:
            String in format "Close Combat: B (D10)"
        """
        return f"{self.name}: {self.level} ({self.get_die_type()})"


class SkillSet:
    """Collection of skills for a character"""

    def __init__(self):
        """Initialize an empty skill set"""
        self.skills = {}

    def add_skill(self, name, level="F", attribute=None):
        """Add a skill to the set

        Args:
            name: Skill name
            level: Skill level (A, B, C, D, or F)
            attribute: Associated attribute (STR, AGL, INT, EMP)

        Returns:
            True if skill was added or improved, False otherwise
        """
        # Check if skill already exists
        if name in self.skills:
            current_level = self.skills[name].get_level()

            # Only update if new level is better
            if self._compare_levels(level, current_level) < 0:
                self.skills[name].set_level(level)
                return True
            return False

        # Add new skill
        self.skills[name] = Skill(name, level, attribute)
        return True

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

    def get_skill(self, name):
        """Get a skill by name

        Args:
            name: Skill name

        Returns:
            Skill object or None if not found
        """
        return self.skills.get(name)

    def get_level(self, name):
        """Get skill level by name

        Args:
            name: Skill name

        Returns:
            Skill level or "F" if not found
        """
        skill = self.get_skill(name)
        if skill:
            return skill.get_level()
        return "F"

    def improve_skill(self, name, steps=1):
        """Improve a skill by a number of steps

        Args:
            name: Skill name
            steps: Number of steps to improve

        Returns:
            Number of steps actually improved, or 0 if skill not found
        """
        skill = self.get_skill(name)
        if skill:
            return skill.improve(steps)
        return 0

    def to_dict(self):
        """Convert skill set to dictionary for saving

        Returns:
            Dictionary mapping skill names to levels
        """
        return {name: skill.level for name, skill in self.skills.items()}

    @classmethod
    def from_dict(cls, data):
        """Create skill set from dictionary

        Args:
            data: Dictionary mapping skill names to levels

        Returns:
            SkillSet object
        """
        skill_set = cls()

        for name, level in data.items():
            skill_set.add_skill(name, level)

        return skill_set


class Specialty:
    """Model for a character specialty"""

    def __init__(self, name, description=None, parent_skill=None):
        """Initialize a new specialty

        Args:
            name: Specialty name
            description: Specialty description
            parent_skill: Parent skill name
        """
        self.name = name
        self.description = description
        self.parent_skill = parent_skill

    def to_dict(self):
        """Convert specialty to dictionary for saving

        Returns:
            Dictionary representation of the specialty
        """
        return {
            "name": self.name,
            "description": self.description,
            "parent_skill": self.parent_skill
        }

    @classmethod
    def from_dict(cls, data):
        """Create specialty from dictionary

        Args:
            data: Dictionary with specialty data

        Returns:
            Specialty object
        """
        return cls(
            name=data.get("name", ""),
            description=data.get("description"),
            parent_skill=data.get("parent_skill")
        )

    def __str__(self):
        """String representation of the specialty

        Returns:
            String with name and parent skill if available
        """
        if self.parent_skill:
            return f"{self.name} ({self.parent_skill})"
        return self.name


class SpecialtySet:
    """Collection of specialties for a character"""

    def __init__(self):
        """Initialize an empty specialty set"""
        self.specialties = {}

    def add_specialty(self, name, description=None, parent_skill=None):
        """Add a specialty to the set

        Args:
            name: Specialty name
            description: Specialty description
            parent_skill: Parent skill name

        Returns:
            True if specialty was added, False if already exists
        """
        if name in self.specialties:
            return False

        self.specialties[name] = Specialty(name, description, parent_skill)
        return True

    def has_specialty(self, name):
        """Check if character has a specialty

        Args:
            name: Specialty name

        Returns:
            True if character has the specialty, False otherwise
        """
        return name in self.specialties

    def get_specialty(self, name):
        """Get a specialty by name

        Args:
            name: Specialty name

        Returns:
            Specialty object or None if not found
        """
        return self.specialties.get(name)

    def get_specialties_for_skill(self, skill_name):
        """Get all specialties for a skill

        Args:
            skill_name: Skill name

        Returns:
            List of specialty names for the skill
        """
        return [name for name, specialty in self.specialties.items()
                if specialty.parent_skill == skill_name]

    def to_dict(self):
        """Convert specialty set to dictionary for saving

        Returns:
            Dictionary mapping specialty names to True
        """
        return {name: True for name in self.specialties}

    @classmethod
    def from_dict(cls, data):
        """Create specialty set from dictionary

        Args:
            data: Dictionary mapping specialty names to True/False

        Returns:
            SpecialtySet object
        """
        specialty_set = cls()

        for name, has_specialty in data.items():
            if has_specialty:
                specialty_set.add_specialty(name)

        return specialty_set