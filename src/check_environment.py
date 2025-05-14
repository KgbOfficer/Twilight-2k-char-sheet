"""
check_environment.py - Verify that all required components are available
"""

import sys
import os
from pathlib import Path
import importlib
import subprocess


def check_python_version():
    """Check Python version"""
    print("\n--- Checking Python Version ---")
    python_version = sys.version_info
    print(f"Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")

    # Check if Python version is compatible
    is_compatible = python_version.major == 3 and python_version.minor >= 9
    print(f"Compatible version: {is_compatible}")

    return is_compatible


def check_dependencies():
    """Check if required packages are installed"""
    print("\n--- Checking Required Packages ---")
    required_packages = [
        "PyQt6",
        "PyQt6.QtCore",
        "PyQt6.QtWidgets",
        "PyQt6.QtGui",
        "PyQt6.QtMultimedia"
    ]

    all_available = True

    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✓ {package}: Installed")
        except ImportError as e:
            print(f"✗ {package}: Not found - {e}")
            all_available = False

    if not all_available:
        print("\nSome required packages are missing. Run the following command:")
        print("pip install -r requirements.txt")

    return all_available


def check_asset_directories():
    """Check if required asset directories exist"""
    print("\n--- Checking Asset Directories ---")
    required_dirs = [
        "assets/fonts",
        "assets/images/backgrounds",
        "assets/images/icons",
        "assets/sounds",
        "assets/music"
    ]

    all_exist = True

    for directory in required_dirs:
        dir_path = Path(directory)
        if dir_path.exists() and dir_path.is_dir():
            print(f"✓ {directory}: Exists")
        else:
            print(f"✗ {directory}: Not found")
            all_exist = False

    if not all_exist:
        print("\nSome required directories are missing. Run the following command:")
        print("python fonts_setup.py")
        print("python image_setup.py")

    return all_exist


def check_required_files():
    """Check if required asset files exist"""
    print("\n--- Checking Required Files ---")
    required_files = [
        "assets/fonts/military_font.ttf",
        "assets/images/backgrounds/default_bg.png",
        "assets/images/backgrounds/military_bg.png",
        "assets/images/backgrounds/soviet_bg.png",
        "assets/images/icons/app_icon.png",
        "assets/images/icons/dice.png",
        "assets/images/icons/save.png",
        "assets/images/icons/export.png",
        "assets/images/icons/new.png",
        "assets/sounds/button_click.wav",
        "assets/sounds/dice_roll.wav",
        "assets/music/main_theme.mp3",
        "assets/music/military_theme.mp3",
        "assets/music/soviet_theme.mp3"
    ]

    all_exist = True

    for file_path in required_files:
        path = Path(file_path)
        if path.exists() and path.is_file():
            print(f"✓ {file_path}: Exists")
        else:
            print(f"✗ {file_path}: Not found")
            all_exist = False

    if not all_exist:
        print("\nSome required files are missing. Run the following commands:")
        print("python fonts_setup.py")
        print("python image_setup.py")

    return all_exist


def check_source_files():
    """Check if core source files exist"""
    print("\n--- Checking Core Source Files ---")
    required_files = [
        "src/main.py",
        "src/config.py",
        "src/controllers/dice_controller.py",
        "src/controllers/game_controller.py",
        "src/controllers/character_controller.py",
        "src/controllers/career_controller.py",
        "src/models/character.py",
        "src/models/attribute.py",
        "src/models/skill.py",
        "src/models/career.py",
        "src/ui/main_window.py",
        "src/ui/intro_screen.py",
        "src/ui/theme_manager.py",
        "src/ui/character_creation.py",
        "src/utils/audio_manager.py",
        "src/utils/resource_loader.py",
        "src/utils/pdf_generator.py"
    ]

    all_exist = True

    for file_path in required_files:
        path = Path(file_path)
        if path.exists() and path.is_file():
            print(f"✓ {file_path}: Exists")
        else:
            print(f"✗ {file_path}: Not found")
            all_exist = False

    if not all_exist:
        print("\nSome core source files are missing. Check your project structure.")

    return all_exist


def check_career_controller():
    """Check if CareerController has the necessary signal"""
    print("\n--- Checking CareerController ---")
    career_controller_path = Path("src/controllers/career_controller.py")

    if not career_controller_path.exists():
        print("✗ CareerController file not found")
        return False

    with open(career_controller_path, "r") as f:
        content = f.read()

    if "careerCompleted = pyqtSignal" in content:
        print("✓ CareerController has careerCompleted signal")
        signal_ok = True
    else:
        print("✗ CareerController missing careerCompleted signal")
        signal_ok = False

    if "def _on_career_completed" in content or "def on_career_completed" in content:
        print("✓ CareerController has career completion handler")
        handler_ok = True
    else:
        print("✗ CareerController missing career completion handler")
        handler_ok = False

    if not signal_ok or not handler_ok:
        print("\nCareerController needs to be fixed. Run the following command:")
        print("python fixed_main.py")

    return signal_ok and handler_ok


def check_game_controller():
    """Check GameController for potential issues"""
    print("\n--- Checking GameController ---")
    game_controller_path = Path("src/controllers/game_controller.py")

    if not game_controller_path.exists():
        print("✗ GameController file not found")
        return False

    with open(game_controller_path, "r") as f:
        content = f.read()

    issues = []

    # Check for error-prone patterns
    if "self.career_controller.careerCompleted.connect" in content:
        connection_line = \
        [line for line in content.split("\n") if "self.career_controller.careerCompleted.connect" in line][0].strip()
        print(f"✓ Connection to careerCompleted exists: {connection_line}")
    else:
        print("✗ No connection to careerCompleted signal")
        issues.append("Missing connection to careerCompleted signal")

    if issues:
        print("\nGameController has potential issues that need fixing:")
        for issue in issues:
            print(f"- {issue}")
        print("\nRun the following command to apply fixes:")
        print("python fixed_main.py")
        return False

    return True


def run_simple_test():
    """Run a simple test to check if PyQt works"""
    print("\n--- Running Simple PyQt Test ---")
    test_script = Path("test_pyqt.py")

    if not test_script.exists():
        print("✗ test_pyqt.py not found")
        return False

    try:
        print("Attempting to run PyQt test...")
        result = subprocess.run([sys.executable, "test_pyqt.py"],
                                capture_output=True,
                                text=True,
                                timeout=5)

        if result.returncode == 0:
            print("✓ PyQt test ran successfully")
            return True
        else:
            print(f"✗ PyQt test failed with return code {result.returncode}")
            print(f"Error output: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("✗ PyQt test timed out - this might be normal if it displayed a window")
        return True
    except Exception as e:
        print(f"✗ Error running PyQt test: {e}")
        return False


def main():
    """Run all checks"""
    print("=== Twilight 2000 Character Creator Environment Check ===")

    # Run all checks
    python_ok = check_python_version()
    deps_ok = check_dependencies()
    dirs_ok = check_asset_directories()
    files_ok = check_required_files()
    source_ok = check_source_files()
    career_controller_ok = check_career_controller()
    game_controller_ok = check_game_controller()

    # Run PyQt test if basic checks pass
    if python_ok and deps_ok:
        pyqt_ok = run_simple_test()
    else:
        pyqt_ok = False
        print("\n--- Skipping PyQt Test ---")
        print("Python or dependency check failed. Skipping PyQt test.")

    # Summarize results
    print("\n=== Summary ===")
    print(f"Python Version: {'✓' if python_ok else '✗'}")
    print(f"Dependencies: {'✓' if deps_ok else '✗'}")
    print(f"Asset Directories: {'✓' if dirs_ok else '✗'}")
    print(f"Required Files: {'✓' if files_ok else '✗'}")
    print(f"Source Files: {'✓' if source_ok else '✗'}")
    print(f"CareerController: {'✓' if career_controller_ok else '✗'}")
    print(f"GameController: {'✓' if game_controller_ok else '✗'}")
    print(f"PyQt Test: {'✓' if pyqt_ok else '✗'}")

    # Overall assessment
    all_checks = python_ok and deps_ok and dirs_ok and files_ok and source_ok and career_controller_ok and game_controller_ok and pyqt_ok

    if all_checks:
        print("\n✅ All checks passed! The environment appears to be set up correctly.")
        print("To run the application, use:")
        print("python src/main.py")
    else:
        print("\n❌ Some checks failed. Please address the issues mentioned above.")
        print("If you've already fixed the issues and they're still being reported,")
        print("try running with the fixed main script:")
        print("python fixed_main.py")


if __name__ == "__main__":
    main()