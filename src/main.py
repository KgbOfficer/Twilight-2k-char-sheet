"""
main.py - Entry point for the Twilight 2000 Character Creator application
"""

import sys
from PyQt6.QtWidgets import QApplication
from src.ui.main_window import MainWindow
from src.utils.resource_loader import setup_resources


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