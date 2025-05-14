"""
fonts_setup.py - Create necessary font directory structure
"""

import os
import sys
import shutil
from pathlib import Path


def ensure_font_directory():
    """Ensure the font directory exists and contains a placeholder"""
    # Create the font directory if it doesn't exist
    font_dir = Path("assets/fonts")
    font_dir.mkdir(parents=True, exist_ok=True)

    # Check if the military font exists
    military_font_path = font_dir / "military_font.ttf"

    if not military_font_path.exists():
        # If not, we'll try to copy a system font as a placeholder
        system_fonts = find_system_fonts()

        if system_fonts:
            # Use the first available system font
            print(f"Copying system font {system_fonts[0]} as placeholder")
            shutil.copy(system_fonts[0], military_font_path)
            print(f"Created placeholder font at {military_font_path}")
            return True
        else:
            print("Could not find any system fonts to use as placeholder")

            # Create an empty placeholder file to prevent load errors
            with open(military_font_path, "wb") as f:
                # Write minimal TTF header to create a simple placeholder
                f.write(b"\x00\x01\x00\x00\x00\x0C\x00\x00\x00\x00\x00\x00\x00\x00")

            print(f"Created empty placeholder font at {military_font_path}")
            return False

    print(f"Military font already exists at {military_font_path}")
    return True


def find_system_fonts():
    """Find system fonts that could be used as placeholders"""
    system_fonts = []

    if sys.platform.startswith('win'):
        # Windows font paths
        font_dirs = [
            os.path.join(os.environ['WINDIR'], 'Fonts'),
            os.path.join(os.environ['LOCALAPPDATA'], 'Microsoft', 'Windows', 'Fonts')
        ]

        # Look for common monospace fonts that might be suitable
        target_fonts = [
            'consola.ttf',  # Consolas
            'cour.ttf',  # Courier New
            'lucon.ttf',  # Lucida Console
            'arial.ttf'  # Arial (fallback)
        ]

        for font_dir in font_dirs:
            if os.path.exists(font_dir):
                for font in target_fonts:
                    font_path = os.path.join(font_dir, font)
                    if os.path.exists(font_path):
                        system_fonts.append(font_path)

    elif sys.platform.startswith('darwin'):
        # macOS font paths
        font_dirs = [
            '/System/Library/Fonts',
            '/Library/Fonts',
            os.path.expanduser('~/Library/Fonts')
        ]

        # Look for common monospace fonts
        target_fonts = [
            'Menlo.ttc',
            'Monaco.ttf',
            'CourierNew.ttf',
            'Arial.ttf'
        ]

        for font_dir in font_dirs:
            if os.path.exists(font_dir):
                for font in target_fonts:
                    font_path = os.path.join(font_dir, font)
                    if os.path.exists(font_path):
                        system_fonts.append(font_path)

    else:
        # Linux font paths
        font_dirs = [
            '/usr/share/fonts',
            '/usr/local/share/fonts',
            os.path.expanduser('~/.fonts')
        ]

        # Walk through directories to find TTF fonts
        for font_dir in font_dirs:
            if os.path.exists(font_dir):
                for root, dirs, files in os.walk(font_dir):
                    for file in files:
                        if file.lower().endswith('.ttf'):
                            system_fonts.append(os.path.join(root, file))

    return system_fonts


if __name__ == "__main__":
    ensure_font_directory()
