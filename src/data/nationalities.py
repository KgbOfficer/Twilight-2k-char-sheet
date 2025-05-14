"""
nationalities.py - Nationality data for character creation
"""

# List of available nationalities
NATIONALITIES = [
    "American",
    "Soviet",
    "Polish",
    "Swedish",
    "British",
    "French",
    "German",
    "Italian",
    "Spanish",
    "Finnish",
    "Norwegian",
    "Danish",
    "Dutch",
    "Belgian",
    "Austrian",
    "Swiss",
    "Hungarian",
    "Romanian",
    "Czech",
    "Slovak",
    "Ukrainian",
    "Belarusian",
    "Lithuanian",
    "Latvian",
    "Estonian",
    "Other"
]

# Languages associated with nationalities
NATIONALITY_LANGUAGES = {
    "American": ["English"],
    "Soviet": ["Russian"],
    "Polish": ["Polish", "Russian"],
    "Swedish": ["Swedish"],
    "British": ["English"],
    "French": ["French"],
    "German": ["German"],
    "Italian": ["Italian"],
    "Spanish": ["Spanish"],
    "Finnish": ["Finnish", "Swedish"],
    "Norwegian": ["Norwegian"],
    "Danish": ["Danish"],
    "Dutch": ["Dutch"],
    "Belgian": ["Dutch", "French"],
    "Austrian": ["German"],
    "Swiss": ["German", "French", "Italian"],
    "Hungarian": ["Hungarian"],
    "Romanian": ["Romanian"],
    "Czech": ["Czech"],
    "Slovak": ["Slovak"],
    "Ukrainian": ["Ukrainian", "Russian"],
    "Belarusian": ["Belarusian", "Russian"],
    "Lithuanian": ["Lithuanian", "Russian"],
    "Latvian": ["Latvian", "Russian"],
    "Estonian": ["Estonian", "Russian"],
    "Other": []
}

# Starting gear based on nationality
NATIONALITY_GEAR = {
    "American": {
        "military": ["M16A2 assault rifle", "M1911A1 pistol", "ALICE pack"],
        "civilian": ["Hunting rifle", "S&W Model 10 revolver", "Backpack"]
    },
    "Soviet": {
        "military": ["AK-74 assault rifle", "Makarov PM pistol", "Soviet field pack"],
        "civilian": ["Hunting rifle", "Makarov PM pistol", "Backpack"]
    },
    "Polish": {
        "military": ["AKM assault rifle", "P-64 pistol", "Field pack"],
        "civilian": ["Hunting shotgun", "P-64 pistol", "Backpack"]
    },
    "Swedish": {
        "military": ["AK5 assault rifle", "Glock 17 pistol", "Field pack"],
        "civilian": ["Hunting rifle", "Glock 17 pistol", "Backpack"]
    },
    "British": {
        "military": ["L85A1 assault rifle", "Browning Hi-Power pistol", "PLCE webbing"],
        "civilian": ["Hunting shotgun", "Webley revolver", "Backpack"]
    },
    "French": {
        "military": ["FAMAS assault rifle", "MAC 50 pistol", "Field pack"],
        "civilian": ["Hunting rifle", "MAB Model D pistol", "Backpack"]
    },
    "German": {
        "military": ["G3 battle rifle", "P1 pistol", "Field pack"],
        "civilian": ["Hunting rifle", "Walther P38 pistol", "Backpack"]
    },
    "Italian": {
        "military": ["Beretta AR70 assault rifle", "Beretta 92 pistol", "Field pack"],
        "civilian": ["Hunting shotgun", "Beretta 92 pistol", "Backpack"]
    },
    "Spanish": {
        "military": ["CETME battle rifle", "Star Model 30 pistol", "Field pack"],
        "civilian": ["Hunting shotgun", "Star Model 30 pistol", "Backpack"]
    },
    "Finnish": {
        "military": ["RK 62 assault rifle", "Lahti L-35 pistol", "Field pack"],
        "civilian": ["Hunting rifle", "Lahti L-35 pistol", "Backpack"]
    },
    "Norwegian": {
        "military": ["AG-3 battle rifle", "USP pistol", "Field pack"],
        "civilian": ["Hunting rifle", "USP pistol", "Backpack"]
    },
    "Danish": {
        "military": ["M/95 assault rifle", "SIG P210 pistol", "Field pack"],
        "civilian": ["Hunting rifle", "SIG P210 pistol", "Backpack"]
    },
    "Dutch": {
        "military": ["Diemaco C7 assault rifle", "Browning Hi-Power pistol", "Field pack"],
        "civilian": ["Hunting shotgun", "Browning Hi-Power pistol", "Backpack"]
    },
    "Belgian": {
        "military": ["FNC assault rifle", "Browning Hi-Power pistol", "Field pack"],
        "civilian": ["Hunting shotgun", "Browning Hi-Power pistol", "Backpack"]
    },
    "Austrian": {
        "military": ["Steyr AUG assault rifle", "Glock 17 pistol", "Field pack"],
        "civilian": ["Hunting rifle", "Glock 17 pistol", "Backpack"]
    },
    "Swiss": {
        "military": ["SIG SG 550 assault rifle", "SIG P210 pistol", "Field pack"],
        "civilian": ["Hunting rifle", "SIG P210 pistol", "Backpack"]
    },
    "Hungarian": {
        "military": ["AK-63 assault rifle", "FEG P9R pistol", "Field pack"],
        "civilian": ["Hunting shotgun", "FEG P9R pistol", "Backpack"]
    },
    "Romanian": {
        "military": ["PM md. 65 assault rifle", "TTC pistol", "Field pack"],
        "civilian": ["Hunting rifle", "TTC pistol", "Backpack"]
    },
    "Czech": {
        "military": ["VZ. 58 assault rifle", "CZ 75 pistol", "Field pack"],
        "civilian": ["Hunting rifle", "CZ 75 pistol", "Backpack"]
    },
    "Slovak": {
        "military": ["VZ. 58 assault rifle", "CZ 75 pistol", "Field pack"],
        "civilian": ["Hunting rifle", "CZ 75 pistol", "Backpack"]
    },
    "Ukrainian": {
        "military": ["AK-74 assault rifle", "Fort-12 pistol", "Soviet field pack"],
        "civilian": ["Hunting shotgun", "Fort-12 pistol", "Backpack"]
    },
    "Belarusian": {
        "military": ["AK-74 assault rifle", "Makarov PM pistol", "Soviet field pack"],
        "civilian": ["Hunting rifle", "Makarov PM pistol", "Backpack"]
    },
    "Lithuanian": {
        "military": ["AK-74 assault rifle", "Makarov PM pistol", "Soviet field pack"],
        "civilian": ["Hunting shotgun", "Makarov PM pistol", "Backpack"]
    },
    "Latvian": {
        "military": ["AK-74 assault rifle", "Makarov PM pistol", "Soviet field pack"],
        "civilian": ["Hunting rifle", "Makarov PM pistol", "Backpack"]
    },
    "Estonian": {
        "military": ["AK-74 assault rifle", "Makarov PM pistol", "Soviet field pack"],
        "civilian": ["Hunting rifle", "Makarov PM pistol", "Backpack"]
    },
    # Default gear for any nationality not explicitly listed
    "default": {
        "military": ["Assault rifle", "Pistol", "Field pack"],
        "civilian": ["Hunting rifle", "Pistol", "Backpack"]
    }
}

# Military ranks by nationality
NATIONALITY_RANKS = {
    "American": [
        "Private", "Private First Class", "Corporal/Specialist", "Sergeant", "Staff Sergeant",
        "Sergeant First Class", "Master Sergeant", "First Sergeant", "Sergeant Major",
        "Command Sergeant Major", "Sergeant Major of the Army", "Second Lieutenant",
        "First Lieutenant", "Captain", "Major", "Lieutenant Colonel", "Colonel",
        "Brigadier General", "Major General", "Lieutenant General", "General"
    ],
    "Soviet": [
        "Ryadovoy", "Yefreitor", "Mladshiy Serzhant", "Serzhant", "Starshiy Serzhant",
        "Starshina", "Praporshchik", "Starshiy Praporshchik", "Mladshiy Leytenant",
        "Leytenant", "Starshiy Leytenant", "Kapitan", "Mayor", "Podpolkovnik", "Polkovnik",
        "General-Mayor", "General-Leytenant", "General-Polkovnik", "General Armii", "Marshal"
    ],
    "British": [
        "Private", "Lance Corporal", "Corporal", "Sergeant", "Staff/Colour Sergeant",
        "Warrant Officer Class 2", "Warrant Officer Class 1", "Second Lieutenant",
        "Lieutenant", "Captain", "Major", "Lieutenant Colonel", "Colonel", "Brigadier",
        "Major General", "Lieutenant General", "General", "Field Marshal"
    ],
    # Default ranks for any nationality not explicitly listed
    "default": [
        "Private", "Corporal", "Sergeant", "Lieutenant", "Captain", "Major", "Colonel", "General"
    ]
}


def get_nationality_languages(nationality):
    """Get languages for a nationality

    Args:
        nationality: Nationality name

    Returns:
        List of languages for the nationality
    """
    return NATIONALITY_LANGUAGES.get(nationality, ["English"])


def get_nationality_gear(nationality, military=True):
    """Get starting gear for a nationality

    Args:
        nationality: Nationality name
        military: Whether to get military or civilian gear

    Returns:
        List of gear for the nationality
    """
    gear_type = "military" if military else "civilian"

    # Get gear for the specific nationality, or use default if not found
    nationality_gear = NATIONALITY_GEAR.get(nationality, NATIONALITY_GEAR["default"])

    return nationality_gear.get(gear_type, [])


def get_nationality_ranks(nationality):
    """Get military ranks for a nationality

    Args:
        nationality: Nationality name

    Returns:
        List of military ranks for the nationality
    """
    return NATIONALITY_RANKS.get(nationality, NATIONALITY_RANKS["default"])


def get_rank_equivalence(nationality, rank):
    """Get equivalent rank in other nationalities

    Args:
        nationality: Source nationality
        rank: Rank in the source nationality

    Returns:
        Dictionary mapping nationality to equivalent rank
    """
    # This would be a more complex implementation with actual rank equivalencies
    # For now, just return a simple placeholder
    return {nat: "Equivalent Rank" for nat in NATIONALITIES if nat != nationality}


def is_valid_nationality(nationality):
    """Check if a nationality is valid

    Args:
        nationality: Nationality to check

    Returns:
        True if nationality is valid, False otherwise
    """
    return nationality in NATIONALITIES


def get_all_nationalities():
    """Get list of all nationalities

    Returns:
        List of all nationality names
    """
    return NATIONALITIES