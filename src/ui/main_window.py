"""
main_window.py - Main application window
"""

from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QStackedWidget, QMessageBox, QFileDialog,
    QSizePolicy, QSpacerItem
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont, QAction

import src.config as config
from src.ui.intro_screen import IntroScreen
from src.ui.theme_manager import theme_manager
from src.utils.audio_manager import audio_manager
from src.controllers.game_controller import game_controller


class MainWindow(QMainWindow):
    """Main application window for Twilight 2000 Character Creator"""

    def __init__(self):
        """Initialize the main window"""
        super().__init__()

        # Configure the window
        self.setWindowTitle(config.APP_NAME)
        self.resize(config.DEFAULT_WINDOW_WIDTH, config.DEFAULT_WINDOW_HEIGHT)

        # Set up the menu bar
        self._setup_menu_bar()

        # Create central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create main layout
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        # Create header
        self._setup_header()

        # Create stacked widget for screens
        self.stacked_widget = QStackedWidget()
        self.main_layout.addWidget(self.stacked_widget)

        # Create screens
        self.intro_screen = IntroScreen(self)
        self.stacked_widget.addWidget(self.intro_screen)

        # Uncomment these when implemented:
        # self.character_creation_screen = CharacterCreationScreen(self)
        # self.stacked_widget.addWidget(self.character_creation_screen)
        # self.character_sheet_screen = CharacterSheetScreen(self)
        # self.stacked_widget.addWidget(self.character_sheet_screen)

        # Set initial screen
        self.stacked_widget.setCurrentWidget(self.intro_screen)

        # Apply theme
        theme_manager.set_theme(config.DEFAULT_THEME)

        # Start background music
        audio_manager.play_music("intro_music")

    def _setup_menu_bar(self):
        """Set up the menu bar"""
        # File menu
        file_menu = self.menuBar().addMenu("&File")

        # New character action
        new_action = QAction("&New Character", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self._new_character)
        file_menu.addAction(new_action)

        # Open character action
        open_action = QAction("&Open Character", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self._open_character)
        file_menu.addAction(open_action)

        # Save character action
        save_action = QAction("&Save Character", self)
        save_action.setShortcut("Ctrl+S")
        save_action.triggered.connect(self._save_character)
        file_menu.addAction(save_action)

        # Export to PDF action
        export_action = QAction("&Export to PDF", self)
        export_action.setShortcut("Ctrl+E")
        export_action.triggered.connect(self._export_to_pdf)
        file_menu.addAction(export_action)

        file_menu.addSeparator()

        # Exit action
        exit_action = QAction("E&xit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Theme menu
        theme_menu = self.menuBar().addMenu("&Theme")

        # Add theme actions
        for theme_key, theme_data in config.THEMES.items():
            theme_action = QAction(theme_data["name"], self)
            theme_action.setData(theme_key)
            theme_action.triggered.connect(lambda checked, t=theme_key: theme_manager.set_theme(t))
            theme_menu.addAction(theme_action)

        # Audio menu
        audio_menu = self.menuBar().addMenu("&Audio")

        # Music toggle action
        music_action = QAction("&Music", self)
        music_action.setCheckable(True)
        music_action.setChecked(config.ENABLE_MUSIC)
        music_action.triggered.connect(lambda checked: audio_manager.enable_music(checked))
        audio_menu.addAction(music_action)

        # Sound effects toggle action
        sfx_action = QAction("&Sound Effects", self)
        sfx_action.setCheckable(True)
        sfx_action.setChecked(config.ENABLE_SFX)
        sfx_action.triggered.connect(lambda checked: audio_manager.enable_sfx(checked))
        audio_menu.addAction(sfx_action)

        # Help menu
        help_menu = self.menuBar().addMenu("&Help")

        # About action
        about_action = QAction("&About", self)
        about_action.triggered.connect(self._show_about)
        help_menu.addAction(about_action)

    def _setup_header(self):
        """Set up the header with title and theme switcher"""
        header_widget = QWidget()
        header_widget.setFixedHeight(80)
        header_layout = QHBoxLayout(header_widget)
        header_layout.setContentsMargins(20, 10, 20, 10)

        # Title label
        title_label = QLabel(config.APP_NAME)
        title_label.setFont(theme_manager.get_military_font(24, bold=True))
        title_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        header_layout.addWidget(title_label, 1)

        # Add spacer
        header_layout.addStretch(1)

        # Theme buttons
        for theme_key, theme_data in config.THEMES.items():
            theme_button = QPushButton(theme_data["name"])
            theme_button.setFixedSize(QSize(100, 40))
            theme_button.clicked.connect(lambda checked, t=theme_key: theme_manager.set_theme(t))
            header_layout.addWidget(theme_button)

        # Add header to main layout
        self.main_layout.addWidget(header_widget)

    def navigate_to_screen(self, screen):
        """Navigate to a specific screen

        Args:
            screen: The screen widget to navigate to
        """
        # Play sound
        audio_manager.play_sound("button_click")

        # Add screen to stacked widget if not already there
        if self.stacked_widget.indexOf(screen) == -1:
            self.stacked_widget.addWidget(screen)

        # Navigate to the screen
        self.stacked_widget.setCurrentWidget(screen)

    def _new_character(self):
        """Create a new character"""
        # Play sound
        audio_manager.play_sound("button_click")

        # Reset the game controller
        game_controller.reset()

        # Navigate to the intro screen
        self.stacked_widget.setCurrentWidget(self.intro_screen)
        self.intro_screen.restart()

    def _open_character(self):
        """Open an existing character"""
        # Play sound
        audio_manager.play_sound("button_click")

        # Show file dialog
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Character", "", "Character Files (*.json);;All Files (*)")

        if file_path:
            # Load character
            if game_controller.load_character(file_path):
                # Navigate to character sheet screen (when implemented)
                # self.stacked_widget.setCurrentWidget(self.character_sheet_screen)
                # self.character_sheet_screen.update_display()
                pass
            else:
                QMessageBox.warning(self, "Error", "Failed to load character file.")

    def _save_character(self):
        """Save the current character"""
        # Play sound
        audio_manager.play_sound("button_click")

        # Show file dialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Character", "", "Character Files (*.json);;All Files (*)")

        if file_path:
            # Save character
            if game_controller.save_character(file_path):
                QMessageBox.information(self, "Success", "Character saved successfully.")
            else:
                QMessageBox.warning(self, "Error", "Failed to save character.")

    def _export_to_pdf(self):
        """Export the current character to PDF"""
        # Play sound
        audio_manager.play_sound("button_click")

        # Show file dialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Export to PDF", "", "PDF Files (*.pdf);;All Files (*)")

        if file_path:
            # Export to PDF
            if game_controller.export_to_pdf(file_path):
                QMessageBox.information(self, "Success", "Character exported to PDF successfully.")
            else:
                QMessageBox.warning(self, "Error", "Failed to export character to PDF.")

    def _show_about(self):
        """Show the about dialog"""
        # Play sound
        audio_manager.play_sound("button_click")

        # Show about dialog
        QMessageBox.about(self, "About " + config.APP_NAME,
            f"<h1>{config.APP_NAME}</h1>"
            f"<p>Version {config.APP_VERSION}</p>"
            f"<p>A character creator for Twilight 2000 4th Edition.</p>"
            f"<p>Based on the tabletop role-playing game by {config.GAME_PUBLISHER}.</p>"
        )

    def closeEvent(self, event):
        """Handle window close event"""
        # Stop music
        audio_manager.stop_music()

        # Accept the event
        event.accept()