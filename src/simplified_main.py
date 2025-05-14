"""
simplified_main.py - Simplified entry point for the Twilight 2000 Character Creator
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel


class SimpleMainWindow(QMainWindow):
    """A simplified main window for testing"""

    def __init__(self):
        super().__init__()

        # Configure the window
        self.setWindowTitle("Twilight 2000 Character Creator")
        self.resize(800, 600)

        # Create central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create main layout
        self.main_layout = QVBoxLayout(self.central_widget)

        # Add a label
        label = QLabel("Twilight 2000 Character Creator", self.central_widget)
        label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.main_layout.addWidget(label)


def main():
    """Main application entry point"""
    # Create the application
    app = QApplication(sys.argv)

    # Create and show the main window
    window = SimpleMainWindow()
    window.show()

    # Run the application
    sys.exit(app.exec())


if __name__ == "__main__":
    main()