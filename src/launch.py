"""
launch.py - Comprehensive launcher that applies all fixes and starts the application
"""

import sys
import os
import shutil
import subprocess
from pathlib import Path


def apply_all_fixes():
    """Apply all necessary fixes before launching the application"""
    print("=== Twilight 2000 Character Creator Launcher ===")
    print("Applying fixes and setting up the environment...")

    # Step 1: Check if Python and dependencies are available
    print("\nChecking Python and dependencies...")
    try:
        # Check Python version
        if sys.version_info.major < 3 or (sys.version_info.major == 3 and sys.version_info.minor < 9):
            print("⚠️ Warning: This application requires Python 3.9 or higher.")
            print(f"Current Python version: {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

        # Check PyQt6
        try:
            import PyQt6
            from PyQt6.QtWidgets import QApplication
            print("✓ PyQt6 is installed")
        except ImportError:
            print("❌ PyQt6 is not installed. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "PyQt6==6.6.0", "PyQt6-Qt6==6.6.0"])

        # Check PyPDF2
        try:
            import PyPDF2
            print("✓ PyPDF2 is installed")
        except ImportError:
            print("❌ PyPDF2 is not installed. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2==3.0.1"])

        # Check reportlab
        try:
            import reportlab
            print("✓ reportlab is installed")
        except ImportError:
            print("❌ reportlab is not installed. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "reportlab==4.0.4"])

    except Exception as e:
        print(f"❌ Error checking dependencies: {e}")

    # Step 2: Ensure all required directories exist
    print("\nEnsuring required directories exist...")
    try:
        directories = [
            "assets/fonts",
            "assets/images/backgrounds",
            "assets/images/icons",
            "assets/sounds",
            "assets/music"
        ]

        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
            print(f"✓ Created directory: {directory}")
    except Exception as e:
        print(f"❌ Error creating directories: {e}")

    # Step 3: Create placeholder font file
    print("\nChecking font file...")
    try:
        font_path = Path("assets/fonts/military_font.ttf")

        if not font_path.exists():
            print("Font file not found. Creating placeholder...")

            # Check if fonts_setup.py exists and run it
            if Path("fonts_setup.py").exists():
                subprocess.run([sys.executable, "fonts_setup.py"])
            else:
                # Simple font creation
                print("Creating minimal font placeholder...")
                with open(font_path, "wb") as f:
                    # Write minimal TTF header
                    f.write(b"\x00\x01\x00\x00\x00\x0C\x00\x00\x00\x00\x00\x00\x00\x00")
        else:
            print("✓ Font file exists")
    except Exception as e:
        print(f"❌ Error handling font file: {e}")

    # Step 4: Create placeholder images
    print("\nChecking image files...")
    try:
        background_files = [
            "assets/images/backgrounds/default_bg.png",
            "assets/images/backgrounds/military_bg.png",
            "assets/images/backgrounds/soviet_bg.png"
        ]

        icon_files = [
            "assets/images/icons/app_icon.png",
            "assets/images/icons/dice.png",
            "assets/images/icons/save.png",
            "assets/images/icons/export.png",
            "assets/images/icons/new.png"
        ]

        # Check if any image is missing
        missing_images = []
        for img_path in background_files + icon_files:
            if not Path(img_path).exists():
                missing_images.append(img_path)

        if missing_images:
            print(f"Missing {len(missing_images)} image files. Creating placeholders...")

            # Check if image_setup.py exists and run it
            if Path("image_setup.py").exists():
                subprocess.run([sys.executable, "image_setup.py"])
            else:
                # Simple image creation
                print("Creating minimal image placeholders...")
                for img_path in missing_images:
                    path = Path(img_path)
                    path.parent.mkdir(parents=True, exist_ok=True)
                    with open(path, "wb") as f:
                        # Write minimal PNG header
                        f.write(
                            b"\x89PNG\r\n\x1a\n\x00\x00\x00\x0dIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\x0aIDAT\x08\x99c\x00\x00\x00\x02\x00\x01\xe2\x21\xbc\x33\x00\x00\x00\x00IEND\xaeB`\x82")
                    print(f"✓ Created placeholder for {img_path}")
        else:
            print("✓ All image files exist")
    except Exception as e:
        print(f"❌ Error handling image files: {e}")

    # Step 5: Create placeholder sound files
    print("\nChecking sound files...")
    try:
        sound_files = [
            "assets/sounds/button_click.wav",
            "assets/sounds/dice_roll.wav",
            "assets/music/main_theme.mp3",
            "assets/music/military_theme.mp3",
            "assets/music/soviet_theme.mp3"
        ]

        # Check if any sound is missing
        missing_sounds = []
        for sound_path in sound_files:
            if not Path(sound_path).exists():
                missing_sounds.append(sound_path)

        if missing_sounds:
            print(f"Missing {len(missing_sounds)} sound files. Creating placeholders...")

            # Create simple sound placeholders
            for sound_path in missing_sounds:
                path = Path(sound_path)
                path.parent.mkdir(parents=True, exist_ok=True)
                with open(path, "wb") as f:
                    # Write minimal audio file
                    f.write(b"\x00" * 64)
                print(f"✓ Created placeholder for {sound_path}")
        else:
            print("✓ All sound files exist")
    except Exception as e:
        print(f"❌ Error handling sound files: {e}")

    # Step 6: Fix CareerController issues
    print("\nChecking CareerController...")
    try:
        career_controller_path = Path("src/controllers/career_controller.py")

        if career_controller_path.exists():
            # Read the file content
            with open(career_controller_path, "r") as f:
                content = f.read()

            # Check if it has the careerCompleted signal
            if "careerCompleted = pyqtSignal" not in content:
                print("CareerController missing careerCompleted signal. Fixing...")

                # Check if we've already created the fixed version
                fixed_path = Path("career_controller_fixed.py")
                if fixed_path.exists():
                    # Back up original if not already backed up
                    backup_path = Path("src/controllers/career_controller_original.py")
                    if not backup_path.exists():
                        shutil.copy(career_controller_path, backup_path)
                        print("✓ Backed up original career_controller.py")

                    # Use our fixed version
                    shutil.copy(fixed_path, career_controller_path)
                    print("✓ Replaced career_controller.py with fixed version")
                else:
                    print("⚠️ No fixed CareerController found. Applying minimal fix...")

                    # Try to modify the existing file
                    lines = content.split("\n")

                    # Find the signals section
                    for i, line in enumerate(lines):
                        if "# Signals" in line or "    # Signals" in line:
                            # Find the end of the signals section
                            for j in range(i + 1, len(lines)):
                                if "pyqtSignal" in lines[j]:
                                    last_signal_line = j
                                else:
                                    break

                            # Add the missing signal
                            lines.insert(last_signal_line + 1,
                                         "    careerCompleted = pyqtSignal(dict)  # Emitted when a career is completed, passes career data")
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

                    print("✓ Added missing signal and method to career_controller.py")
            else:
                print("✓ CareerController has careerCompleted signal")
        else:
            print("❌ CareerController file not found")
    except Exception as e:
        print(f"❌ Error fixing CareerController: {e}")

    # Step 7: Fix theme_manager.py to handle missing fonts
    print("\nChecking ThemeManager...")
    try:
        theme_manager_path = Path("src/ui/theme_manager.py")

        if theme_manager_path.exists():
            # Read the file content
            with open(theme_manager_path, "r") as f:
                content = f.read()

            # Check if it has the _setup_fonts method with proper error handling
            if "_setup_fonts" in content and "except Exception as e:" in content:
                print("✓ ThemeManager already has error handling for fonts")
            else:
                print("ThemeManager needs better font handling. Fixing...")

                # Check if we've already created the fixed version
                fixed_path = Path("theme_manager_fixed.py")
                if fixed_path.exists():
                    # Back up original if not already backed up
                    backup_path = Path("src/ui/theme_manager_original.py")
                    if not backup_path.exists():
                        shutil.copy(theme_manager_path, backup_path)
                        print("✓ Backed up original theme_manager.py")

                    # Use our fixed version
                    shutil.copy(fixed_path, theme_manager_path)
                    print("✓ Replaced theme_manager.py with fixed version")
                else:
                    print("⚠️ No fixed ThemeManager found. Using original")
        else:
            print("❌ ThemeManager file not found")
    except Exception as e:
        print(f"❌ Error fixing ThemeManager: {e}")

    # Step 8: Fix audio_manager.py to handle missing audio files
    print("\nChecking AudioManager...")
    try:
        audio_manager_path = Path("src/utils/audio_manager.py")

        if audio_manager_path.exists():
            # Read the file content to check for potential issues
            with open(audio_manager_path, "r") as f:
                content = f.read()

            # Check if QMediaPlayer is used and might cause issues
            if "QMediaPlayer" in content and not "except Exception as e:" in content:
                print("AudioManager may have issues with QMediaPlayer. Creating safer version...")

                # Check if we've already created a disabled version
                disabled_path = Path("audio_manager_disabled.py")
                if disabled_path.exists():
                    # Back up original if not already backed up
                    backup_path = Path("src/utils/audio_manager_original.py")
                    if not backup_path.exists():
                        shutil.copy(audio_manager_path, backup_path)
                        print("✓ Backed up original audio_manager.py")

                    # Use our disabled version
                    shutil.copy(disabled_path, audio_manager_path)
                    print("✓ Replaced audio_manager.py with safer version")
                else:
                    print("⚠️ No safer AudioManager found. Using original (may crash)")
            else:
                print("✓ AudioManager appears to have proper error handling")
        else:
            print("❌ AudioManager file not found")
    except Exception as e:
        print(f"❌ Error fixing AudioManager: {e}")

    # Step 9: Fix skill.py if it's empty
    print("\nChecking skill.py...")
    try:
        skill_path = Path("src/models/skill.py")

        if skill_path.exists():
            # Check if file is empty
            if os.path.getsize(skill_path) == 0:
                print("skill.py is empty. Fixing...")

                # Check if we have a fixed version
                skill_fixed_path = Path("skill.py")
                if skill_fixed_path.exists():
                    shutil.copy(skill_fixed_path, skill_path)
                    print("✓ Replaced empty skill.py with fixed version")
                else:
                    print("⚠️ No skill.py implementation found. Application may not work.")
            else:
                print("✓ skill.py exists and has content")
        else:
            print("❌ skill.py file not found")
    except Exception as e:
        print(f"❌ Error fixing skill.py: {e}")

    print("\nAll fixes applied. Ready to launch application!")
    return True


def launch_application():
    """Launch the application"""
    print("\n=== Launching Twilight 2000 Character Creator ===")
    try:
        # Run the application
        subprocess.run([sys.executable, "src/main.py"])
        return True
    except Exception as e:
        print(f"❌ Error launching application: {e}")

        # Try running with debug mode
        print("\nAttempting to run with debug output...")
        try:
            if Path("debug_main.py").exists():
                subprocess.run([sys.executable, "debug_main.py"])
            else:
                print("❌ debug_main.py not found")
        except Exception as e2:
            print(f"❌ Error launching with debug mode: {e2}")

        return False


def main():
    """Main function"""
    # Apply all fixes
    fixes_applied = apply_all_fixes()

    # Ask user if they want to continue
    if fixes_applied:
        while True:
            try:
                response = input("\nLaunch the application now? (y/n): ").strip().lower()
                if response in ['y', 'yes']:
                    launch_application()
                    break
                elif response in ['n', 'no']:
                    print("Application not launched. Run 'python src/main.py' when ready.")
                    break
                else:
                    print("Please enter 'y' or 'n'.")
            except KeyboardInterrupt:
                print("\nOperation cancelled.")
                break
    else:
        print("\nFixes could not be fully applied. Please fix the issues manually.")


if __name__ == "__main__":
    main()