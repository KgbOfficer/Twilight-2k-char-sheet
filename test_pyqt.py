"""
test_pyqt.py - Simple test script for PyQt6
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


def main():
    # Create the application
    app = QApplication(sys.argv)

    # Create the main window
    window = QWidget()
    window.setWindowTitle("PyQt6 Test")
    window.resize(400, 200)

    # Create a layout
    layout = QVBoxLayout(window)

    # Add a label
    label = QLabel("PyQt6 is working correctly!", window)
    layout.addWidget(label)

    # Show the window
    window.show()

    # Run the application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()