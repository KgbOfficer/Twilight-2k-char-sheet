"""
config.py - Configuration settings for the Twilight 2000 Character Creator
"""

# Application Settings
APP_NAME = "Twilight 2000 Character Creator"
APP_VERSION = "1.0.0"
DEBUG_MODE = True

# UI Settings
DEFAULT_WINDOW_WIDTH = 1024
DEFAULT_WINDOW_HEIGHT = 768
DEFAULT_FONT = "Arial"
MILITARY_FONT = "assets/fonts/military_font.ttf"  # Replace with actual font file
TEXT_SCROLL_SPEED = 30  # ms per character

# Theme Settings
THEMES = {
    "default": {
        "name": "Default",
        "primary_bg": "#2E2E2E",  # Dark grey
        "secondary_bg": "#3C3C3C",
        "accent": "#505050",
        "text": "#E0E0E0",
        "highlight": "#6C6C6C",
        "button_bg": "#404040",
        "button_text": "#FFFFFF",
        "border": "#505050",
    },
    "military": {
        "name": "Military Green",
        "primary_bg": "#2F3625",  # Dark olive
        "secondary_bg": "#3A4331",
        "accent": "#4F5745",
        "text": "#E0E0D0",
        "highlight": "#6B7356",
        "button_bg": "#4D5445",
        "button_text": "#FFFFFF",
        "border": "#616B53",
    },
    "soviet": {
        "name": "Soviet Red",
        "primary_bg": "#3B2B2B",  # Dark red/brown
        "secondary_bg": "#4A2F2F",
        "accent": "#5F3A3A",
        "text": "#E0D0D0",
        "highlight": "#7C4242",
        "button_bg": "#5D3939",
        "button_text": "#FFFFFF",
        "border": "#6E4444",
    }
}
DEFAULT_THEME = "default"

# Audio Settings
MASTER_VOLUME = 0.7
MUSIC_VOLUME = 0.5
SFX_VOLUME = 0.8
ENABLE_MUSIC = True
ENABLE_SFX = True

AUDIO_FILES = {
    "intro_music": "assets/music/main_theme.mp3",
    "military_theme": "assets/music/military_theme.mp3",
    "soviet_theme": "assets/music/soviet_theme.mp3",
    "button_click": "assets/sounds/button_click.wav",
    "dice_roll": "assets/sounds/dice_roll.wav",
}

# Game Data Settings
DATA_VERSION = "1.0"
DICE_ANIMATION_SPEED = 50  # ms between dice roll frames

# Character Creation Settings
STARTING_AGE = 18