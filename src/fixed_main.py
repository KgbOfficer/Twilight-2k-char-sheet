"""
fixed_main.py - Entry point with fixed components
"""

import sys
import os
import shutil
from pathlib import Path

# First, make sure we have the assets directory structure
def ensure_assets_directories():
    """Create the necessary assets directories if they don't exist"""
    directories = [
        "assets/fonts",
        "assets/images/backgrounds",
        "assets/images/icons",
        "assets/sounds",
        "assets/music"
    ]

    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)

# Next, ensure we have a placeholder font
def ensure_font_file():
    """Ensure we have a font file to use"""
    font_path = Path("assets/fonts/military_font.ttf")

    if not font_path.exists():
        # Search for a system font to use as placeholder
        system_fonts = []

        if sys.platform.startswith('win'):
            # Windows - try to find Courier New
            if os.path.exists(os.path.join(os.environ['WINDIR'], 'Fonts', 'cour.ttf')):
                system_fonts.append(os.path.join(os.environ['WINDIR'], 'Fonts', 'cour.ttf'))

        if system_fonts:
            # Copy the first found font
            print(f"Copying system font as placeholder: {system_fonts[0]}")
            shutil.copy(system_fonts[0], font_path)
        else:
            # Create a minimal placeholder
            print("Creating minimal placeholder font file")
            with open(font_path, "wb") as f:
                # Write minimal TTF header to create a simple placeholder
                f.write(b"\x00\x01\x00\x00\x00\x0C\x00\x00\x00\x00\x00\x00\x00\x00")

# Make sure we have sound files
def ensure_sound_files():
    """Ensure we have placeholder sound files"""
    sound_files = [
        "assets/sounds/button_click.wav",
        "assets/sounds/dice_roll.wav",
        "assets/music/main_theme.mp3",
        "assets/music/military_theme.mp3",
        "assets/music/soviet_theme.mp3"
    ]

    for sound_file in sound_files:
        sound_path = Path(sound_file)
        if not sound_path.exists():
            print(f"Creating placeholder sound file: {sound_file}")
            # Create an empty sound file
            sound_path.parent.mkdir(parents=True, exist_ok=True)
            with open(sound_path, "wb") as f:
                # Write minimal empty audio file
                f.write(b"\x00" * 64)

# Now check for the CareerController issue and fix it if needed
def fix_career_controller():
    """Fix the CareerController if needed"""
    career_controller_path = Path("src/controllers/career_controller.py")

    if career_controller_path.exists():
        # Read the file content
        with open(career_controller_path, "r") as f:
            content = f.read()

        # Check if it has the careerCompleted signal
        if "careerCompleted = pyqtSignal" not in content:
            print("Fixing CareerController - adding missing signal")

            # Check if we've already created the fixed version
            fixed_path = Path("career_controller_fixed.py")
            if fixed_path.exists():
                # Use our fixed version
                shutil.copy(fixed_path, career_controller_path)
                print("Replaced career_controller.py with fixed version")
            else:
                # Try to modify the existing file
                lines = content.split("\n")

                # Find the signals section
                for i, line in enumerate(lines):
                    if "# Signals" in line or "    # Signals" in line:
                        # Find the end of the signals section
                        for j in range(i+1, len(lines)):
                            if "pyqtSignal" in lines[j]:
                                last_signal_line = j
                            else:
                                break

                        # Add the missing signal
                        lines.insert(last_signal_line + 1, "    careerCompleted = pyqtSignal(dict)  # Emitted when a career is completed, passes career data")
                        break

                # Also look for _on_career_completed method reference
                method_found = False
                for i, line in enumerate(lines):
                    if "_on_career_completed" in line:
                        method_found = True
                        break

                if not method_found:
                    # Add a placeholder method
                    for i, line in enumerate(lines):
                        if "def " in line:
                            # Find last method
                            last_method_line = i

                    # Add missing method
                    lines.append("")
                    lines.append("    def _on_career_completed(self, career_data):")
                    lines.append("        \"\"\"Handle career completion")
                    lines.append("")
                    lines.append("        Args:")
                    lines.append("            career_data: Career data dictionary")
                    lines.append("        \"\"\"")
                    lines.append("        # Update character")
                    lines.append("        self.characterChanged.emit(self.character)")
                    lines.append("")

                # Write the modified content back
                with open(career_controller_path, "w") as f:
                    f.write("\n".join(lines))

                print("Added missing signal and method to career_controller.py")

# Fix theme manager to handle missing fonts
def fix_theme_manager():
    """Fix the theme manager if needed"""
    theme_manager_path = Path("src/ui/theme_manager.py")

    if theme_manager_path.exists():
        # Check if we've already created the fixed version
        fixed_path = Path("theme_manager_fixed.py")
        if fixed_path.exists():
            # Use our fixed version
            shutil.copy(fixed_path, theme_manager_path)
            print("Replaced theme_manager.py with fixed version")

# Make sure we have all required directories and files
ensure_assets_directories()
ensure_font_file()
ensure_sound_files()
fix_career_controller()
fix_theme_manager()

# Now import and run the application
print("Starting application...")

try:
    from src.ui.main_window import MainWindow
    from src.utils.resource_loader import setup_resources
    from PyQt6.QtWidgets import QApplication

    def main():
        """Main application entry point"""
        # Create the application
        app = QApplication(sys.argv)

        # Setup resources
        setup_resources()

        # Create and show the main window
        window = MainWindow()
        window.show()

        # Run the application
        sys.exit(app.exec())

    if __name__ == "__main__":
        main()

except Exception as e:
    print(f"Error starting application: {e}")
    import traceback
    traceback.print_exc()
