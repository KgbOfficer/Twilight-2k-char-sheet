"""
intro_screen.py - Introduction screen with scrolling text
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt, QTimer, QSize
from PyQt6.QtGui import QFont, QFontMetrics, QPixmap

import src.config as config
from src.ui.theme_manager import theme_manager
from src.utils.audio_manager import audio_manager
from src.ui.character_creation import BasicInfoScreen


class ScriptedTextLabel(QLabel):
    """A label that displays text character by character for a typewriter effect"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.full_text = ""
        self.current_pos = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update_text)
        self.setText("")
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setWordWrap(True)

        # Use the military font
        self.setFont(theme_manager.get_military_font(12))

    def start_script(self, text, speed=None, callback=None):
        """Start displaying text character by character

        Args:
            text: The text to display
            speed: Milliseconds between each character (default: config.TEXT_SCROLL_SPEED)
            callback: Function to call when text is fully displayed
        """
        self.full_text = text
        self.current_pos = 0
        self.setText("")
        self.callback = callback

        # Set scroll speed
        if speed is None:
            speed = config.TEXT_SCROLL_SPEED

        # Start the timer
        self.timer.start(speed)

    def _update_text(self):
        """Update the displayed text with the next character"""
        if self.current_pos < len(self.full_text):
            self.current_pos += 1
            self.setText(self.full_text[:self.current_pos])

            # Play a subtle typing sound for every 3rd character
            if self.current_pos % 3 == 0:
                # This would be better with a typing sound
                audio_manager.play_sound("button_click")
        else:
            # Stop the timer
            self.timer.stop()

            # Call the callback if provided
            if hasattr(self, 'callback') and self.callback:
                self.callback()

    def display_instantly(self, text):
        """Display text immediately without animation

        Args:
            text: The text to display
        """
        self.full_text = text
        self.current_pos = len(text)
        self.setText(text)

        # Stop the timer if it's running
        if self.timer.isActive():
            self.timer.stop()


class IntroScreen(QWidget):
    """Introduction screen with scrolling text"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self._setup_ui()

    def _setup_ui(self):
        """Set up the user interface"""
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.setSpacing(20)

        # Add spacer at the top
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Headline label
        self.headline_label = ScriptedTextLabel(self)
        self.headline_label.setFont(theme_manager.get_military_font(32, bold=True))
        self.headline_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.headline_label)

        # Main text label
        self.main_text_label = ScriptedTextLabel(self)
        self.main_text_label.setFont(theme_manager.get_military_font(16))
        self.main_text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.main_text_label)

        # Add spacer before button
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Button container (for centering)
        button_container = QWidget(self)
        button_layout = QHBoxLayout(button_container)
        button_layout.setContentsMargins(0, 0, 0, 0)

        # Add spacer on the left
        button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # Start button
        self.start_button = QPushButton("YES", self)
        self.start_button.setFont(theme_manager.get_military_font(16, bold=True))
        self.start_button.setMinimumSize(QSize(150, 50))
        self.start_button.setVisible(False)
        self.start_button.clicked.connect(self._on_start_clicked)
        button_layout.addWidget(self.start_button)

        # Add spacer on the right
        button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # Add button container to main layout
        main_layout.addWidget(button_container)

        # Add spacer at the bottom
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Start the intro sequence
        QTimer.singleShot(500, self._start_intro_sequence)

    def _start_intro_sequence(self):
        """Start the introduction sequence"""
        # Define the text for the headline
        headline_text = "YOU'RE ON YOUR OWN NOW"

        # Define the text for the main text
        main_text = ("It is the year 2000, no corner of the earth has been left untouched "
                     "by the nuclear Armageddon unleashed by warring nations. This is a story "
                     "about you, a survivor, and the other survivors you meet along the way.")

        # Start displaying the headline
        self.headline_label.start_script(headline_text, callback=self._on_headline_complete)

    def _on_headline_complete(self):
        """Called when the headline is fully displayed"""
        # Start displaying the main text after a short delay
        QTimer.singleShot(1000, lambda: self.main_text_label.start_script(
            self.main_text_label.full_text + self.main_text_label.text(),
            callback=self._on_main_text_complete
        ))

    def _on_main_text_complete(self):
        """Called when the main text is fully displayed"""
        # Wait a second, then show the prompt
        QTimer.singleShot(1000, self._show_prompt)

    def _show_prompt(self):
        """Show the 'Are you ready to begin?' prompt"""
        # Clear the current text
        self.headline_label.setText("")
        self.main_text_label.setText("")

        # Show the prompt
        self.headline_label.start_script("Are you ready to begin?", callback=lambda: self.start_button.setVisible(True))

    def _on_start_clicked(self):
        """Handle the start button click"""
        # Play button click sound
        audio_manager.play_sound("button_click")

        # Hide the button
        self.start_button.setVisible(False)

        # Show the lifepath explanation
        self._show_lifepath_explanation()

    def _show_lifepath_explanation(self):
        """Show the explanation of the lifepath system"""
        explanation_text = ("This is a character creator for Twilight 2000 4th edition, "
                            "that uses the Lifepath system. Your character will begin at 18, "
                            "and we will follow their life as they live it until war breaks out. "
                            "When that happens, we will know how old your character is during the war, "
                            "what skills they have accumulated during their life, and the choices "
                            "they've made along the way.")

        # Clear the current text
        self.headline_label.setText("")

        # Show the explanation
        self.main_text_label.start_script(explanation_text, callback=self._on_explanation_complete)

    def _on_explanation_complete(self):
        """Called when the explanation is fully displayed"""
        # Proceed to the character creation screen after a delay
        QTimer.singleShot(2000, self._proceed_to_character_creation)

    def _proceed_to_character_creation(self):
        """Proceed to the character creation screen"""
        # Create basic info screen
        basic_info_screen = BasicInfoScreen(self.parent)

        # Navigate to the basic info screen
        self.parent.navigate_to_screen(basic_info_screen)

    def restart(self):
        """Restart the intro sequence"""
        # Reset UI elements
        self.headline_label.setText("")
        self.main_text_label.setText("")
        self.start_button.setVisible(False)

        # Start the intro sequence again
        self._start_intro_sequence()