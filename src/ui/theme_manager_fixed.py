"""
theme_manager_fixed.py - Theme management for the application with better font handling
"""

from PyQt6.QtGui import QPalette, QColor, QFont, QFontDatabase
from PyQt6.QtWidgets import QApplication
import src.config as config
import os


class ThemeManager:
    """Manages application themes and styling"""

    def __init__(self):
        self.current_theme = config.DEFAULT_THEME
        self._setup_fonts()

    def _setup_fonts(self):
        """Load custom fonts for the application"""
        try:
            # Check if font file exists
            military_font_path = config.MILITARY_FONT
            if not os.path.exists(military_font_path):
                print(f"Error: Could not load font {military_font_path}")
                # Fallback to a system font
                config.MILITARY_FONT_FAMILY = "Courier New"
                return

            # Load military font
            font_id = QFontDatabase.addApplicationFont(military_font_path)
            if font_id < 0:
                print(f"Error: Could not load font {military_font_path}")
                # Fallback to a system font that might look military-ish
                config.MILITARY_FONT_FAMILY = "Courier New"
            else:
                font_families = QFontDatabase.applicationFontFamilies(font_id)
                if font_families:
                    config.MILITARY_FONT_FAMILY = font_families[0]
                else:
                    print(f"Error: No font families found for {military_font_path}")
                    config.MILITARY_FONT_FAMILY = "Courier New"
        except Exception as e:
            print(f"Error loading custom fonts: {e}")
            # Fallback to a system font that might look military-ish
            config.MILITARY_FONT_FAMILY = "Courier New"

    def get_theme_data(self, theme_name=None):
        """Get the data for a specific theme"""
        if theme_name is None:
            theme_name = self.current_theme

        if theme_name not in config.THEMES:
            theme_name = config.DEFAULT_THEME

        return config.THEMES[theme_name]

    def set_theme(self, theme_name):
        """Set the application theme"""
        if theme_name not in config.THEMES:
            print(f"Warning: Theme {theme_name} not found, using default")
            theme_name = config.DEFAULT_THEME

        self.current_theme = theme_name
        theme_data = self.get_theme_data()

        # Apply the theme to the application
        self._apply_theme(theme_data)

        # Return the theme data in case it's needed
        return theme_data

    def _apply_theme(self, theme_data):
        """Apply theme to the application"""
        app = QApplication.instance()
        if not app:
            print("Warning: No QApplication instance found")
            return

        # Create a palette for the theme
        palette = QPalette()

        # Set palette colors
        palette.setColor(QPalette.ColorRole.Window, QColor(theme_data["primary_bg"]))
        palette.setColor(QPalette.ColorRole.WindowText, QColor(theme_data["text"]))
        palette.setColor(QPalette.ColorRole.Base, QColor(theme_data["secondary_bg"]))
        palette.setColor(QPalette.ColorRole.AlternateBase, QColor(theme_data["accent"]))
        palette.setColor(QPalette.ColorRole.ToolTipBase, QColor(theme_data["secondary_bg"]))
        palette.setColor(QPalette.ColorRole.ToolTipText, QColor(theme_data["text"]))
        palette.setColor(QPalette.ColorRole.Text, QColor(theme_data["text"]))
        palette.setColor(QPalette.ColorRole.Button, QColor(theme_data["button_bg"]))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor(theme_data["button_text"]))
        palette.setColor(QPalette.ColorRole.Highlight, QColor(theme_data["highlight"]))
        palette.setColor(QPalette.ColorRole.HighlightedText, QColor(theme_data["button_text"]))

        # Apply the palette to the application
        app.setPalette(palette)

        # Create a stylesheet for additional styling
        stylesheet = f"""
        QMainWindow, QDialog {{
            background-color: {theme_data["primary_bg"]};
        }}

        QLabel {{
            color: {theme_data["text"]};
        }}

        QPushButton {{
            background-color: {theme_data["button_bg"]};
            color: {theme_data["button_text"]};
            border: 1px solid {theme_data["border"]};
            padding: 5px 10px;
            border-radius: 3px;
        }}

        QPushButton:hover {{
            background-color: {theme_data["highlight"]};
        }}

        QPushButton:pressed {{
            background-color: {theme_data["accent"]};
        }}

        QLineEdit, QTextEdit, QComboBox {{
            background-color: {theme_data["secondary_bg"]};
            color: {theme_data["text"]};
            border: 1px solid {theme_data["border"]};
            padding: 2px;
        }}

        QScrollBar {{
            background-color: {theme_data["primary_bg"]};
        }}

        QScrollBar::handle {{
            background-color: {theme_data["accent"]};
        }}
        """

        # Apply the stylesheet
        app.setStyleSheet(stylesheet)

    def get_military_font(self, size=12, bold=False):
        """Get the military font at a specific size"""
        # First try to create a font from the military font family
        font = QFont(config.MILITARY_FONT_FAMILY, size)

        # If that fails, fallback to a system monospace font
        if not font.exactMatch():
            font = QFont("Courier New", size)

        if bold:
            font.setBold(True)

        return font

    def get_default_font(self, size=12, bold=False):
        """Get the default font at a specific size"""
        font = QFont(config.DEFAULT_FONT, size)
        if bold:
            font.setBold(True)
        return font


# Create a global instance for easy access
theme_manager = ThemeManager()