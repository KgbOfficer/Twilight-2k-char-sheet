"""
careers.py - Career data for Twilight 2000 character creation
"""

# Military careers
MILITARY_CAREERS = {
    "Combat Arms": {
        "description": "The core combat units of military forces, primarily focused on direct engagement with enemy forces.",
        "requirements": {"attributes": {"STR": "B+", "AGL": "B+"}, "special": None},
        "starting_rank": "Private",
        "skills": ["Close Combat", "Heavy Weapons", "Ranged Combat", "Recon"],
        "specialties": {
            "Rifleman": "Standard infantry soldier trained in basic tactics and firearms.",
            "Redleg": "Artillery specialist trained to provide fire support.",
            "Tanker": "Armored vehicle crewman trained to operate tanks and other armored vehicles.",
            "Machinegunner": "Specialist in machine gun operations and tactics.",
            "Launcher Crew": "Specialist in anti-tank or anti-aircraft launchers.",
            "Combat Engineer": "Trained in demolitions, obstacle clearing, and battlefield construction."
        },
        "starting_gear": [
            "Assault rifle",
            "LMG or ATRL",
            "D6 reloads",
            "Flak jacket and helmet",
            "Knife or D6 hand grenades",
            "Personal medkit",
            "Backpack"
        ]
    },
    "Combat Support": {
        "description": "Units that provide direct support to combat arms units by providing intelligence, communications, and other specialized functions.",
        "requirements": {"attributes": {"INT": "B+"}, "special": None},
        "starting_rank": "PFC",
        "skills": ["Recon", "Survival", "Tech"],
        "specialties": {
            "Intelligence": "Trained to gather and analyze intelligence data.",
            "Linguist": "Specialist in languages, trained for translation and interrogation.",
            "Communications": "Expert in military communications systems.",
            "NBC": "Trained in Nuclear, Biological, and Chemical defense.",
            "Computers": "Specialist in military computer systems.",
            "Psy Ops": "Psychological operations specialist."
        },
        "starting_gear": [
            "Assault rifle",
            "D6 reloads",
            "Flak jacket and helmet",
            "Knife or D6 hand grenades",
            "MOPP suit or manpack radio",
            "Personal medkit",
            "Backpack"
        ]
    },
    "Combat Service Support": {
        "description": "Units that provide logistics, maintenance, and medical support to combat units.",
        "requirements": {"attributes": {}, "special": None},
        "starting_rank": "PFC",
        "skills": ["Medical Aid", "Tech"],
        "specialties": {
            "Mechanic": "Specialist in vehicle maintenance and repair.",
            "Gunsmith": "Expert in weapon maintenance and repair.",
            "Electrician": "Trained in electrical systems maintenance.",
            "Combat Medic": "Medical specialist trained to provide care under fire.",
            "Field Surgeon": "Advanced medical specialist capable of surgery.",
            "Vehicle Tools": "Expert in specialized vehicle maintenance."
        },
        "starting_gear": [
            "Assault rifle",
            "D6 reloads",
            "Flak jacket and helmet",
            "Knife or D6 hand grenades",
            "Personal medkit",
            "Basic tools or weapon tools or surgical instruments",
            "Backpack"
        ]
    },
    "Special Operations": {
        "description": "Elite units trained for specialized missions, often operating behind enemy lines or in hostile territory.",
        "requirements": {"attributes": {"STR": "B+", "AGL": "B+", "INT": "C+"},
                         "special": "At least one term in Combat Arms"},
        "starting_rank": "Sergeant",
        "skills": ["Close Combat", "Ranged Combat", "Recon", "Survival"],
        "specialties": {
            "Paratrooper": "Airborne insertion specialist.",
            "Ranger": "Elite light infantry trained for special operations.",
            "Infiltrator": "Specialist in covert insertion and operations.",
            "Combat Awareness": "Trained in advanced situational awareness.",
            "Sniper": "Long-range precision shooting specialist.",
            "SERE Training": "Survival, Evasion, Resistance, and Escape specialist."
        },
        "starting_gear": [
            "Assault rifle or sniper rifle",
            "Any pistol or D6 hand grenades or rifle-mounted grenade launcher",
            "D6 reloads for each weapon",
            "Binoculars or night vision goggles",
            "Flak jacket and helmet",
            "Knife",
            "Personal medkit",
            "Backpack"
        ]
    },
    "Officer": {
        "description": "Command personnel responsible for leading military units.",
        "requirements": {"attributes": {"INT": "B+"}, "special": "No D attributes, at least one term in Education"},
        "starting_rank": "2nd Lieutenant",
        "skills": ["Ranged Combat", "Command", "Persuasion"],
        "specialties": {
            "Sidearms": "Specialist in pistol use and tactics.",
            "Intelligence": "Trained in intelligence gathering and analysis.",
            "Tactician": "Expert in military tactics and planning.",
            "Logistician": "Specialist in military logistics and supply.",
            "Frontline Leader": "Skilled in leading troops in combat.",
            "Quartermaster": "Expert in managing military supplies and equipment."
        },
        "starting_gear": [
            "Pistol or submachine gun",
            "D6 reloads",
            "Manpack radio or night vision goggles",
            "Flak jacket",
            "Knife or D6 hand grenades",
            "Personal medkit"
        ]
    }
}

# Police careers
POLICE_CAREERS = {
    "Police Officer": {
        "description": "Standard law enforcement officer, trained to maintain public order and enforce laws.",
        "requirements": {"attributes": {}, "special": "No D attribute"},
        "skills": ["Close Combat", "Ranged Combat"],
        "specialties": {
            "Sidearms": "Specialist in handgun use and tactics.",
            "Melee": "Trained in close quarters combat and non-lethal takedowns.",
            "Runner": "Pursuit specialist, trained in foot chases and parkour.",
            "Racer": "Vehicle pursuit specialist, skilled in high-speed driving.",
            "Biker": "Motorcycle patrol officer.",
            "Scout": "Skilled in observation and surveillance."
        },
        "starting_gear": [
            "Pistol",
            "D6 reloads",
            "Handcuffs",
            "Baton (club)",
            "Patrol car with half a tank of gasoline"
        ]
    },
    "Detective": {
        "description": "Investigative officer specialized in solving crimes and gathering evidence.",
        "requirements": {"attributes": {"EMP": "B+"}, "special": "At least one term as Police Officer"},
        "skills": ["Ranged Combat", "Recon", "Persuasion"],
        "specialties": {
            "Infiltrator": "Undercover operations specialist.",
            "Interrogator": "Expert in questioning suspects and witnesses.",
            "Intelligence": "Skilled in gathering and analyzing criminal intelligence.",
            "Investigator": "Specialist in crime scene investigation.",
            "Locksmith": "Expert in bypassing locks and security systems.",
            "Linguist": "Skilled in multiple languages for diverse community policing."
        },
        "starting_gear": [
            "Pistol",
            "D6 reloads",
            "Lockpicks"
        ]
    },
    "SWAT": {
        "description": "Special Weapons and Tactics, elite police units trained for high-risk operations.",
        "requirements": {"attributes": {"STR": "B+", "AGL": "B+"}, "special": "At least one term as Police Officer"},
        "skills": ["Close Combat", "Ranged Combat", "Recon"],
        "specialties": {
            "Martial Artist": "Hand-to-hand combat specialist.",
            "Rifleman": "Precision shooter trained for tactical operations.",
            "Sniper": "Long-range precision shooting specialist.",
            "Combat Awareness": "Tactical situation awareness expert.",
            "Infiltrator": "Specialized in covert entry and operations.",
            "Scout": "Reconnaissance and surveillance specialist."
        },
        "starting_gear": [
            "Assault rifle or submachine gun",
            "D6 reloads",
            "Night vision goggles",
            "Flak jacket and helmet",
            "Knife",
            "Personal medkit"
        ]
    }
}

# Crime careers
CRIME_CAREERS = {
    "Gang Member": {
        "description": "Member of an organized criminal group, typically involved in street-level crime.",
        "requirements": {"attributes": {"STR": "C+", "AGL": "C+"}, "special": None},
        "skills": ["Close Combat", "Ranged Combat"],
        "specialties": {
            "Brawler": "Street fighting specialist.",
            "Melee": "Skilled in using knives and improvised weapons.",
            "Killer": "Specializes in violent crimes and intimidation.",
            "Martial Artist": "Trained in formal combat techniques.",
            "Rifleman": "Skilled with firearms and ranged combat.",
            "Sidearms": "Handgun specialist."
        },
        "starting_gear": [
            "Any civilian firearm",
            "D6 reloads",
            "Knife"
        ]
    },
    "Burglar": {
        "description": "Specialist in breaking and entering, typically for theft.",
        "requirements": {"attributes": {"AGL": "C+", "INT": "C+"}, "special": None},
        "skills": ["Recon"],
        "specialties": {
            "Brawler": "Can handle themselves in a fight if caught.",
            "Sidearms": "Prefers pistols for their concealability.",
            "Mountaineer": "Skilled in scaling buildings and obstacles.",
            "Infiltrator": "Expert in stealthy entry.",
            "Electrician": "Specializes in bypassing electronic security.",
            "Locksmith": "Expert in defeating locks and security systems."
        },
        "starting_gear": [
            "Pistol or revolver",
            "D6 reloads",
            "Lockpick set (TECH +2)"
        ]
    },
    "Hustler": {
        "description": "Con artist or scammer who makes a living through deception and fraud.",
        "requirements": {"attributes": {"INT": "C+", "EMP": "C+"}, "special": None},
        "skills": ["Recon", "Persuasion"],
        "specialties": {
            "Sidearms": "Keeps a concealed weapon for protection.",
            "Infiltrator": "Good at assuming false identities.",
            "Scout": "Skilled at spotting marks and opportunities.",
            "Interrogator": "Expert in extracting information through manipulation.",
            "Psy Ops": "Uses psychological tactics to influence victims.",
            "Trader": "Skilled in scamming through fake business deals."
        },
        "starting_gear": [
            "Pistol or revolver",
            "D6 reloads"
        ]
    },
    "Prisoner": {
        "description": "Character who has spent time incarcerated, learning to survive in prison.",
        "requirements": {"attributes": {}, "special": "After a term in a career of crime, if war does not break out"},
        "skills": ["Close Combat"],
        "specialties": {
            "Brawler": "Necessary for survival in prison.",
            "Melee": "Skilled with improvised weapons.",
            "Killer": "Has had to kill to survive.",
            "Ranger": "Good at avoiding trouble and guards.",
            "SERE Training": "Survival under harsh conditions.",
            "Scrounger": "Expert at finding or making useful items from limited resources."
        },
        "starting_gear": [
            "Any civilian firearm",
            "D6 reloads",
            "Knife"
        ]
    }
}

# Intelligence careers
INTELLIGENCE_CAREERS = {
    "Agent": {
        "description": "Intelligence operative gathering information and conducting covert operations.",
        "requirements": {"attributes": {"INT": "B+"}, "special": "At least one term in Education"},
        "skills": ["Ranged Combat", "Recon", "Persuasion"],
        "specialties": {
            "Intelligence": "Core skill of information gathering and analysis.",
            "Locksmith": "Expert in bypassing security systems.",
            "Investigator": "Skilled in detailed investigation and analysis.",
            "Scout": "Surveillance and observation specialist.",
            "Psy Ops": "Psychological operations and manipulation expert.",
            "Sidearms": "Trained in discreet weaponry."
        },
        "starting_gear": [
            "Pistol",
            "D6 reloads",
            "Lockpick set",
            "Knife or explosives",
            "Personal medkit"
        ]
    },
    "Assassin": {
        "description": "Specialized operative trained to eliminate high-value targets.",
        "requirements": {"attributes": {"EMP": "C", "AGL": "B+"}, "special": "One or more terms as an Agent"},
        "skills": ["Close Combat", "Ranged Combat"],
        "specialties": {
            "Killer": "Trained specifically in lethal techniques.",
            "Interrogator": "Information extraction specialist.",
            "Sniper": "Long-range elimination expert.",
            "Martial Artist": "Hand-to-hand combat specialist.",
            "Improvised Munitions": "Expert in creating weapons from available materials.",
            "Infiltrator": "Covert operations specialist."
        },
        "starting_gear": [
            "Sniper rifle or submachine gun (suppressed)",
            "D6 reloads",
            "Radio or binoculars",
            "Knife or explosives",
            "Personal medkit"
        ]
    },
    "Paramilitary": {
        "description": "Operatives working for intelligence agencies in direct combat roles.",
        "requirements": {"attributes": {"STR": "B+", "AGL": "B+"}, "special": "One or more terms in the military"},
        "skills": ["Heavy Weapons", "Ranged Combat", "Survival"],
        "specialties": {
            "Brawler": "Direct combat specialist.",
            "Rifleman": "Firearms expert.",
            "Machinegunner": "Heavy weapons specialist.",
            "Combat Engineer": "Demolitions and fortification expert.",
            "Improvised Munitions": "Creates weapons from available materials.",
            "Tactician": "Combat tactics and planning specialist."
        },
        "starting_gear": [
            "Assault rifle, LMG or ATRL",
            "D6 reloads",
            "Knife or D6 hand grenades",
            "Personal medkit"
        ]
    }
}

# Blue Collar careers
BLUE_COLLAR_CAREERS = {
    "Driver": {
        "description": "Professional vehicle operator, from taxis to heavy trucks.",
        "requirements": {"attributes": {"AGL": "B+"}, "special": None},
        "skills": ["Tech"],
        "specialties": {
            "Biker": "Motorcycle specialist.",
            "Boatman": "Watercraft operator.",
            "Navigator": "Expert in finding routes and reading maps.",
            "Pilot": "Aircraft operator.",
            "Racer": "High-speed driving specialist.",
            "Tanker": "Heavy vehicle specialist."
        },
        "starting_gear": [
            "Any civilian firearm",
            "D3 reloads",
            "Any civilian car or truck",
            "Vehicle tools"
        ]
    },
    "Farmer": {
        "description": "Agricultural worker producing food and managing land.",
        "requirements": {"attributes": {}, "special": None},
        "skills": ["Survival"],
        "specialties": {
            "Cook": "Food preparation specialist.",
            "Farmer": "Agricultural expert.",
            "Fisher": "Fishing and aquaculture specialist.",
            "Hunter": "Game hunting expert.",
            "Forager": "Skilled at finding edible plants and resources.",
            "Rider": "Animal husbandry and riding expert."
        },
        "starting_gear": [
            "Any civilian firearm",
            "D3 reloads",
            "Pickup truck",
            "Basic toolkit",
            "2D6 rations of food"
        ]
    },
    "Mechanic": {
        "description": "Technical specialist in maintaining and repairing machinery.",
        "requirements": {"attributes": {}, "special": None},
        "skills": ["Tech"],
        "specialties": {
            "Blacksmith": "Metal working specialist.",
            "Gunsmith": "Firearms maintenance expert.",
            "Locksmith": "Security systems specialist.",
            "Mechanic": "General mechanical repair expert.",
            "Scrounger": "Salvage and improvisation specialist.",
            "Improvised Munitions": "Creates weapons from available materials."
        },
        "starting_gear": [
            "Any civilian firearm",
            "D3 reloads",
            "Pickup truck",
            "Basic tools",
            "Vehicle tools or weapon tools"
        ]
    },
    "Construction": {
        "description": "Builder involved in creating or maintaining structures.",
        "requirements": {"attributes": {"STR": "B+"}, "special": None},
        "skills": ["Close Combat", "Tech"],
        "specialties": {
            "Brawler": "Physical labor specialist.",
            "Builder": "Construction expert.",
            "Load Carrier": "Heavy lifting specialist.",
            "Blacksmith": "Metal construction specialist.",
            "Electrician": "Electrical systems expert.",
            "Improvised Munitions": "Demolitions knowledge."
        },
        "starting_gear": [
            "Any civilian firearm",
            "D3 reloads",
            "Crowbar",
            "Pickup truck",
            "Basic tools"
        ]
    }
}

# Education careers
EDUCATION_CAREERS = {
    "Liberal Arts": {
        "description": "Education focused on humanities, social sciences, and creative fields.",
        "requirements": {"attributes": {"INT": "C+", "EMP": "C+"}, "special": None},
        "skills": ["Persuasion"],
        "specialties": {
            "Historian": "History specialist.",
            "Cook": "Culinary arts expert.",
            "Linguist": "Language and communication specialist.",
            "Musician": "Performing arts specialist.",
            "Psy Ops": "Psychology specialist.",
            "Counselor": "Mental health specialist."
        },
        "starting_gear": [
            "Any civilian firearm",
            "D3 reloads",
            "Dictionary in any language",
            "Bicycle"
        ]
    },
    "Sciences": {
        "description": "Education focused on natural sciences, mathematics, and technical fields.",
        "requirements": {"attributes": {"INT": "B+"}, "special": None},
        "skills": ["Tech"],
        "specialties": {
            "Chemist": "Chemical sciences specialist.",
            "Communication": "Information technology specialist.",
            "Computers": "Computer science specialist.",
            "Electrician": "Electrical engineering specialist.",
            "Scientist": "Research and development specialist.",
            "Linguist": "Computational linguistics specialist."
        },
        "starting_gear": [
            "Any civilian firearm",
            "D3 reloads",
            "Bicycle or 2WD car with half a tank of gasoline"
        ]
    }
}

# White Collar careers
WHITE_COLLAR_CAREERS = {
    "Doctor": {
        "description": "Medical professional specializing in diagnosis and treatment.",
        "requirements": {"attributes": {"EMP": "B+"}, "special": "Two terms in Education (Sciences)"},
        "skills": ["Medical Aid", "Persuasion"],
        "specialties": {
            "Linguist": "Medical terminology in multiple languages.",
            "Combat Medic": "Emergency medicine specialist.",
            "Counselor": "Mental health specialist.",
            "Field Surgeon": "Surgical specialist.",
            "General Practitioner": "Primary care physician.",
            "Veterinarian": "Animal medicine specialist."
        },
        "starting_gear": [
            "Any civilian firearm",
            "D3 reloads",
            "D6 personal medkits",
            "Pain relievers",
            "Surgical instruments"
        ]
    },
    "Professor": {
        "description": "Academic specialist teaching and researching in higher education.",
        "requirements": {"attributes": {"INT": "B+"}, "special": "Two terms in Education (Liberal Arts)"},
        "skills": ["Persuasion"],
        "specialties": {
            "Historian": "History specialist.",
            "Chemist": "Chemistry specialist.",
            "Scientist": "General sciences specialist.",
            "Linguist": "Languages specialist.",
            "Psy Ops": "Psychology specialist.",
            "Teacher": "Education specialist."
        },
        "starting_gear": [
            "Any civilian firearm",
            "D3 reloads",
            "2WD car with half a tank of gasoline"
        ]
    },
    "Manager": {
        "description": "Professional leader in business or administration.",
        "requirements": {"attributes": {"EMP": "B+"}, "special": "One term in Education (any)"},
        "skills": ["Tech", "Command", "Persuasion"],
        "specialties": {
            "Quartermaster": "Resource management specialist.",
            "Computers": "Information systems specialist.",
            "Frontline Leader": "Team leadership specialist.",
            "Logistician": "Supply chain specialist.",
            "Teacher": "Training and development specialist.",
            "Counselor": "Human resources specialist."
        },
        "starting_gear": [
            "Any civilian firearm",
            "D3 reloads",
            "Pocket calculator",
            "2WD car with half a tank of gasoline"
        ]
    }
}

# Local Militia (At War career)
LOCAL_MILITIA = {
    "description": "Civilian defenders fighting to protect their homes and communities during the war.",
    "requirements": {"attributes": {}, "special": "Automatically get the benefits of the At War career term."},
    "skills": ["Varies based on background"],
    "specialties": ["Varies based on background"],
    "bonuses": ["Know the local area", "Have multiple local contacts", "Speak the local language fluently"],
    "starting_gear": ["Varies based on background"]
}

# All careers combined
ALL_CAREERS = {
    "Military": MILITARY_CAREERS,
    "Police": POLICE_CAREERS,
    "Crime": CRIME_CAREERS,
    "Intelligence": INTELLIGENCE_CAREERS,
    "Blue Collar": BLUE_COLLAR_CAREERS,
    "Education": EDUCATION_CAREERS,
    "White Collar": WHITE_COLLAR_CAREERS,
    "Local Militia": LOCAL_MILITIA
}

# At War career bonuses
AT_WAR_BONUSES = {
    "description": "Special benefits for characters during the war term.",
    "skill_increase": "Increase any two skills by one step each.",
    "coolness_under_fire": "Chance to improve Coolness Under Fire rating.",
    "specialties": "Gain a final new specialty based on war experience."
}


def get_career_categories():
    """Get a list of all career categories

    Returns:
        List of career category names
    """
    return list(ALL_CAREERS.keys())


def get_careers_in_category(category):
    """Get all careers in a category

    Args:
        category: Career category name

    Returns:
        Dictionary of careers in the category
    """
    return ALL_CAREERS.get(category, {})


def get_career(category, career_name):
    """Get a specific career

    Args:
        category: Career category name
        career_name: Name of the career

    Returns:
        Career data dictionary or None if not found
    """
    category_careers = ALL_CAREERS.get(category, {})
    return category_careers.get(career_name, None)


def check_career_requirements(character, category, career_name):
    """Check if a character meets the requirements for a career

    Args:
        character: Character object
        category: Career category name
        career_name: Name of the career

    Returns:
        True if requirements are met, False otherwise
    """
    career = get_career(category, career_name)
    if not career:
        return False

    # Check attribute requirements
    for attr, req in career.get("requirements", {}).get("attributes", {}).items():
        if req.endswith("+"):
            # Requirement is minimum level (e.g., "B+")
            min_level = req[0]
            char_level = character.get_attribute_letter(attr)

            # Check if character's level is at least the minimum
            if ord(char_level) > ord(min_level):
                return False
        else:
            # Requirement is exact level
            if character.get_attribute_letter(attr) != req:
                return False

    # Check special requirements
    special_req = career.get("requirements", {}).get("special", None)
    if special_req:
        # This would need custom logic based on the requirement
        # For example: "At least one term in Combat Arms"
        # For now, assume special requirements are not met
        return False

    return True


def get_starting_gear(character, category, career_name):
    """Get starting gear for a career

    Args:
        character: Character object
        category: Career category name
        career_name: Name of the career

    Returns:
        List of starting gear items
    """
    career = get_career(category, career_name)
    if not career:
        return []

    return career.get("starting_gear", [])


def get_at_war_benefits():
    """Get benefits for the At War career term

    Returns:
        Dictionary of At War benefits
    """
    return AT_WAR_BONUSES