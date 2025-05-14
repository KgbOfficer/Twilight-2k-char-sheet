"""
debug_main.py - Debug version of the main entry point
"""

import sys
import traceback


def main():
    """Main application entry point with debug output"""
    try:
        print("Starting application...")

        # Import QApplication
        print("Importing PyQt6.QtWidgets.QApplication...")
        from PyQt6.QtWidgets import QApplication

        # Create the application
        print("Creating QApplication...")
        app = QApplication(sys.argv)

        # Import MainWindow
        print("Importing MainWindow...")
        try:
            from src.ui.main_window import MainWindow
            print("MainWindow imported successfully")
        except ImportError as e:
            print(f"Error importing MainWindow: {e}")
            traceback.print_exc()

            # Try a simpler window
            print("Falling back to a simple QMainWindow...")
            from PyQt6.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget

            class SimpleWindow(QMainWindow):
                def __init__(self):
                    super().__init__()
                    self.setWindowTitle("Twilight 2000 - Simple Mode")
                    self.resize(800, 600)

                    central = QWidget()
                    layout = QVBoxLayout(central)
                    label = QLabel("Twilight 2000 Character Creator (Simple Mode)")
                    layout.addWidget(label)
                    self.setCentralWidget(central)

            # Create and show the simple window
            print("Creating SimpleWindow...")
            window = SimpleWindow()
        else:
            # If MainWindow imported correctly, try to create it
            print("Creating MainWindow...")
            try:
                window = MainWindow()
                print("MainWindow created successfully")
            except Exception as e:
                print(f"Error creating MainWindow: {e}")
                traceback.print_exc()
                sys.exit(1)

        # Show the window
        print("Showing window...")
        window.show()

        # Run the application
        print("Starting event loop...")
        sys.exit(app.exec())

    except Exception as e:
        print(f"Unexpected error: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()