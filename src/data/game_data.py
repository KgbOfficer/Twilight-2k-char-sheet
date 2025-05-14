"""
game_data.py - General game data for Twilight 2000 character creation
"""

# Game data constants
GAME_NAME = "Twilight 2000"
GAME_EDITION = "4th Edition"
GAME_PUBLISHER = "Free League Publishing"

# Timeline data
TIMELINE = {
    1989: "Fall of the Berlin Wall",
    1991: "Dissolution of the Soviet Union",
    1996: "Sino-Soviet War begins",
    1997: "NATO-Soviet conflict escalates",
    1998: "Limited nuclear exchanges",
    1999: "Major conventional war in Europe",
    2000: "Current year - civilization in ruins"
}

# Nuclear exchange data
NUCLEAR_TARGETS = {
    "USA": ["Washington DC", "New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", "San Antonio",
            "San Diego", "Dallas", "San Jose"],
    "Soviet": ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg", "Nizhny Novgorod", "Kazan", "Chelyabinsk",
               "Omsk", "Samara", "Rostov-on-Don"],
    "Europe": ["London", "Paris", "Berlin", "Madrid", "Rome", "Hamburg", "Warsaw", "Vienna", "Budapest", "Brussels"]
}

# Radiation effects
RADIATION_EFFECTS = {
    0: "No radiation sickness",
    1: "Minor symptoms, occasional fatigue",
    2: "Recurring symptoms, periodic illness",
    3: "Moderate sickness, frequent illness",
    4: "Severe symptoms, constant health issues",
    5: "Critical condition, terminal prognosis"
}

# Coolness Under Fire (CUF) levels
CUF_LEVELS = {
    "A": "Elite - Performs exceptionally under pressure",
    "B": "Veteran - Handles stress well, rarely panics",
    "C": "Experienced - Generally steady but may falter",
    "D": "Novice - Prone to panic in dangerous situations"
}

# Unit Morale levels
UNIT_MORALE_LEVELS = {
    "A": "Exceptional - Highly motivated and disciplined",
    "B": "Good - Reliable and steady under pressure",
    "C": "Average - Generally follows orders but may falter",
    "D": "Poor - Unreliable and prone to breaking",
    "F": "Terrible - Likely to desert or surrender"
}

# Time measurements
TIME_UNITS = {
    "Round": {"duration": "5-10 seconds", "primary_use": "Combat"},
    "Stretch": {"duration": "5-10 minutes", "primary_use": "Repairs"},
    "Shift": {"duration": "5-10 hours", "primary_use": "Travel"},
    "Day": {"parts": ["Morning", "Day", "Evening", "Night"]}
}

# Regions and major locations
REGIONS = {
    "Central Europe": {
        "description": "The heart of the conflict, heavily damaged by fighting",
        "countries": ["Germany", "Poland", "Czech Republic", "Austria", "Hungary", "Switzerland"],
        "major_cities": ["Berlin", "Warsaw", "Prague", "Vienna", "Budapest", "Zurich"]
    },
    "Western Europe": {
        "description": "Suffered significant damage but some areas remain functional",
        "countries": ["France", "United Kingdom", "Spain", "Italy", "Netherlands", "Belgium"],
        "major_cities": ["Paris", "London", "Madrid", "Rome", "Amsterdam", "Brussels"]
    },
    "Eastern Europe": {
        "description": "Former Soviet satellites, caught between NATO and Soviet forces",
        "countries": ["Ukraine", "Belarus", "Romania", "Bulgaria", "Moldova", "Slovakia"],
        "major_cities": ["Kiev", "Minsk", "Bucharest", "Sofia", "Chisinau", "Bratislava"]
    },
    "Scandinavia": {
        "description": "Northern European nations with varying levels of involvement",
        "countries": ["Sweden", "Norway", "Finland", "Denmark"],
        "major_cities": ["Stockholm", "Oslo", "Helsinki", "Copenhagen"]
    },
    "North America": {
        "description": "Heavily damaged by nuclear strikes, struggling with regional conflicts",
        "countries": ["United States", "Canada"],
        "major_cities": ["Washington DC", "New York", "Los Angeles", "Chicago", "Toronto", "Montreal"]
    },
    "Soviet Union": {
        "description": "The former superpower, fragmented and in disarray",
        "regions": ["Western Russia", "Eastern Russia", "Siberia", "Caucasus", "Central Asia"],
        "major_cities": ["Moscow", "Saint Petersburg", "Novosibirsk", "Yekaterinburg"]
    }
}

# Factions
FACTIONS = {
    "NATO Remnants": {
        "description": "Remaining organized NATO military forces",
        "alignment": "Western",
        "strength": "Moderate",
        "territory": "Scattered across Western Europe"
    },
    "Soviet Military": {
        "description": "Remnants of the Soviet armed forces",
        "alignment": "Eastern",
        "strength": "Moderate to Strong",
        "territory": "Concentrated in Western Russia and parts of Eastern Europe"
    },
    "Local Militias": {
        "description": "Civilian self-defense groups",
        "alignment": "Varies",
        "strength": "Weak to Moderate",
        "territory": "Localized to specific towns and regions"
    },
    "Warlords": {
        "description": "Military or civilian leaders who have seized power",
        "alignment": "Self-interest",
        "strength": "Varies",
        "territory": "Regional control"
    },
    "Bandits": {
        "description": "Organized criminal groups preying on survivors",
        "alignment": "Self-interest",
        "strength": "Weak to Moderate",
        "territory": "Mobile, targeting vulnerable areas"
    },
    "Survivor Communities": {
        "description": "Organized groups of civilians attempting to rebuild",
        "alignment": "Self-preservation",
        "strength": "Weak",
        "territory": "Small, defensible locations"
    }
}

# Twilight 2000 themes
THEMES = {
    "Survival": "Fighting against the elements and scarcity of resources",
    "Hope": "Believing in a better future despite overwhelming odds",
    "Morality": "Making difficult choices in a world without rules",
    "Community": "Finding or building new families in the ruins",
    "Legacy": "What remains when civilization falls"
}

# Exchange Rates (for barter economy)
EXCHANGE_RATES = {
    "Ammunition": {
        "9mm (10 rounds)": 1,
        "5.56mm (10 rounds)": 2,
        "7.62mm (10 rounds)": 3,
        "12 Gauge (5 shells)": 2
    },
    "Food": {
        "1 day ration": 2,
        "Canned food": 1,
        "Fresh vegetables": 4,
        "Fresh meat": 5
    },
    "Fuel": {
        "1 liter gasoline": 3,
        "1 liter diesel": 4,
        "1 liter alcohol": 2
    },
    "Medicine": {
        "Antibiotics": 10,
        "Painkillers": 5,
        "Bandages": 2,
        "Med-kit": 15
    }
}


def get_game_info():
    """Get basic game information

    Returns:
        Dictionary with game name, edition, and publisher
    """
    return {
        "name": GAME_NAME,
        "edition": GAME_EDITION,
        "publisher": GAME_PUBLISHER
    }


def get_timeline_events():
    """Get timeline events

    Returns:
        Dictionary of years and events
    """
    return TIMELINE


def get_nuclear_targets():
    """Get nuclear targets by region

    Returns:
        Dictionary of regions and their nuclear targets
    """
    return NUCLEAR_TARGETS


def get_radiation_effect(points):
    """Get radiation effect description

    Args:
        points: Number of radiation points

    Returns:
        Description of radiation effects
    """
    # Ensure points is in the valid range
    points = max(0, min(5, points))
    return RADIATION_EFFECTS[points]


def get_cuf_description(level):
    """Get Coolness Under Fire description

    Args:
        level: CUF level (A, B, C, or D)

    Returns:
        Description of CUF level
    """
    return CUF_LEVELS.get(level, "Unknown")


def get_unit_morale_description(level):
    """Get Unit Morale description

    Args:
        level: Morale level (A, B, C, D, or F)

    Returns:
        Description of morale level
    """
    return UNIT_MORALE_LEVELS.get(level, "Unknown")


def get_region_info(region_name):
    """Get information about a region

    Args:
        region_name: Name of the region

    Returns:
        Dictionary with region information or None if not found
    """
    return REGIONS.get(region_name, None)


def get_faction_info(faction_name):
    """Get information about a faction

    Args:
        faction_name: Name of the faction

    Returns:
        Dictionary with faction information or None if not found
    """
    return FACTIONS.get(faction_name, None)


def get_exchange_value(item_type, item_name):
    """Get exchange value of an item

    Args:
        item_type: Type of item (Ammunition, Food, Fuel, Medicine)
        item_name: Name of the item

    Returns:
        Exchange value or 0 if not found
    """
    category = EXCHANGE_RATES.get(item_type, {})
    return category.get(item_name, 0)


def get_all_themes():
    """Get all game themes

    Returns:
        Dictionary of themes and their descriptions
    """
    return THEMES