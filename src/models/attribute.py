"""
attribute.py - Attribute model for Twilight 2000 character creator
"""


class Attribute:
    """Model for a character attribute"""

    def __init__(self, name, abbreviation, level="C"):
        """Initialize a new attribute

        Args:
            name: Full attribute name (e.g., "Strength")
            abbreviation: Abbreviation (e.g., "STR")
            level: Attribute level (A, B, C, or D)
        """
        self.name = name
        self.abbreviation = abbreviation
        self.level = level if level in ["A", "B", "C", "D"] else "C"

    def get_level(self):
        """Get the attribute level

        Returns:
            Attribute level letter (A, B, C, or D)
        """
        return self.level

    def set_level(self, level):
        """Set the attribute level

        Args:
            level: Attribute level (A, B, C, or D)

        Returns:
            True if level was set, False if invalid level
        """
        if level in ["A", "B", "C", "D"]:
            self.level = level
            return True
        return False

    def improve(self, steps=1):
        """Improve the attribute by a number of steps

        Args:
            steps: Number of steps to improve (1 = C to B)

        Returns:
            Number of steps actually improved
        """
        level_map = {"A": 0, "B": 1, "C": 2, "D": 3}
        level_rev = {0: "A", 1: "B", 2: "C", 3: "D"}

        current_value = level_map.get(self.level, 2)  # Default to C
        new_value = max(0, current_value - steps)  # Lower value is better (A = 0)

        actual_steps = current_value - new_value

        self.level = level_rev[new_value]

        return actual_steps

    def decrease(self, steps=1):
        """Decrease the attribute by a number of steps

        Args:
            steps: Number of steps to decrease (1 = B to C)

        Returns:
            Number of steps actually decreased
        """
        level_map = {"A": 0, "B": 1, "C": 2, "D": 3}
        level_rev = {0: "A", 1: "B", 2: "C", 3: "D"}

        current_value = level_map.get(self.level, 2)  # Default to C
        new_value = min(3, current_value + steps)  # Higher value is worse (D = 3)

        actual_steps = new_value - current_value

        self.level = level_rev[new_value]

        return actual_steps

    def get_die_type(self):
        """Get the die type for this attribute

        Returns:
            Die type (D12, D10, D8, or D6)
        """
        die_map = {"A": "D12", "B": "D10", "C": "D8", "D": "D6"}
        return die_map.get(self.level, "D8")

    def get_die_size(self):
        """Get the numeric die size for this attribute

        Returns:
            Die size (12, 10, 8, or 6)
        """
        size_map = {"A": 12, "B": 10, "C": 8, "D": 6}
        return size_map.get(self.level, 8)

    def get_description(self):
        """Get a description of the attribute at its current level

        Returns:
            Description string
        """
        from src.data.attributes import get_attribute_description
        return get_attribute_description(self.abbreviation, self.level)

    def to_dict(self):
        """Convert attribute to dictionary for saving

        Returns:
            Dictionary representation of the attribute
        """
        return {
            "name": self.name,
            "abbreviation": self.abbreviation,
            "level": self.level
        }

    @classmethod
    def from_dict(cls, data):
        """Create attribute from dictionary

        Args:
            data: Dictionary with attribute data

        Returns:
            Attribute object
        """
        return cls(
            name=data.get("name", ""),
            abbreviation=data.get("abbreviation", ""),
            level=data.get("level", "C")
        )

    def __str__(self):
        """String representation of the attribute

        Returns:
            String in format "STR: B (D10)"
        """
        return f"{self.abbreviation}: {self.level} ({self.get_die_type()})"


class AttributeSet:
    """Collection of attributes for a character"""

    def __init__(self):
        """Initialize with default attributes"""
        self.attributes = {
            "STR": Attribute("Strength", "STR", "C"),
            "AGL": Attribute("Agility", "AGL", "C"),
            "INT": Attribute("Intelligence", "INT", "C"),
            "EMP": Attribute("Empathy", "EMP", "C")
        }

    def get_attribute(self, abbreviation):
        """Get an attribute by abbreviation

        Args:
            abbreviation: Attribute abbreviation (STR, AGL, INT, EMP)

        Returns:
            Attribute object or None if not found
        """
        return self.attributes.get(abbreviation.upper())

    def get_level(self, abbreviation):
        """Get attribute level by abbreviation

        Args:
            abbreviation: Attribute abbreviation (STR, AGL, INT, EMP)

        Returns:
            Attribute level or None if not found
        """
        attribute = self.get_attribute(abbreviation)
        if attribute:
            return attribute.get_level()
        return None

    def set_level(self, abbreviation, level):
        """Set attribute level by abbreviation

        Args:
            abbreviation: Attribute abbreviation (STR, AGL, INT, EMP)
            level: Attribute level (A, B, C, or D)

        Returns:
            True if level was set, False if invalid level or attribute not found
        """
        attribute = self.get_attribute(abbreviation)
        if attribute:
            return attribute.set_level(level)
        return False

    def improve_attribute(self, abbreviation, steps=1):
        """Improve an attribute by a number of steps

        Args:
            abbreviation: Attribute abbreviation (STR, AGL, INT, EMP)
            steps: Number of steps to improve

        Returns:
            Number of steps actually improved
        """
        attribute = self.get_attribute(abbreviation)
        if attribute:
            return attribute.improve(steps)
        return 0

    def decrease_attribute(self, abbreviation, steps=1):
        """Decrease an attribute by a number of steps

        Args:
            abbreviation: Attribute abbreviation (STR, AGL, INT, EMP)
            steps: Number of steps to decrease

        Returns:
            Number of steps actually decreased
        """
        attribute = self.get_attribute(abbreviation)
        if attribute:
            return attribute.decrease(steps)
        return 0

    def reset_attributes(self):
        """Reset all attributes to C"""
        for attribute in self.attributes.values():
            attribute.set_level("C")

    def calculate_hit_capacity(self):
        """Calculate hit capacity

        Returns:
            Hit capacity value
        """
        str_attr = self.get_attribute("STR")
        agl_attr = self.get_attribute("AGL")

        if not str_attr or not agl_attr:
            return 4  # Default

        # Hit capacity = (STR die size + AGL die size) / 4, rounded up
        hit_capacity = (str_attr.get_die_size() + agl_attr.get_die_size()) / 4
        return int(hit_capacity + 0.5)  # Round up

    def calculate_stress_capacity(self):
        """Calculate stress capacity

        Returns:
            Stress capacity value
        """
        int_attr = self.get_attribute("INT")
        emp_attr = self.get_attribute("EMP")

        if not int_attr or not emp_attr:
            return 4  # Default

        # Stress capacity = (INT die size + EMP die size) / 4, rounded up
        stress_capacity = (int_attr.get_die_size() + emp_attr.get_die_size()) / 4
        return int(stress_capacity + 0.5)  # Round up

    def to_dict(self):
        """Convert attribute set to dictionary for saving

        Returns:
            Dictionary representation of the attribute set
        """
        return {attr_key: attr.to_dict() for attr_key, attr in self.attributes.items()}

    @classmethod
    def from_dict(cls, data):
        """Create attribute set from dictionary

        Args:
            data: Dictionary with attribute set data

        Returns:
            AttributeSet object
        """
        attribute_set = cls()

        for attr_key, attr_data in data.items():
            if attr_key in attribute_set.attributes:
                attribute_set.attributes[attr_key] = Attribute.from_dict(attr_data)

        return attribute_set