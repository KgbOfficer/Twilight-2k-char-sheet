"""
dice_controller.py - Dice rolling controller
"""

import random


class DiceController:
    """Controller for rolling dice"""

    def __init__(self):
        """Initialize the dice controller"""
        # Seed the random number generator
        random.seed()

    def roll_d6(self):
        """Roll a six-sided die

        Returns:
            Random number from 1 to 6
        """
        return random.randint(1, 6)

    def roll_2d6(self):
        """Roll two six-sided dice

        Returns:
            Sum of two random numbers from 1 to 6
        """
        return self.roll_d6() + self.roll_d6()

    def roll_die(self, size):
        """Roll a die of the specified size

        Args:
            size: Number of sides on the die

        Returns:
            Random number from 1 to size
        """
        return random.randint(1, size)

    def roll_attribute_die(self, attribute_level):
        """Roll a die based on attribute level

        Args:
            attribute_level: Attribute level (A, B, C, or D)

        Returns:
            Random number from the appropriate die (D12, D10, D8, or D6)
        """
        # Map attribute levels to die sizes
        die_sizes = {
            "A": 12,  # D12
            "B": 10,  # D10
            "C": 8,  # D8
            "D": 6  # D6
        }

        # Get the die size for the attribute level
        die_size = die_sizes.get(attribute_level, 8)  # Default to D8 if level not found

        # Roll the die
        return self.roll_die(die_size)

    def roll_skill_die(self, skill_level):
        """Roll a die based on skill level

        Args:
            skill_level: Skill level (A, B, C, D, or F)

        Returns:
            Random number from the appropriate die (D12, D10, D8, D6, or 0)
        """
        # Map skill levels to die sizes
        die_sizes = {
            "A": 12,  # D12
            "B": 10,  # D10
            "C": 8,  # D8
            "D": 6,  # D6
            "F": 0  # No die
        }

        # Get the die size for the skill level
        die_size = die_sizes.get(skill_level, 0)  # Default to 0 if level not found

        # Return 0 for level F (untrained)
        if die_size == 0:
            return 0

        # Roll the die
        return self.roll_die(die_size)

    def roll_skill_check(self, attribute_level, skill_level):
        """Roll a skill check using an attribute and skill

        Args:
            attribute_level: Attribute level (A, B, C, or D)
            skill_level: Skill level (A, B, C, D, or F)

        Returns:
            Tuple of (attribute roll, skill roll, total)
        """
        # Roll the attribute die
        attribute_roll = self.roll_attribute_die(attribute_level)

        # Roll the skill die
        skill_roll = self.roll_skill_die(skill_level)

        # Calculate total
        total = attribute_roll + skill_roll

        return (attribute_roll, skill_roll, total)

    def roll_career_path(self):
        """Roll for a random career path based on 2D6

        Returns:
            Integer from 2 to 12
        """
        return self.roll_2d6()

    def roll_for_promotion(self):
        """Roll for a promotion check

        Returns:
            Boolean indicating success
        """
        # Promotion on 6 or higher on D6
        return self.roll_d6() >= 6

    def roll_for_war(self):
        """Roll to check if war breaks out

        Returns:
            Boolean indicating if war breaks out
        """
        # War breaks out on 7 or lower on 2D6
        return self.roll_2d6() <= 7

    def roll_for_radiation(self):
        """Roll for starting radiation exposure

        Returns:
            Integer from 0 to 5 representing radiation points
        """
        # Roll D6, subtract 1 (0-5 radiation points)
        return max(0, self.roll_d6() - 1)