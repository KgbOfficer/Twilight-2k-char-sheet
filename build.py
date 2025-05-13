"""
build.py - Script to build the Twilight 2000 Character Creator executable
"""

import os
import sys
import subprocess
import shutil


def compile_resources():
    """Compile Qt resources file into a Python module"""
    print("Compiling resources...")

    # Check if pyrcc6 is available
    try:
        subprocess.run(["pyrcc6", "--version"], check=True, capture_output=True)
    except (subprocess.SubprocessError, FileNotFoundError):
        print("Error: pyrcc6 not found. Make sure PyQt6 is installed correctly.")
        return False

    # Compile resources
    subprocess.run(["pyrcc6", "resources.qrc", "-o", "src/resources_rc.py"], check=True)
    print("Resources compiled successfully.")
    return True


def build_executable():
    """Build the executable using PyInstaller"""
    print("Building executable...")

    # Check if PyInstaller is available
    try:
        subprocess.run(["pyinstaller", "--version"], check=True, capture_output=True)
    except (subprocess.SubprocessError, FileNotFoundError):
        print("Error: PyInstaller not found. Install it with: pip install pyinstaller")
        return False

    # Build the executable
    subprocess.run([
        "pyinstaller",
        "--name=Twilight2000CharacterCreator",
        "--windowed",  # GUI mode
        "--onefile",  # Single executable
        "--icon=assets/images/icons/app_icon.png",
        "--add-data=assets;assets",  # Include assets
        "main.py"
    ], check=True)

    print("Executable built successfully.")
    return True


def cleanup():
    """Clean up build files"""
    print("Cleaning up build files...")

    # Remove build directory
    if os.path.exists("build"):
        shutil.rmtree("build")

    # Remove spec file
    if os.path.exists("Twilight2000CharacterCreator.spec"):
        os.remove("Twilight2000CharacterCreator.spec")

    # Remove compiled resources
    if os.path.exists("src/resources_rc.py"):
        os.remove("src/resources_rc.py")

    print("Cleanup complete.")


def main():
    """Main function"""
    print("Building Twilight 2000 Character Creator...")

    # Ensure assets directories exist
    os.makedirs("assets/fonts", exist_ok=True)
    os.makedirs("assets/images/backgrounds", exist_ok=True)
    os.makedirs("assets/images/icons", exist_ok=True)
    os.makedirs("assets/sounds", exist_ok=True)
    os.makedirs("assets/music", exist_ok=True)

    # Check for placeholder assets and warn if missing
    required_assets = [
        "assets/fonts/military_font.ttf",
        "assets/images/icons/app_icon.png",
        "assets/sounds/button_click.wav",
        "assets/sounds/dice_roll.wav",
        "assets/music/main_theme.mp3"
    ]

    missing_assets = [asset for asset in required_assets if not os.path.exists(asset)]
    if missing_assets:
        print("Warning: Some required assets are missing:")
        for asset in missing_assets:
            print(f"  - {asset}")
        print("Please add these assets before distributing the application.")

    # Compile resources
    if not compile_resources():
        return

    # Build executable
    if not build_executable():
        return

    # Cleanup
    cleanup()

    print("Build complete. Executable is in the dist directory.")


if __name__ == "__main__":
    main()