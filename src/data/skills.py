"""
skills.py - Skill data for Twilight 2000 character creation
"""

# Core skills from the rulebook
CORE_SKILLS = {
    "Close Combat": {
        "description": "Fighting in close quarters with melee weapons or bare hands.",
        "attribute": "STR",
        "specialties": [
            "Brawler", "Melee", "Runner", "Infiltrator", "Scrounger", "Locksmith",
            "Martial Artist", "Killer", "SERE Training", "Scout"
        ]
    },
    "Heavy Weapons": {
        "description": "Use and maintenance of heavy firearms like machine guns, grenade launchers, and anti-tank weapons.",
        "attribute": "STR",
        "specialties": [
            "Rifleman", "Redleg", "Tanker", "Machinegunner", "Launcher Crew", "Combat Engineer",
            "Improvised Munitions"
        ]
    },
    "Mobility": {
        "description": "Moving efficiently through different environments and obstacles.",
        "attribute": "AGL",
        "specialties": [
            "Runner", "Infiltrator", "Martial Artist", "Biker", "Racer", "Boatman",
            "Rider", "Pilot", "Navigator", "Tanker"
        ]
    },
    "Ranged Combat": {
        "description": "Using firearms and projectile weapons effectively.",
        "attribute": "AGL",
        "specialties": [
            "Rifleman", "Sniper", "Ranger", "Sidearms", "Machinegunner", "Launcher Crew",
            "Combat Engineer", "Intelligence"
        ]
    },
    "Stamina": {
        "description": "Physical endurance and resistance to fatigue and stress.",
        "attribute": "STR",
        "specialties": [
            "Runner", "Load Carrier", "Mountaineer", "Ranger", "Brawler", "Martial Artist"
        ]
    },
    "Survival": {
        "description": "Skills for staying alive in hostile environments.",
        "attribute": "INT",
        "specialties": [
            "Hunter", "Farmer", "Forager", "Fisher", "Cook", "Quartermaster",
            "SERE Training"
        ]
    },
    "Recon": {
        "description": "Gathering information through observation and surveillance.",
        "attribute": "INT",
        "specialties": [
            "Scout", "Infiltrator", "Intelligence", "Investigator", "Sniper", "Ranger",
            "Combat Awareness"
        ]
    },
    "Tech": {
        "description": "Understanding, using, and repairing technology.",
        "attribute": "INT",
        "specialties": [
            "Mechanic", "Gunsmith", "Electrician", "Blacksmith", "Builder", "Communications",
            "NBC", "Computers", "Improvised Munitions", "Scientist"
        ]
    },
    "Medical Aid": {
        "description": "Providing medical care and treatment.",
        "attribute": "INT",
        "specialties": [
            "Combat Medic", "Field Surgeon", "General Practitioner", "Veterinarian",
            "Scientist", "Counselor"
        ]
    },
    "Command": {
        "description": "Leading others effectively, especially in combat situations.",
        "attribute": "EMP",
        "specialties": [
            "Frontline Leader", "Tactician", "Quartermaster", "Logistician", "Psy Ops",
            "Teacher"
        ]
    },
    "Persuasion": {
        "description": "Convincing others through charm, deception, or intimidation.",
        "attribute": "EMP",
        "specialties": [
            "Interrogator", "Trader", "Linguist", "Psy Ops", "Historian", "Musician",
            "Communications", "Counselor", "Teacher"
        ]
    }
}

# Skill levels and their corresponding dice
SKILL_LEVELS = {
    "A": {"die": "D12", "description": "Elite"},
    "B": {"die": "D10", "description": "Veteran"},
    "C": {"die": "D8", "description": "Experienced"},
    "D": {"die": "D6", "description": "Novice"},
    "F": {"die": "None", "description": "Untrained"}
}

# Specialties descriptions
SPECIALTIES = {
    # Close Combat Specialties
    "Brawler": "Skilled in unarmed combat and street fighting.",
    "Melee": "Proficient with melee weapons like knives, clubs, and improvised weapons.",
    "Martial Artist": "Formally trained in martial arts techniques.",
    "Killer": "Specialized in efficient, lethal techniques.",

    # Movement Specialties
    "Runner": "Fast and agile, skilled at parkour and urban movement.",
    "Infiltrator": "Expert at stealthy movement and infiltration.",
    "Biker": "Skilled motorcycle rider and mechanic.",
    "Racer": "Expert at high-speed vehicle operation.",
    "Boatman": "Skilled in watercraft operation and navigation.",
    "Rider": "Expert in riding and caring for animals.",
    "Pilot": "Trained in aircraft operation.",
    "Navigator": "Skilled in finding routes and reading maps.",
    "Tanker": "Expert at operating heavy vehicles.",

    # Ranged Combat Specialties
    "Rifleman": "Proficient with rifles and combat tactics.",
    "Sniper": "Expert in long-range precision shooting.",
    "Ranger": "Combines shooting skills with wilderness survival.",
    "Sidearms": "Specializes in handguns and close-quarters combat.",
    "Machinegunner": "Expert with machine guns and suppressive fire.",
    "Launcher Crew": "Trained in rocket and grenade launchers.",

    # Technical Specialties
    "Combat Engineer": "Skilled in demolitions, fortifications, and obstacle clearing.",
    "Mechanic": "Expert in vehicle repair and maintenance.",
    "Gunsmith": "Specializes in weapon repair and modification.",
    "Electrician": "Skilled with electrical systems and electronics.",
    "Blacksmith": "Expert in metalworking and improvised repairs.",
    "Builder": "Skilled in construction and structural repairs.",
    "Communications": "Expert in radio and communications equipment.",
    "NBC": "Trained in Nuclear, Biological, and Chemical defense.",
    "Computers": "Skilled with computer systems and software.",
    "Improvised Munitions": "Creates weapons and explosives from available materials.",

    # Intelligence Specialties
    "Intelligence": "Trained in gathering and analyzing information.",
    "Scout": "Expert in reconnaissance and observation.",
    "Investigator": "Skilled at solving crimes and gathering evidence.",
    "Combat Awareness": "Enhanced situational awareness in combat.",

    # Survival Specialties
    "Hunter": "Skilled at tracking and hunting game.",
    "Farmer": "Expert in agriculture and animal husbandry.",
    "Forager": "Finds edible plants and useful resources.",
    "Fisher": "Skilled at fishing and aquatic resource gathering.",
    "Cook": "Prepares nutritious meals from available ingredients.",
    "Quartermaster": "Manages and allocates supplies efficiently.",
    "SERE Training": "Survival, Evasion, Resistance, and Escape specialist.",
    "Load Carrier": "Skilled at carrying heavy loads efficiently.",
    "Mountaineer": "Expert in mountain and climbing techniques.",

    # Medical Specialties
    "Combat Medic": "Provides emergency medical care under fire.",
    "Field Surgeon": "Performs surgical procedures in field conditions.",
    "General Practitioner": "Broad medical knowledge for diagnosis and treatment.",
    "Veterinarian": "Specialized in animal medicine.",

    # Command Specialties
    "Frontline Leader": "Effective at leading troops in combat.",
    "Tactician": "Expert in planning and executing military operations.",
    "Logistician": "Skilled at managing supply lines and resources.",

    # Social Specialties
    "Interrogator": "Expert at extracting information from subjects.",
    "Trader": "Skilled at bartering and evaluating goods.",
    "Linguist": "Proficient in multiple languages.",
    "Psy Ops": "Psychological operations specialist.",
    "Historian": "Expert knowledge of historical events and contexts.",
    "Musician": "Skilled performer who can boost morale.",
    "Counselor": "Provides mental health support and guidance.",
    "Teacher": "Effectively instructs others in skills and knowledge.",

    # Military-Specific Specialties
    "Redleg": "Artillery specialist trained in fire support.",
    "Tanker": "Armored vehicle crew trained in tank operations.",
    "Paratrooper": "Airborne insertion specialist.",
    "Scientist": "Conducts research and experiments in specialized fields.",
    "Scrounger": "Expert at finding useful items in ruins and wasteland.",
    "Locksmith": "Skilled at bypassing locks and security systems."
}

# Skill relationships - which skills often work together
SKILL_RELATIONSHIPS = {
    "Close Combat": ["Mobility", "Stamina"],
    "Heavy Weapons": ["Ranged Combat", "Tech"],
    "Mobility": ["Close Combat", "Survival"],
    "Ranged Combat": ["Recon", "Heavy Weapons"],
    "Stamina": ["Close Combat", "Survival"],
    "Survival": ["Recon", "Mobility"],
    "Recon": ["Ranged Combat", "Survival"],
    "Tech": ["Medical Aid", "Heavy Weapons"],
    "Medical Aid": ["Tech", "Persuasion"],
    "Command": ["Persuasion", "Recon"],
    "Persuasion": ["Command", "Medical Aid"]
}

# Skill upgrade paths - how skills typically develop
SKILL_UPGRADE_PATHS = {
    "Close Combat": {
        "common_upgrades": ["Stamina", "Mobility"],
        "specialty_paths": {
            "Brawler": ["Killer", "Martial Artist"],
            "Melee": ["Killer", "Martial Artist"],
            "Martial Artist": ["Killer", "Brawler"]
        }
    },
    "Ranged Combat": {
        "common_upgrades": ["Heavy Weapons", "Recon"],
        "specialty_paths": {
            "Rifleman": ["Sniper", "Machinegunner"],
            "Sidearms": ["Rifleman", "Scout"],
            "Sniper": ["Scout", "Combat Awareness"]
        }
    },
    "Medical Aid": {
        "common_upgrades": ["Tech", "Persuasion"],
        "specialty_paths": {
            "Combat Medic": ["Field Surgeon", "General Practitioner"],
            "Field Surgeon": ["General Practitioner", "Veterinarian"],
            "General Practitioner": ["Counselor", "Scientist"]
        }
    }
}


def get_all_skills():
    """Get a list of all skills

    Returns:
        Dictionary of all skills and their information
    """
    return CORE_SKILLS


def get_skill_info(skill_name):
    """Get information about a specific skill

    Args:
        skill_name: Name of the skill

    Returns:
        Dictionary with skill information or None if not found
    """
    return CORE_SKILLS.get(skill_name, None)


def get_skill_specialties(skill_name):
    """Get specialties for a specific skill

    Args:
        skill_name: Name of the skill

    Returns:
        List of specialties for the skill or empty list if skill not found
    """
    skill_info = get_skill_info(skill_name)
    if not skill_info:
        return []

    return skill_info.get("specialties", [])


def get_specialty_info(specialty_name):
    """Get information about a specific specialty

    Args:
        specialty_name: Name of the specialty

    Returns:
        Description of the specialty or None if not found
    """
    return SPECIALTIES.get(specialty_name, None)


def get_specialty_parent_skills(specialty_name):
    """Get the skills that a specialty belongs to

    Args:
        specialty_name: Name of the specialty

    Returns:
        List of skill names that include this specialty
    """
    parent_skills = []

    for skill_name, skill_info in CORE_SKILLS.items():
        if specialty_name in skill_info.get("specialties", []):
            parent_skills.append(skill_name)

    return parent_skills


def get_skill_die(skill_level):
    """Get the die type for a skill level

    Args:
        skill_level: Skill level (A, B, C, D, or F)

    Returns:
        Die type (D12, D10, D8, D6, or None)
    """
    level_info = SKILL_LEVELS.get(skill_level, None)
    if not level_info:
        return "None"

    return level_info.get("die", "None")


def get_skill_level_description(skill_level):
    """Get the description for a skill level

    Args:
        skill_level: Skill level (A, B, C, D, or F)

    Returns:
        Description of the skill level
    """
    level_info = SKILL_LEVELS.get(skill_level, None)
    if not level_info:
        return "Unknown"

    return level_info.get("description", "Unknown")


def get_attribute_for_skill(skill_name):
    """Get the attribute used for a skill

    Args:
        skill_name: Name of the skill

    Returns:
        Attribute name (STR, AGL, INT, or EMP) or None if skill not found
    """
    skill_info = get_skill_info(skill_name)
    if not skill_info:
        return None

    return skill_info.get("attribute", None)


def calculate_skill_check_dice(character, skill_name):
    """Calculate the dice used for a skill check

    Args:
        character: Character object
        skill_name: Name of the skill

    Returns:
        Tuple of (attribute_die, skill_die, attribute_name)
    """
    # Get the attribute used for the skill
    skill_info = get_skill_info(skill_name)
    if not skill_info:
        return ("None", "None", None)

    attribute_name = skill_info.get("attribute", "STR")

    # Get the attribute die
    attribute_letter = character.get_attribute_letter(attribute_name)
    attribute_die = "D12" if attribute_letter == "A" else "D10" if attribute_letter == "B" else "D8" if attribute_letter == "C" else "D6"

    # Get the skill die
    skill_level = character.skills.get(skill_name, "F")
    skill_die = get_skill_die(skill_level)

    return (attribute_die, skill_die, attribute_name)


def get_related_skills(skill_name):
    """Get skills that are related to a specific skill

    Args:
        skill_name: Name of the skill

    Returns:
        List of related skill names
    """
    return SKILL_RELATIONSHIPS.get(skill_name, [])


def get_upgrade_path(skill_name, specialty=None):
    """Get the upgrade path for a skill and optionally a specialty

    Args:
        skill_name: Name of the skill
        specialty: Optional specialty name

    Returns:
        Dictionary with upgrade information
    """
    upgrade_info = SKILL_UPGRADE_PATHS.get(skill_name, {})

    if specialty and "specialty_paths" in upgrade_info:
        specialty_path = upgrade_info["specialty_paths"].get(specialty, [])
        if specialty_path:
            return {"specialty_upgrades": specialty_path}

    return {"common_upgrades": upgrade_info.get("common_upgrades", [])}


def get_skill_combinations(skill1, skill2):
    """Get benefits of combining two skills

    Args:
        skill1: First skill name
        skill2: Second skill name

    Returns:
        Description of the combination benefits or None if no specific combination
    """
    # This would be implemented with actual skill combination data
    # For now, just check if they're related
    if skill2 in get_related_skills(skill1):
        return f"{skill1} and {skill2} work well together and can provide mutual benefits."

    return None


def get_all_specialties():
    """Get all specialties

    Returns:
        Dictionary of all specialties and their descriptions
    """
    return SPECIALTIES