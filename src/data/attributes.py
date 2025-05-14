"""
attributes.py - Attribute data for Twilight 2000 character creation
"""

# Attributes definition
ATTRIBUTES = {
    "STR": {
        "name": "Strength",
        "abbreviation": "STR",
        "description": "Muscle power, toughness, and physical endurance",
        "examples": {
            "A": "Professional athlete, elite soldier",
            "B": "Manual laborer, fit individual",
            "C": "Average adult",
            "D": "Frail, weak, or sickly individual"
        }
    },
    "AGL": {
        "name": "Agility",
        "abbreviation": "AGL",
        "description": "Body control, speed, and fine motor skills",
        "examples": {
            "A": "Gymnast, martial artist",
            "B": "Athlete, dancer",
            "C": "Average adult",
            "D": "Clumsy or slow individual"
        }
    },
    "INT": {
        "name": "Intelligence",
        "abbreviation": "INT",
        "description": "Perception, intellect, and mental stability",
        "examples": {
            "A": "Genius, exceptional mind",
            "B": "Well-educated, quick thinker",
            "C": "Average adult",
            "D": "Slow learner, poor memory"
        }
    },
    "EMP": {
        "name": "Empathy",
        "abbreviation": "EMP",
        "description": "Charisma, amiability, and emotional stability",
        "examples": {
            "A": "Charismatic leader, natural empath",
            "B": "Likable, socially adept",
            "C": "Average adult",
            "D": "Socially awkward, off-putting"
        }
    }
}

# Attribute levels and their corresponding dice
ATTRIBUTE_LEVELS = {
    "A": {"die": "D12", "description": "Extraordinary"},
    "B": {"die": "D10", "description": "Capable"},
    "C": {"die": "D8", "description": "Average"},
    "D": {"die": "D6", "description": "Feeble"}
}


def get_all_attributes():
    """Get a dictionary of all attributes

    Returns:
        Dictionary of attribute data
    """
    return ATTRIBUTES


def get_attribute_info(attribute_name):
    """Get information about a specific attribute

    Args:
        attribute_name: Name or abbreviation of the attribute

    Returns:
        Dictionary with attribute information or None if not found
    """
    if attribute_name in ATTRIBUTES:
        return ATTRIBUTES[attribute_name]

    # Try to find by full name
    for attr, info in ATTRIBUTES.items():
        if info["name"].lower() == attribute_name.lower():
            return info

    return None


def get_attribute_die(attribute_level):
    """Get the die type for an attribute level

    Args:
        attribute_level: Attribute level (A, B, C, or D)

    Returns:
        Die type (D12, D10, D8, or D6)
    """
    level_info = ATTRIBUTE_LEVELS.get(attribute_level, None)
    if not level_info:
        return "D8"  # Default to average (C)

    return level_info["die"]


def get_attribute_die_size(attribute_level):
    """Get the numeric die size for an attribute level

    Args:
        attribute_level: Attribute level (A, B, C, or D)

    Returns:
        Die size (12, 10, 8, or 6)
    """
    die = get_attribute_die(attribute_level)
    return int(die[1:])  # Remove 'D' prefix and convert to int


def get_attribute_description(attribute_name, level):
    """Get a description for an attribute at a specific level

    Args:
        attribute_name: Name or abbreviation of the attribute
        level: Attribute level (A, B, C, or D)

    Returns:
        Description string or None if not found
    """
    attr_info = get_attribute_info(attribute_name)
    if not attr_info:
        return None

    return attr_info["examples"].get(level, None)


def calculate_hit_capacity(str_level, agl_level):
    """Calculate hit capacity based on STR and AGL

    Args:
        str_level: Strength level (A, B, C, or D)
        agl_level: Agility level (A, B, C, or D)

    Returns:
        Hit capacity value
    """
    str_die = get_attribute_die_size(str_level)
    agl_die = get_attribute_die_size(agl_level)

    # Hit capacity = (STR die size + AGL die size) / 4, rounded up
    hit_capacity = (str_die + agl_die) / 4
    return int(hit_capacity + 0.5)  # Round up


def calculate_stress_capacity(int_level, emp_level):
    """Calculate stress capacity based on INT and EMP

    Args:
        int_level: Intelligence level (A, B, C, or D)
        emp_level: Empathy level (A, B, C, or D)

    Returns:
        Stress capacity value
    """
    int_die = get_attribute_die_size(int_level)
    emp_die = get_attribute_die_size(emp_level)

    # Stress capacity = (INT die size + EMP die size) / 4, rounded up
    stress_capacity = (int_die + emp_die) / 4
    return int(stress_capacity + 0.5)  # Round up