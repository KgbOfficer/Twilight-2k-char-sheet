"""
character_creation.py - Character creation screens
"""

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit,
    QComboBox, QFormLayout, QGroupBox, QRadioButton, QSpacerItem, QSizePolicy,
    QScrollArea, QFrame
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont

import src.config as config
from src.ui.theme_manager import theme_manager
from src.utils.audio_manager import audio_manager
from src.controllers.game_controller import game_controller
from src.controllers.dice_controller import DiceController
from src.data.nationalities import get_all_nationalities


class BasicInfoScreen(QWidget):
    """Screen for entering basic character information"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.dice_controller = DiceController()
        self._setup_ui()

    def _setup_ui(self):
        """Set up the user interface"""
        # Main layout
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.setSpacing(20)

        # Title
        title_label = QLabel("Character Basics", self)
        title_label.setFont(theme_manager.get_military_font(24, bold=True))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)

        # Form
        form_widget = QWidget(self)
        form_layout = QFormLayout(form_widget)
        form_layout.setSpacing(15)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)

        # Name field
        self.name_edit = QLineEdit(self)
        self.name_edit.setFont(theme_manager.get_military_font(12))
        self.name_edit.setMinimumWidth(300)
        form_layout.addRow(QLabel("Name:", self), self.name_edit)

        # Nationality field
        self.nationality_combo = QComboBox(self)
        self.nationality_combo.setFont(theme_manager.get_military_font(12))
        self.nationality_combo.setMinimumWidth(300)

        # Add nationalities
        nationalities = get_all_nationalities()
        self.nationality_combo.addItems(nationalities)

        form_layout.addRow(QLabel("Nationality:", self), self.nationality_combo)

        # Add form to main layout
        main_layout.addWidget(form_widget)

        # Attribute section
        attribute_group = QGroupBox("Starting Attributes", self)
        attribute_group.setFont(theme_manager.get_military_font(14, bold=True))
        attribute_layout = QVBoxLayout(attribute_group)

        # Attribute explanation
        attr_explanation = QLabel(
            "Your character starts with all attributes at C (Average). "
            "You can improve some attributes by decreasing others, or roll randomly.",
            self
        )
        attr_explanation.setWordWrap(True)
        attribute_layout.addWidget(attr_explanation)

        # Attribute grid
        attr_widget = QWidget(self)
        attr_grid = QFormLayout(attr_widget)
        attr_grid.setSpacing(10)

        # Strength
        self.str_combo = QComboBox(self)
        self.str_combo.addItems(["A", "B", "C", "D"])
        self.str_combo.setCurrentText("C")
        self.str_combo.currentIndexChanged.connect(self._update_attribute_pool)
        attr_grid.addRow(QLabel("Strength (STR):", self), self.str_combo)

        # Agility
        self.agl_combo = QComboBox(self)
        self.agl_combo.addItems(["A", "B", "C", "D"])
        self.agl_combo.setCurrentText("C")
        self.agl_combo.currentIndexChanged.connect(self._update_attribute_pool)
        attr_grid.addRow(QLabel("Agility (AGL):", self), self.agl_combo)

        # Intelligence
        self.int_combo = QComboBox(self)
        self.int_combo.addItems(["A", "B", "C", "D"])
        self.int_combo.setCurrentText("C")
        self.int_combo.currentIndexChanged.connect(self._update_attribute_pool)
        attr_grid.addRow(QLabel("Intelligence (INT):", self), self.int_combo)

        # Empathy
        self.emp_combo = QComboBox(self)
        self.emp_combo.addItems(["A", "B", "C", "D"])
        self.emp_combo.setCurrentText("C")
        self.emp_combo.currentIndexChanged.connect(self._update_attribute_pool)
        attr_grid.addRow(QLabel("Empathy (EMP):", self), self.emp_combo)

        # Add attribute grid to attribute layout
        attribute_layout.addWidget(attr_widget)

        # Roll attributes button
        self.roll_attr_button = QPushButton("Roll Attributes", self)
        self.roll_attr_button.clicked.connect(self._roll_attributes)
        attribute_layout.addWidget(self.roll_attr_button)

        # Add attribute group to main layout
        main_layout.addWidget(attribute_group)

        # Points remaining
        self.points_label = QLabel("Points Remaining: 0", self)
        self.points_label.setFont(theme_manager.get_military_font(14, bold=True))
        self.points_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.points_label)

        # Buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(20)

        # Spacer on the left
        button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # Back button
        self.back_button = QPushButton("Back", self)
        self.back_button.setMinimumSize(QSize(120, 40))
        self.back_button.clicked.connect(self._on_back_clicked)
        button_layout.addWidget(self.back_button)

        # Next button
        self.next_button = QPushButton("Next", self)
        self.next_button.setMinimumSize(QSize(120, 40))
        self.next_button.clicked.connect(self._on_next_clicked)
        button_layout.addWidget(self.next_button)

        # Spacer on the right
        button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # Add buttons to main layout
        main_layout.addLayout(button_layout)

        # Add spacer at the bottom
        main_layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Initialize attributes
        self._update_attribute_pool()

    def _update_attribute_pool(self):
        """Update the attribute pool based on selected attributes"""
        # Calculate points used
        points_used = 0

        # A = +2 points, B = +1 point, C = 0 points, D = -1 point
        attr_values = {"A": 2, "B": 1, "C": 0, "D": -1}

        points_used += attr_values[self.str_combo.currentText()]
        points_used += attr_values[self.agl_combo.currentText()]
        points_used += attr_values[self.int_combo.currentText()]
        points_used += attr_values[self.emp_combo.currentText()]

        # Update points label
        self.points_label.setText(f"Points Used: {points_used}")

        # Enable/disable next button based on points
        self.next_button.setEnabled(points_used <= 0)

    def _roll_attributes(self):
        """Roll random attributes"""
        # Play sound
        audio_manager.play_sound("dice_roll")

        # Reset attributes to C
        self.str_combo.setCurrentText("C")
        self.agl_combo.setCurrentText("C")
        self.int_combo.setCurrentText("C")
        self.emp_combo.setCurrentText("C")

        # Roll 2D3-2 for number of attribute increases (0-4)
        num_increases = min(4, max(0, (self.dice_controller.roll_die(3) + self.dice_controller.roll_die(3) - 2)))

        # Apply random increases
        attributes = ["STR", "AGL", "INT", "EMP"]
        combos = {"STR": self.str_combo, "AGL": self.agl_combo, "INT": self.int_combo, "EMP": self.emp_combo}

        import random
        for _ in range(num_increases):
            # Select random attribute
            attr = random.choice(attributes)

            # Improve it if not already at A
            combo = combos[attr]
            current_level = combo.currentText()
            if current_level != "A":
                # Calculate new level (one step better)
                new_level = chr(ord(current_level) - 1)  # A is better than B
                combo.setCurrentText(new_level)

        # Update attribute pool
        self._update_attribute_pool()

    def _on_back_clicked(self):
        """Handle back button click"""
        # Play sound
        audio_manager.play_sound("button_click")

        # Go back to intro screen
        if self.parent:
            intro_screen = self.parent.stacked_widget.widget(0)  # Assuming intro screen is the first widget
            self.parent.stacked_widget.setCurrentWidget(intro_screen)

    def _on_next_clicked(self):
        """Handle next button click"""
        # Play sound
        audio_manager.play_sound("button_click")

        # Validate form
        if not self._validate_form():
            return

        # Save
        def _validate_form(self):
            """Validate the form

            Returns:
                True if valid, False otherwise
            """
            # Check if name is entered
            if not self.name_edit.text().strip():
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.warning(self, "Missing Information", "Please enter a character name.")
                return False

            # Check attribute points
            attr_values = {"A": 2, "B": 1, "C": 0, "D": -1}
            points_used = (attr_values[self.str_combo.currentText()] +
                           attr_values[self.agl_combo.currentText()] +
                           attr_values[self.int_combo.currentText()] +
                           attr_values[self.emp_combo.currentText()])

            if points_used > 0:
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.warning(self, "Invalid Attributes",
                                    "You've used too many attribute points. Please adjust your attributes.")
                return False

            # Save basic info
            game_controller.set_basic_info(
                self.name_edit.text().strip(),
                self.nationality_combo.currentText()
            )

            # Save attributes
            game_controller.set_attributes({
                "STR": self.str_combo.currentText(),
                "AGL": self.agl_combo.currentText(),
                "INT": self.int_combo.currentText(),
                "EMP": self.emp_combo.currentText()
            })

            # Calculate derived attributes
            game_controller.character.calculate_derived_attributes()

            # Proceed to childhood screen
            self._proceed_to_childhood()

            return True

        def _proceed_to_childhood(self):
            """Proceed to childhood selection screen"""
            # Create childhood screen
            childhood_screen = ChildhoodScreen(self.parent)

            # Navigate to childhood screen
            self.parent.navigate_to_screen(childhood_screen)

    class ChildhoodScreen(QWidget):
        """Screen for selecting childhood background"""

        def __init__(self, parent=None):
            super().__init__(parent)
            self.parent = parent
            self.dice_controller = DiceController()
            self._setup_ui()

        def _setup_ui(self):
            """Set up the user interface"""
            # Main layout
            main_layout = QVBoxLayout(self)
            main_layout.setContentsMargins(50, 50, 50, 50)
            main_layout.setSpacing(20)

            # Title
            title_label = QLabel("Childhood", self)
            title_label.setFont(theme_manager.get_military_font(24, bold=True))
            title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            main_layout.addWidget(title_label)

            # Description
            desc_label = QLabel(
                "Your character's childhood shaped their early skills and abilities. "
                "Choose a childhood background or roll randomly.",
                self
            )
            desc_label.setWordWrap(True)
            main_layout.addWidget(desc_label)

            # Scroll area for childhood options
            scroll_area = QScrollArea(self)
            scroll_area.setWidgetResizable(True)
            scroll_area.setFrameShape(QFrame.Shape.NoFrame)
            scroll_content = QWidget()
            scroll_layout = QVBoxLayout(scroll_content)
            scroll_layout.setSpacing(15)

            # Childhood options
            self.childhood_radios = []

            # Street Kid
            street_kid_group = QGroupBox("Street Kid", self)
            street_kid_layout = QVBoxLayout(street_kid_group)
            street_kid_desc = QLabel(
                "You grew up on the streets, learning to survive by your wits and quick reflexes. "
                "You know how to fight, how to run, and how to fade into the background when necessary.",
                self
            )
            street_kid_desc.setWordWrap(True)
            street_kid_layout.addWidget(street_kid_desc)

            street_kid_skills = QLabel("Skills: Close Combat, Mobility, Recon", self)
            street_kid_layout.addWidget(street_kid_skills)

            street_kid_specialties = QFormLayout()
            self.street_kid_specialty = QComboBox(self)
            self.street_kid_specialty.addItems(["Brawler", "Melee", "Runner", "Infiltrator", "Scrounger", "Locksmith"])
            street_kid_specialties.addRow("Specialty:", self.street_kid_specialty)
            street_kid_layout.addLayout(street_kid_specialties)

            street_kid_radio = QRadioButton("Select Street Kid", self)
            self.childhood_radios.append((street_kid_radio, "Street Kid", self.street_kid_specialty))
            street_kid_layout.addWidget(street_kid_radio)

            scroll_layout.addWidget(street_kid_group)

            # Small Town
            small_town_group = QGroupBox("Small Town", self)
            small_town_layout = QVBoxLayout(small_town_group)
            small_town_desc = QLabel(
                "You grew up in a small town, where everyone knew each other. "
                "You learned practical skills like driving, hunting, and basic survival.",
                self
            )
            small_town_desc.setWordWrap(True)
            small_town_layout.addWidget(small_town_desc)

            small_town_skills = QLabel("Skills: Driving, Ranged Combat, Survival", self)
            small_town_layout.addWidget(small_town_skills)

            small_town_specialties = QFormLayout()
            self.small_town_specialty = QComboBox(self)
            self.small_town_specialty.addItems(["Biker", "Racer", "Sniper", "Farmer", "Hunter", "Quartermaster"])
            small_town_specialties.addRow("Specialty:", self.small_town_specialty)
            small_town_layout.addLayout(small_town_specialties)

            small_town_radio = QRadioButton("Select Small Town", self)
            self.childhood_radios.append((small_town_radio, "Small Town", self.small_town_specialty))
            small_town_layout.addWidget(small_town_radio)

            scroll_layout.addWidget(small_town_group)

            # Working Class
            working_class_group = QGroupBox("Working Class", self)
            working_class_layout = QVBoxLayout(working_class_group)
            working_class_desc = QLabel(
                "You grew up in a working-class family, learning the value of hard work. "
                "You picked up practical skills and how to work with your hands.",
                self
            )
            working_class_desc.setWordWrap(True)
            working_class_layout.addWidget(working_class_desc)

            working_class_skills = QLabel("Skills: Close Combat, Stamina, Tech", self)
            working_class_layout.addWidget(working_class_skills)

            working_class_specialties = QFormLayout()
            self.working_class_specialty = QComboBox(self)
            self.working_class_specialty.addItems(
                ["Brawler", "Builder", "Load Carrier", "Scrounger", "Blacksmith", "Mechanic"])
            working_class_specialties.addRow("Specialty:", self.working_class_specialty)
            working_class_layout.addLayout(working_class_specialties)

            working_class_radio = QRadioButton("Select Working Class", self)
            self.childhood_radios.append((working_class_radio, "Working Class", self.working_class_specialty))
            working_class_layout.addWidget(working_class_radio)

            scroll_layout.addWidget(working_class_group)

            # Intellectual
            intellectual_group = QGroupBox("Intellectual", self)
            intellectual_layout = QVBoxLayout(intellectual_group)
            intellectual_desc = QLabel(
                "You grew up in an environment that valued education and intellect. "
                "You spent more time with books than with people, developing your mind.",
                self
            )
            intellectual_desc.setWordWrap(True)
            intellectual_layout.addWidget(intellectual_desc)

            intellectual_skills = QLabel("Skills: Tech, Medical Aid, Persuasion", self)
            intellectual_layout.addWidget(intellectual_skills)

            intellectual_specialties = QFormLayout()
            self.intellectual_specialty = QComboBox(self)
            self.intellectual_specialty.addItems(
                ["Historian", "Communications", "Computers", "Scientist", "Linguist", "Musician"])
            intellectual_specialties.addRow("Specialty:", self.intellectual_specialty)
            intellectual_layout.addLayout(intellectual_specialties)

            intellectual_radio = QRadioButton("Select Intellectual", self)
            self.childhood_radios.append((intellectual_radio, "Intellectual", self.intellectual_specialty))
            intellectual_layout.addWidget(intellectual_radio)

            scroll_layout.addWidget(intellectual_group)

            # Military Family
            military_family_group = QGroupBox("Military Family", self)
            military_family_layout = QVBoxLayout(military_family_group)
            military_family_desc = QLabel(
                "You grew up in a military family, moving from base to base. "
                "You learned discipline, physical fitness, and basic military skills.",
                self
            )
            military_family_desc.setWordWrap(True)
            military_family_layout.addWidget(military_family_desc)

            military_family_skills = QLabel("Skills: Stamina, Mobility, Ranged Combat", self)
            military_family_layout.addWidget(military_family_skills)

            military_family_specialties = QFormLayout()
            self.military_family_specialty = QComboBox(self)
            self.military_family_specialty.addItems(
                ["Brawler", "Martial Artist", "Ranger", "Mountaineer", "Runner", "Rifleman"])
            military_family_specialties.addRow("Specialty:", self.military_family_specialty)
            military_family_layout.addLayout(military_family_specialties)

            military_family_radio = QRadioButton("Select Military Family", self)
            self.childhood_radios.append((military_family_radio, "Military Family", self.military_family_specialty))
            military_family_layout.addWidget(military_family_radio)

            scroll_layout.addWidget(military_family_group)

            # Affluence
            affluence_group = QGroupBox("Affluence", self)
            affluence_layout = QVBoxLayout(affluence_group)
            affluence_desc = QLabel(
                "You grew up in a wealthy family, with access to resources and opportunities. "
                "You learned social skills, how to move in affluent circles, and how to get what you want.",
                self
            )
            affluence_desc.setWordWrap(True)
            affluence_layout.addWidget(affluence_desc)

            affluence_skills = QLabel("Skills: Mobility, Command, Persuasion", self)
            affluence_layout.addWidget(affluence_skills)

            affluence_specialties = QFormLayout()
            self.affluence_specialty = QComboBox(self)
            self.affluence_specialty.addItems(["Boatman", "Rider", "Runner", "Linguist", "Musician", "Trader"])
            affluence_specialties.addRow("Specialty:", self.affluence_specialty)
            affluence_layout.addLayout(affluence_specialties)

            affluence_radio = QRadioButton("Select Affluence", self)
            self.childhood_radios.append((affluence_radio, "Affluence", self.affluence_specialty))
            affluence_layout.addWidget(affluence_radio)

            scroll_layout.addWidget(affluence_group)

            # Add scroll content to scroll area
            scroll_area.setWidget(scroll_content)
            main_layout.addWidget(scroll_area)

            # Random roll button
            self.roll_button = QPushButton("Roll Random Childhood", self)
            self.roll_button.clicked.connect(self._roll_random_childhood)
            main_layout.addWidget(self.roll_button)

            # Buttons
            button_layout = QHBoxLayout()
            button_layout.setSpacing(20)

            # Spacer on the left
            button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

            # Back button
            self.back_button = QPushButton("Back", self)
            self.back_button.setMinimumSize(QSize(120, 40))
            self.back_button.clicked.connect(self._on_back_clicked)
            button_layout.addWidget(self.back_button)

            # Next button
            self.next_button = QPushButton("Next", self)
            self.next_button.setMinimumSize(QSize(120, 40))
            self.next_button.clicked.connect(self._on_next_clicked)
            button_layout.addWidget(self.next_button)

            # Spacer on the right
            button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

            # Add buttons to main layout
            main_layout.addLayout(button_layout)

        def _roll_random_childhood(self):
            """Roll a random childhood"""
            # Play sound
            audio_manager.play_sound("dice_roll")

            # Roll D6 for childhood
            roll = self.dice_controller.roll_d6()

            # Select the appropriate radio button based on roll
            self.childhood_radios[roll - 1][0].setChecked(True)

            # Roll for specialty
            specialty_combo = self.childhood_radios[roll - 1][2]
            specialty_roll = self.dice_controller.roll_d6() - 1  # 0-5 for combo box
            specialty_combo.setCurrentIndex(specialty_roll)

        def _on_back_clicked(self):
            """Handle back button click"""
            # Play sound
            audio_manager.play_sound("button_click")

            # Go back to basic info screen
            basic_info_screen = BasicInfoScreen(self.parent)
            self.parent.navigate_to_screen(basic_info_screen)

        def _on_next_clicked(self):
            """Handle next button click"""
            # Play sound
            audio_manager.play_sound("button_click")

            # Validate form
            if not self._validate_form():
                return

            # Proceed to career screen
            self._proceed_to_career()

        def _validate_form(self):
            """Validate the form

            Returns:
                True if valid, False otherwise
            """
            # Check if a childhood is selected
            selected_childhood = None
            selected_specialty = None

            for radio, childhood, specialty_combo in self.childhood_radios:
                if radio.isChecked():
                    selected_childhood = childhood
                    selected_specialty = specialty_combo.currentText()
                    break

            if not selected_childhood:
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.warning(self, "Missing Selection", "Please select a childhood background.")
                return False

            # Save childhood
            game_controller.character.childhood = selected_childhood
            game_controller.character.childhood_specialty = selected_specialty

            # Add basic skills based on childhood
            if selected_childhood == "Street Kid":
                game_controller.add_skills({"Close Combat": "D", "Mobility": "D", "Recon": "D"})
            elif selected_childhood == "Small Town":
                game_controller.add_skills({"Driving": "D", "Ranged Combat": "D", "Survival": "D"})
            elif selected_childhood == "Working Class":
                game_controller.add_skills({"Close Combat": "D", "Stamina": "D", "Tech": "D"})
            elif selected_childhood == "Intellectual":
                game_controller.add_skills({"Tech": "D", "Medical Aid": "D", "Persuasion": "D"})
            elif selected_childhood == "Military Family":
                game_controller.add_skills({"Stamina": "D", "Mobility": "D", "Ranged Combat": "D"})
            elif selected_childhood == "Affluence":
                game_controller.add_skills({"Mobility": "D", "Command": "D", "Persuasion": "D"})

            # Add specialty
            game_controller.add_specialty(selected_specialty)

            return True

        def _proceed_to_career(self):
            """Proceed to career selection screen"""
            # Create career screen
            career_screen = CareerSelectionScreen(self.parent)

            # Navigate to career screen
            self.parent.navigate_to_screen(career_screen)

    class CareerSelectionScreen(QWidget):
        """Screen for selecting a career path"""

        def __init__(self, parent=None):
            super().__init__(parent)
            self.parent = parent
            self.dice_controller = DiceController()
            self._setup_ui()

        def _setup_ui(self):
            """Set up the user interface"""
            # Main layout
            main_layout = QVBoxLayout(self)
            main_layout.setContentsMargins(50, 50, 50, 50)
            main_layout.setSpacing(20)

            # Title
            title_label = QLabel("Career Selection", self)
            title_label.setFont(theme_manager.get_military_font(24, bold=True))
            title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            main_layout.addWidget(title_label)

            # Description
            desc_label = QLabel(
                f"Your character is now {game_controller.character.age} years old. "
                "It's time to choose a career path. Each career lasts 6 years and provides "
                "skills, specialties, and possibly equipment.",
                self
            )
            desc_label.setWordWrap(True)
            main_layout.addWidget(desc_label)

            # Career type tabs
            from PyQt6.QtWidgets import QTabWidget

            self.career_tabs = QTabWidget(self)

            # Military tab
            military_tab = QWidget()
            military_layout = QVBoxLayout(military_tab)

            military_label = QLabel(
                "Military careers involve service in the armed forces. They provide "
                "combat skills, discipline, and structure.",
                self
            )
            military_label.setWordWrap(True)
            military_layout.addWidget(military_label)

            # Military careers
            military_careers_widget = QWidget()
            military_careers_layout = QVBoxLayout(military_careers_widget)

            self.military_radios = []

            # Combat Arms
            combat_arms_group = QGroupBox("Combat Arms", self)
            combat_arms_layout = QVBoxLayout(combat_arms_group)
            combat_arms_desc = QLabel(
                "The core combat units, focused on direct engagement with enemy forces. "
                "Requirements: STR B+, AGL B+",
                self
            )
            combat_arms_desc.setWordWrap(True)
            combat_arms_layout.addWidget(combat_arms_desc)

            combat_arms_skills = QLabel("Skills: Close Combat, Heavy Weapons, Ranged Combat, Recon", self)
            combat_arms_layout.addWidget(combat_arms_skills)

            combat_arms_specialties = QFormLayout()
            self.combat_arms_specialty = QComboBox(self)
            self.combat_arms_specialty.addItems([
                "Rifleman", "Redleg", "Tanker", "Machinegunner", "Launcher Crew", "Combat Engineer"
            ])
            combat_arms_specialties.addRow("Specialty:", self.combat_arms_specialty)
            combat_arms_layout.addLayout(combat_arms_specialties)

            combat_arms_radio = QRadioButton("Select Combat Arms", self)
            self.military_radios.append((combat_arms_radio, "Combat Arms", self.combat_arms_specialty))
            combat_arms_layout.addWidget(combat_arms_radio)

            military_careers_layout.addWidget(combat_arms_group)

            # Combat Support
            combat_support_group = QGroupBox("Combat Support", self)
            combat_support_layout = QVBoxLayout(combat_support_group)
            combat_support_desc = QLabel(
                "Units that provide direct support to combat units through intelligence, "
                "communications, and specialized functions. Requirements: INT B+",
                self
            )
            combat_support_desc.setWordWrap(True)
            combat_support_layout.addWidget(combat_support_desc)

            combat_support_skills = QLabel("Skills: Recon, Survival, Tech", self)
            combat_support_layout.addWidget(combat_support_skills)

            combat_support_specialties = QFormLayout()
            self.combat_support_specialty = QComboBox(self)
            self.combat_support_specialty.addItems([
                "Intelligence", "Linguist", "Communications", "NBC", "Computers", "Psy Ops"
            ])
            combat_support_specialties.addRow("Specialty:", self.combat_support_specialty)
            combat_support_layout.addLayout(combat_support_specialties)

            combat_support_radio = QRadioButton("Select Combat Support", self)
            self.military_radios.append((combat_support_radio, "Combat Support", self.combat_support_specialty))
            combat_support_layout.addWidget(combat_support_radio)

            military_careers_layout.addWidget(combat_support_group)

            # Add more military careers...

            # Scroll area for military careers
            military_scroll = QScrollArea()
            military_scroll.setWidgetResizable(True)
            military_scroll.setWidget(military_careers_widget)
            military_layout.addWidget(military_scroll)

            self.career_tabs.addTab(military_tab, "Military")

            # Add more career type tabs...

            # Add career tabs to main layout
            main_layout.addWidget(self.career_tabs)

            # Random roll button
            self.roll_button = QPushButton("Roll Random Career", self)
            self.roll_button.clicked.connect(self._roll_random_career)
            main_layout.addWidget(self.roll_button)

            # Buttons
            button_layout = QHBoxLayout()
            button_layout.setSpacing(20)

            # Spacer on the left
            button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

            # Back button
            self.back_button = QPushButton("Back", self)
            self.back_button.setMinimumSize(QSize(120, 40))
            self.back_button.clicked.connect(self._on_back_clicked)
            button_layout.addWidget(self.back_button)

            # Next button
            self.next_button = QPushButton("Next", self)
            self.next_button.setMinimumSize(QSize(120, 40))
            self.next_button.clicked.connect(self._on_next_clicked)
            button_layout.addWidget(self.next_button)

            # Spacer on the right
            button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

            # Add buttons to main layout
            main_layout.addLayout(button_layout)

        def _roll_random_career(self):
            """Roll a random career"""
            # Play sound
            audio_manager.play_sound("dice_roll")

            # For now, just roll a military career
            roll = self.dice_controller.roll_die(len(self.military_radios))

            # Select the tab
            self.career_tabs.setCurrentIndex(0)  # Military tab

            # Select the appropriate radio button based on roll
            self.military_radios[roll - 1][0].setChecked(True)

            # Roll for specialty
            specialty_combo = self.military_radios[roll - 1][2]
            specialty_count = specialty_combo.count()
            specialty_roll = self.dice_controller.roll_die(specialty_count) - 1  # 0-(count-1) for combo box
            specialty_combo.setCurrentIndex(specialty_roll)

        def _on_back_clicked(self):
            """Handle back button click"""
            # Play sound
            audio_manager.play_sound("button_click")

            # Go back to childhood screen
            childhood_screen = ChildhoodScreen(self.parent)
            self.parent.navigate_to_screen(childhood_screen)

        def _on_next_clicked(self):
            """Handle next button click"""
            # Play sound
            audio_manager.play_sound("button_click")

            # Validate form
            if not self._validate_form():
                return

            # Proceed to career events screen
            self._proceed_to_career_events()

        def _validate_form(self):
            """Validate the form

            Returns:
                True if valid, False otherwise
            """
            # Check which tab is active
            current_tab = self.career_tabs.currentIndex()

            # Check if a career is selected
            selected_career_type = None
            selected_career = None
            selected_specialty = None

            if current_tab == 0:  # Military
                for radio, career, specialty_combo in self.military_radios:
                    if radio.isChecked():
                        selected_career_type = "Military"
                        selected_career = career
                        selected_specialty = specialty_combo.currentText()
                        break
            # Add more tabs as needed

            if not selected_career:
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.warning(self, "Missing Selection", "Please select a career.")
                return False

            # Check if character meets requirements for the selected career
            if selected_career == "Combat Arms":
                str_level = game_controller.character.get_attribute_letter("STR")
                agl_level = game_controller.character.get_attribute_letter("AGL")

                if str_level not in ["A", "B"] or agl_level not in ["A", "B"]:
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(self, "Requirements Not Met",
                                        "Your character does not meet the requirements for Combat Arms (STR B+, AGL B+).")
                    return False
            elif selected_career == "Combat Support":
                int_level = game_controller.character.get_attribute_letter("INT")

                if int_level not in ["A", "B"]:
                    from PyQt6.QtWidgets import QMessageBox
                    QMessageBox.warning(self, "Requirements Not Met",
                                        "Your character does not meet the requirements for Combat Support (INT B+).")
                    return False

            # Add more requirement checks as needed

            # Save career
            game_controller.add_career(selected_career_type, selected_career)

            # Add specialty
            game_controller.add_specialty(selected_specialty)

            # Add skills based on career
            if selected_career == "Combat Arms":
                game_controller.add_skills({
                    "Close Combat": "D", "Heavy Weapons": "D", "Ranged Combat": "D", "Recon": "D"
                })
            elif selected_career == "Combat Support":
                game_controller.add_skills({"Recon": "D", "Survival": "D", "Tech": "D"})

            # Add more skill additions as needed

            return True

        def _proceed_to_career_events(self):
            """Proceed to career events screen"""
            # In a real implementation, you'd create a career events screen here

            # For now, just create a placeholder war screen
            war_screen = WarScreen(self.parent)

            # Navigate to war screen
            self.parent.navigate_to_screen(war_screen)

    class WarScreen(QWidget):
        """Screen for war experience"""

        def __init__(self, parent=None):
            super().__init__(parent)
            self.parent = parent
            self.dice_controller = DiceController()
            self._setup_ui()

        def _setup_ui(self):
            """Set up the user interface"""
            # Main layout
            main_layout = QVBoxLayout(self)
            main_layout.setContentsMargins(50, 50, 50, 50)
            main_layout.setSpacing(20)

            # Title
            title_label = QLabel("War Breaks Out", self)
            title_label.setFont(theme_manager.get_military_font(24, bold=True))
            title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            main_layout.addWidget(title_label)

            # Description
            desc_label = QLabel(
                f"The year is 2000. Your character is now {game_controller.character.age} years old. "
                "War has broken out across the globe. Nuclear exchanges have devastated major cities. "
                "Civilization is in ruins. What role did your character play during the war?",
                self
            )
            desc_label.setWordWrap(True)
            main_layout.addWidget(desc_label)

            # War role group
            role_group = QGroupBox("Your Role in the War", self)
            role_layout = QVBoxLayout(role_group)

            # Role buttons
            self.role_buttons = []

            # Military
            military_role = QRadioButton("Military Service", self)
            military_role.setChecked(True)
            role_layout.addWidget(military_role)

            military_desc = QLabel(
                "You served in the military during the war, either as a regular soldier "
                "or as part of a special unit.",
                self
            )
            military_desc.setWordWrap(True)
            role_layout.addWidget(military_desc)

            self.role_buttons.append((military_role, "Military Service"))

            # Local Militia
            militia_role = QRadioButton("Local Militia", self)
            role_layout.addWidget(militia_role)

            militia_desc = QLabel(
                "You joined or formed a local militia to defend your hometown "
                "or region from invaders and bandits.",
                self
            )
            militia_desc.setWordWrap(True)
            role_layout.addWidget(militia_desc)

            self.role_buttons.append((militia_role, "Local Militia"))

            # Civilian Survivor
            civilian_role = QRadioButton("Civilian Survivor", self)
            role_layout.addWidget(civilian_role)

            civilian_desc = QLabel(
                "You survived as a civilian, using your skills to stay alive "
                "and help others in a world gone mad.",
                self
            )
            civilian_desc.setWordWrap(True)
            role_layout.addWidget(civilian_desc)

            self.role_buttons.append((civilian_role, "Civilian Survivor"))

            # Add role group to main layout
            main_layout.addWidget(role_group)

            # Radiation section
            radiation_group = QGroupBox("Radiation Exposure", self)
            radiation_layout = QVBoxLayout(radiation_group)

            radiation_desc = QLabel(
                "Nuclear exchanges during the war have left radiation hotspots around the world. "
                "Roll to determine your character's level of radiation exposure.",
                self
            )
            radiation_desc.setWordWrap(True)
            radiation_layout.addWidget(radiation_desc)

            # Radiation level display
            self.radiation_label = QLabel("Current Radiation Points: 0", self)
            self.radiation_label.setFont(theme_manager.get_military_font(14, bold=True))
            radiation_layout.addWidget(self.radiation_label)

            # Radiation roll button
            self.radiation_button = QPushButton("Roll for Radiation Exposure", self)
            self.radiation_button.clicked.connect(self._roll_radiation)
            radiation_layout.addWidget(self.radiation_button)

            # Add radiation group to main layout
            main_layout.addWidget(radiation_group)

            # Buttons
            button_layout = QHBoxLayout()
            button_layout.setSpacing(20)

            # Spacer on the left
            button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

            # Back button
            self.back_button = QPushButton("Back", self)
            self.back_button.setMinimumSize(QSize(120, 40))
            self.back_button.clicked.connect(self._on_back_clicked)
            button_layout.addWidget(self.back_button)

            # Next button
            self.next_button = QPushButton("Next", self)
            self.next_button.setMinimumSize(QSize(120, 40))
            self.next_button.clicked.connect(self._on_next_clicked)
            button_layout.addWidget(self.next_button)

            # Spacer on the right
            button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

            # Add buttons to main layout
            main_layout.addLayout(button_layout)

        def _roll_radiation(self):
            """Roll for radiation exposure"""
            # Play sound
            audio_manager.play_sound("dice_roll")

            # Roll D6, subtract 1 (0-5 radiation points)
            roll = self.dice_controller.roll_d6()
            radiation = max(0, roll - 1)

            # Update label
            self.radiation_label.setText(f"Current Radiation Points: {radiation}")

            # Save radiation level
            game_controller.set_radiation(radiation)

        def _on_back_clicked(self):
            """Handle back button click"""
            # Play sound
            audio_manager.play_sound("button_click")

            # Go back to career selection screen
            career_screen = CareerSelectionScreen(self.parent)
            self.parent.navigate_to_screen(career_screen)

        def _on_next_clicked(self):
            """Handle next button click"""
            # Play sound
            audio_manager.play_sound("button_click")

            # Validate form
            if not self._validate_form():
                return

            # Proceed to character details screen
            self._proceed_to_character_details()

        def _validate_form(self):
            """Validate the form

            Returns:
                True if valid, False otherwise
            """
            # Check if radiation has been rolled
            if game_controller.character.radiation == 0 and not self.radiation_label.text().endswith("0"):
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.warning(self, "Missing Information",
                                    "Please roll for radiation exposure.")
                return False

            # Get selected war role
            selected_role = None
            for button, role in self.role_buttons:
                if button.isChecked():
                    selected_role = role
                    break

            # Save war experience
            game_controller.set_war_experience(selected_role)

            # Add skills based on war role
            if selected_role == "Military Service":
                # Improve two combat-related skills
                if "Ranged Combat" in game_controller.character.skills:
                    game_controller.improve_skill("Ranged Combat")
                else:
                    game_controller.add_skills({"Ranged Combat": "D"})

                if "Close Combat" in game_controller.character.skills:
                    game_controller.improve_skill("Close Combat")
                else:
                    game_controller.add_skills({"Close Combat": "D"})

            elif selected_role == "Local Militia":
                # Improve local knowledge and survival
                if "Survival" in game_controller.character.skills:
                    game_controller.improve_skill("Survival")
                else:
                    game_controller.add_skills({"Survival": "D"})

                if "Recon" in game_controller.character.skills:
                    game_controller.improve_skill("Recon")
                else:
                    game_controller.add_skills({"Recon": "D"})

            elif selected_role == "Civilian Survivor":
                # Improve scrounging and first aid
                if "Tech" in game_controller.character.skills:
                    game_controller.improve_skill("Tech")
                else:
                    game_controller.add_skills({"Tech": "D"})

                if "Medical Aid" in game_controller.character.skills:
                    game_controller.improve_skill("Medical Aid")
                else:
                    game_controller.add_skills({"Medical Aid": "D"})

            return True

        def _proceed_to_character_details(self):
            """Proceed to character details screen"""
            # Create character details screen
            details_screen = CharacterDetailsScreen(self.parent)

            # Navigate to details screen
            self.parent.navigate_to_screen(details_screen)

        class CharacterDetailsScreen(QWidget):
            """Screen for final character details"""

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

                # Title
                title_label = QLabel("Character Details", self)
                title_label.setFont(theme_manager.get_military_font(24, bold=True))
                title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                main_layout.addWidget(title_label)

                # Scroll area for the form
                scroll_widget = QWidget()
                scroll_layout = QVBoxLayout(scroll_widget)

                # Form layout
                form_layout = QFormLayout()
                form_layout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapLongRows)
                form_layout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.ExpandingFieldsGrow)

                # Moral Code
                moral_code_label = QLabel("Moral Code:", self)
                self.moral_code_edit = QLineEdit(self)
                self.moral_code_edit.setPlaceholderText("e.g., 'I will always protect the innocent'")
                form_layout.addRow(moral_code_label, self.moral_code_edit)

                # Big Dream
                big_dream_label = QLabel("Big Dream:", self)
                self.big_dream_edit = QLineEdit(self)
                self.big_dream_edit.setPlaceholderText("e.g., 'Find a safe place to settle down'")
                form_layout.addRow(big_dream_label, self.big_dream_edit)

                # Buddy
                buddy_label = QLabel("Buddy:", self)
                self.buddy_edit = QLineEdit(self)
                self.buddy_edit.setPlaceholderText("The PC you feel closest to")
                form_layout.addRow(buddy_label, self.buddy_edit)

                # How You Met
                how_met_label = QLabel("How You Met:", self)
                self.how_met_edit = QLineEdit(self)
                self.how_met_edit.setPlaceholderText("How you met the other PCs")
                form_layout.addRow(how_met_label, self.how_met_edit)

                # Appearance
                appearance_label = QLabel("Appearance:", self)
                self.appearance_edit = QLineEdit(self)
                self.appearance_edit.setPlaceholderText("Brief description of your character's appearance")
                form_layout.addRow(appearance_label, self.appearance_edit)

                # Add form to scroll layout
                scroll_layout.addLayout(form_layout)

                # Gear section
                gear_group = QGroupBox("Starting Gear", self)
                gear_layout = QVBoxLayout(gear_group)

                gear_desc = QLabel(
                    "Your character starts with gear based on their nationality, career, and skills. "
                    "This is just a starting point - you'll acquire more gear during play.",
                    self
                )
                gear_desc.setWordWrap(True)
                gear_layout.addWidget(gear_desc)

                # Gear list
                from PyQt6.QtWidgets import QTextEdit

                self.gear_text = QTextEdit(self)
                self.gear_text.setReadOnly(True)

                # Populate gear based on character
                gear_text = self._generate_gear_text()
                self.gear_text.setText(gear_text)

                gear_layout.addWidget(self.gear_text)

                # Add gear section to scroll layout
                scroll_layout.addWidget(gear_group)

                # Create scroll area
                scroll_area = QScrollArea(self)
                scroll_area.setWidgetResizable(True)
                scroll_area.setWidget(scroll_widget)

                # Add scroll area to main layout
                main_layout.addWidget(scroll_area)

                # Buttons
                button_layout = QHBoxLayout()
                button_layout.setSpacing(20)

                # Spacer on the left
                button_layout.addSpacerItem(
                    QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

                # Back button
                self.back_button = QPushButton("Back", self)
                self.back_button.setMinimumSize(QSize(120, 40))
                self.back_button.clicked.connect(self._on_back_clicked)
                button_layout.addWidget(self.back_button)

                # Complete button
                self.complete_button = QPushButton("Complete Character", self)
                self.complete_button.setMinimumSize(QSize(150, 40))
                self.complete_button.clicked.connect(self._on_complete_clicked)
                button_layout.addWidget(self.complete_button)

                # Spacer on the right
                button_layout.addSpacerItem(
                    QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

                # Add buttons to main layout
                main_layout.addLayout(button_layout)

            def _generate_gear_text(self):
                """Generate text listing the character's starting gear

                Returns:
                    String with gear list
                """
                gear = []

                character = game_controller.character

                # Add nationality-based gear
                nationality = character.nationality

                # Determine if military or civilian gear
                is_military = False
                for career in character.careers:
                    if career.get("type") == "Military":
                        is_military = True
                        break

                # Add nationality gear
                from src.data.nationalities import get_nationality_gear
                nationality_gear = get_nationality_gear(nationality, is_military)
                gear.extend(nationality_gear)

                # Add career-based gear
                if character.careers:
                    latest_career = character.careers[-1]
                    career_type = latest_career.get("type")
                    career_branch = latest_career.get("branch")

                    # This would use actual gear data in a real implementation
                    if career_type == "Military":
                        if career_branch == "Combat Arms":
                            gear.extend([
                                "Assault rifle",
                                "D6 reloads",
                                "Flak jacket and helmet",
                                "Knife or D6 hand grenades",
                                "Personal medkit",
                                "Backpack"
                            ])
                        elif career_branch == "Combat Support":
                            gear.extend([
                                "Assault rifle",
                                "D6 reloads",
                                "Flak jacket and helmet",
                                "Knife or D6 hand grenades",
                                "MOPP suit or manpack radio",
                                "Personal medkit",
                                "Backpack"
                            ])
                    # Add more career-specific gear

                # Add basic survival gear
                gear.extend([
                    "D6 rations of food",
                    "D6 rations of clean water",
                    "Basic toolkit"
                ])

                return "\n".join(gear)

            def _on_back_clicked(self):
                """Handle back button click"""
                # Play sound
                audio_manager.play_sound("button_click")

                # Go back to war screen
                war_screen = WarScreen(self.parent)
                self.parent.navigate_to_screen(war_screen)

            def _on_complete_clicked(self):
                """Handle complete button click"""
                # Play sound
                audio_manager.play_sound("button_click")

                # Validate and save details
                if not self._validate_form():
                    return

                # Complete character creation
                game_controller.complete_character()

                # Proceed to character sheet
                self._proceed_to_character_sheet()

            def _validate_form(self):
                """Validate the form

                Returns:
                    True if valid, False otherwise
                """
                # All fields are optional, but encourage filling them out
                if (not self.moral_code_edit.text().strip() or
                        not self.big_dream_edit.text().strip() or
                        not self.buddy_edit.text().strip() or
                        not self.how_met_edit.text().strip() or
                        not self.appearance_edit.text().strip()):

                    from PyQt6.QtWidgets import QMessageBox
                    result = QMessageBox.question(
                        self,
                        "Incomplete Details",
                        "Some character details are missing. Would you like to fill them in before continuing?",
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                    )

                    if result == QMessageBox.StandardButton.Yes:
                        return False

                # Save details
                game_controller.set_character_details(
                    self.moral_code_edit.text().strip(),
                    self.big_dream_edit.text().strip(),
                    self.buddy_edit.text().strip(),
                    self.how_met_edit.text().strip(),
                    self.appearance_edit.text().strip()
                )

                return True

            def _proceed_to_character_sheet(self):
                """Proceed to character sheet screen"""
                # Create character sheet screen
                sheet_screen = CharacterSheetScreen(self.parent)

                # Navigate to sheet screen
                self.parent.navigate_to_screen(sheet_screen)

        class CharacterSheetScreen(QWidget):
            """Screen for displaying the final character sheet"""

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

                # Title
                title_label = QLabel(f"Character Sheet: {game_controller.character.name}", self)
                title_label.setFont(theme_manager.get_military_font(24, bold=True))
                title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                main_layout.addWidget(title_label)

                # Scroll area for the sheet
                scroll_widget = QWidget()
                scroll_layout = QVBoxLayout(scroll_widget)

                # Basic info section
                basic_group = QGroupBox("Basic Information", self)
                basic_layout = QFormLayout(basic_group)

                name_label = QLabel(f"Name: {game_controller.character.name}", self)
                basic_layout.addRow(name_label)

                nationality_label = QLabel(f"Nationality: {game_controller.character.nationality}", self)
                basic_layout.addRow(nationality_label)

                age_label = QLabel(f"Age: {game_controller.character.age}", self)
                basic_layout.addRow(age_label)

                appearance_label = QLabel(f"Appearance: {game_controller.character.appearance}", self)
                appearance_label.setWordWrap(True)
                basic_layout.addRow(appearance_label)

                scroll_layout.addWidget(basic_group)

                # Attributes section
                attr_group = QGroupBox("Attributes", self)
                attr_layout = QFormLayout(attr_group)

                str_label = QLabel(
                    f"Strength (STR): {game_controller.character.get_attribute_letter('STR')} ({game_controller.character.get_attribute_die('STR')})",
                    self)
                attr_layout.addRow(str_label)

                agl_label = QLabel(
                    f"Agility (AGL): {game_controller.character.get_attribute_letter('AGL')} ({game_controller.character.get_attribute_die('AGL')})",
                    self)
                attr_layout.addRow(agl_label)

                int_label = QLabel(
                    f"Intelligence (INT): {game_controller.character.get_attribute_letter('INT')} ({game_controller.character.get_attribute_die('INT')})",
                    self)
                attr_layout.addRow(int_label)

                emp_label = QLabel(
                    f"Empathy (EMP): {game_controller.character.get_attribute_letter('EMP')} ({game_controller.character.get_attribute_die('EMP')})",
                    self)
                attr_layout.addRow(emp_label)

                hit_label = QLabel(f"Hit Capacity: {game_controller.character.hit_capacity}", self)
                attr_layout.addRow(hit_label)

                stress_label = QLabel(f"Stress Capacity: {game_controller.character.stress_capacity}", self)
                attr_layout.addRow(stress_label)

                cuf_label = QLabel(f"Coolness Under Fire (CUF): {game_controller.character.cuf}", self)
                attr_layout.addRow(cuf_label)

                scroll_layout.addWidget(attr_group)

                # Skills section
                skills_group = QGroupBox("Skills", self)
                skills_layout = QVBoxLayout(skills_group)

                # Create a table-like display for skills
                from PyQt6.QtWidgets import QGridLayout

                skills_grid = QGridLayout()
                skills_grid.addWidget(QLabel("Skill", self), 0, 0, Qt.AlignmentFlag.AlignLeft)
                skills_grid.addWidget(QLabel("Level", self), 0, 1, Qt.AlignmentFlag.AlignCenter)
                skills_grid.addWidget(QLabel("Die", self), 0, 2, Qt.AlignmentFlag.AlignRight)

                # Add skills to grid
                row = 1
                for skill, level in game_controller.character.skills.items():
                    skills_grid.addWidget(QLabel(skill, self), row, 0, Qt.AlignmentFlag.AlignLeft)
                    skills_grid.addWidget(QLabel(level, self), row, 1, Qt.AlignmentFlag.AlignCenter)

                    # Calculate die based on level
                    if level == "A":
                        die = "D12"
                    elif level == "B":
                        die = "D10"
                    elif level == "C":
                        die = "D8"
                    elif level == "D":
                        die = "D6"
                    else:
                        die = "None"

                    skills_grid.addWidget(QLabel(die, self), row, 2, Qt.AlignmentFlag.AlignRight)
                    row += 1

                skills_layout.addLayout(skills_grid)

                scroll_layout.addWidget(skills_group)

                # Specialties section
                specialties_group = QGroupBox("Specialties", self)
                specialties_layout = QVBoxLayout(specialties_group)

                specialties_text = ", ".join(s for s, has in game_controller.character.specialties.items() if has)
                specialties_label = QLabel(specialties_text, self)
                specialties_label.setWordWrap(True)
                specialties_layout.addWidget(specialties_label)

                scroll_layout.addWidget(specialties_group)

                # Background section
                background_group = QGroupBox("Background", self)
                background_layout = QVBoxLayout(background_group)

                childhood_label = QLabel(f"Childhood: {game_controller.character.childhood}", self)
                background_layout.addWidget(childhood_label)

                childhood_specialty_label = QLabel(
                    f"Childhood Specialty: {game_controller.character.childhood_specialty}", self)
                background_layout.addWidget(childhood_specialty_label)

                # Career history
                career_label = QLabel("Career History:", self)
                career_label.setFont(theme_manager.get_military_font(12, bold=True))
                background_layout.addWidget(career_label)

                for career in game_controller.character.careers:
                    age = career["age"]
                    term = f"Age {age}-{age + 5}: {career['type']}"
                    if career["branch"]:
                        term += f" - {career['branch']}"
                    if career["rank"]:
                        term += f" ({career['rank']})"
                    if career["promotion"]:
                        term += " [Promoted]"

                    career_term_label = QLabel(term, self)
                    background_layout.addWidget(career_term_label)

                war_text = "Yes - " + game_controller.character.at_war_career if game_controller.character.war_experience else "No"
                war_label = QLabel(f"War Experience: {war_text}", self)
                background_layout.addWidget(war_label)

                scroll_layout.addWidget(background_group)

                # Character details section
                details_group = QGroupBox("Character Details", self)
                details_layout = QFormLayout(details_group)

                moral_code_label = QLabel(game_controller.character.moral_code, self)
                moral_code_label.setWordWrap(True)
                details_layout.addRow("Moral Code:", moral_code_label)

                big_dream_label = QLabel(game_controller.character.big_dream, self)
                big_dream_label.setWordWrap(True)
                details_layout.addRow("Big Dream:", big_dream_label)

                buddy_label = QLabel(game_controller.character.buddy, self)
                buddy_label.setWordWrap(True)
                details_layout.addRow("Buddy:", buddy_label)

                how_met_label = QLabel(game_controller.character.how_you_met, self)
                how_met_label.setWordWrap(True)
                details_layout.addRow("How You Met:", how_met_label)

                scroll_layout.addWidget(details_group)

                # Gear section
                gear_group = QGroupBox("Gear", self)
                gear_layout = QVBoxLayout(gear_group)

                # For now, just list gear as a placeholder
                gear_text = QLabel("Standard gear based on nationality and career", self)
                gear_text.setWordWrap(True)
                gear_layout.addWidget(gear_text)

                scroll_layout.addWidget(gear_group)

                # Radiation section
                radiation_group = QGroupBox("Radiation", self)
                radiation_layout = QVBoxLayout(radiation_group)

                radiation_label = QLabel(f"Permanent Radiation Points: {game_controller.character.radiation}", self)
                radiation_layout.addWidget(radiation_label)

                scroll_layout.addWidget(radiation_group)

                # Create scroll area
                scroll_area = QScrollArea(self)
                scroll_area.setWidgetResizable(True)
                scroll_area.setWidget(scroll_widget)

                # Add scroll area to main layout
                main_layout.addWidget(scroll_area)

                # Buttons
                button_layout = QHBoxLayout()
                button_layout.setSpacing(20)

                # Save PDF button
                self.save_pdf_button = QPushButton("Export to PDF", self)
                self.save_pdf_button.clicked.connect(self._on_save_pdf_clicked)
                button_layout.addWidget(self.save_pdf_button)

                # Save JSON button
                self.save_json_button = QPushButton("Save Character", self)
                self.save_json_button.clicked.connect(self._on_save_json_clicked)
                button_layout.addWidget(self.save_json_button)

                # New character button
                self.new_button = QPushButton("Create New Character", self)
                self.new_button.clicked.connect(self._on_new_clicked)
                button_layout.addWidget(self.new_button)

                # Add buttons to main layout
                main_layout.addLayout(button_layout)

            def _on_save_pdf_clicked(self):
                """Handle save PDF button click"""
                # Play sound
                audio_manager.play_sound("button_click")

                # Show file dialog
                from PyQt6.QtWidgets import QFileDialog

                file_path, _ = QFileDialog.getSaveFileName(self, "Export to PDF", "",
                                                           "PDF Files (*.pdf);;All Files (*)")

                if file_path:
                    # Export to PDF
                    if game_controller.export_to_pdf(file_path):
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.information(self, "Success", "Character exported to PDF successfully.")
                    else:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(self, "Error", "Failed to export character to PDF.")

            def _on_save_json_clicked(self):
                """Handle save JSON button click"""
                # Play sound
                audio_manager.play_sound("button_click")

                # Show file dialog
                from PyQt6.QtWidgets import QFileDialog

                file_path, _ = QFileDialog.getSaveFileName(self, "Save Character", "",
                                                           "Character Files (*.json);;All Files (*)")

                if file_path:
                    # Save character
                    if game_controller.save_character(file_path):
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.information(self, "Success", "Character saved successfully.")
                    else:
                        from PyQt6.QtWidgets import QMessageBox
                        QMessageBox.warning(self, "Error", "Failed to save character.")

            def _on_new_clicked(self):
                """Handle new character button click"""
                # Play sound
                audio_manager.play_sound("button_click")

                # Confirm creation of new character
                from PyQt6.QtWidgets import QMessageBox

                result = QMessageBox.question(
                    self,
                    "Create New Character",
                    "Are you sure you want to create a new character? Any unsaved changes to the current character will be lost.",
                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
                )

                if result == QMessageBox.StandardButton.Yes:
                    # Reset game controller
                    game_controller.reset()

                    # Navigate back to intro screen
                    if self.parent:
                        intro_screen = self.parent.stacked_widget.widget(0)  # Assuming intro screen is the first widget
                        intro_screen.restart()  # Restart the intro sequence
                        self.parent.stacked_widget.setCurrentWidget(intro_screen)