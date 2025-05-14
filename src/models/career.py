"""
career.py - Career model for Twilight 2000 character creator
"""


class Career:
    """Model for a character career"""

    def __init__(self, career_type=None, branch=None, rank=None, specialty=None, promotion=False, start_age=None):
        """Initialize a new career

        Args:
            career_type: Type of career (e.g., "Military", "Civilian")
            branch: Branch or specific career (e.g., "Army", "Police")
            rank: Military rank or position
            specialty: Career specialty
            promotion: Whether character was promoted during this career
            start_age: Age when starting this career
        """
        self.career_type = career_type
        self.branch = branch
        self.rank = rank
        self.specialty = specialty
        self.promotion = promotion
        self.start_age = start_age
        self.skills_gained = []  # List of skills gained during this career
        self.duration = 6  # Default duration is 6 years

    def add_skill(self, skill, level):
        """Add a skill gained during this career

        Args:
            skill: Skill name
            level: Skill level (A, B, C, D or F)
        """
        self.skills_gained.append({
            "skill": skill,
            "level": level
        })

    def set_promotion(self, new_rank=None):
        """Set promotion status

        Args:
            new_rank: New rank after promotion
        """
        self.promotion = True
        if new_rank:
            self.rank = new_rank

    def get_duration(self):
        """Get career duration in years

        Returns:
            Number of years
        """
        return self.duration

    def set_duration(self, years):
        """Set career duration

        Args:
            years: Duration in years
        """
        self.duration = years

    def get_end_age(self):
        """Get age at the end of this career

        Returns:
            End age or None if start age not set
        """
        if self.start_age is None:
            return None

        return self.start_age + self.duration

    def is_military(self):
        """Check if this is a military career

        Returns:
            True if military, False otherwise
        """
        return self.career_type == "Military"

    def is_law_enforcement(self):
        """Check if this is a law enforcement career

        Returns:
            True if law enforcement, False otherwise
        """
        return self.career_type == "Police"

    def to_dict(self):
        """Convert career to dictionary for saving

        Returns:
            Dictionary representation of the career
        """
        return {
            "career_type": self.career_type,
            "branch": self.branch,
            "rank": self.rank,
            "specialty": self.specialty,
            "promotion": self.promotion,
            "start_age": self.start_age,
            "skills_gained": self.skills_gained,
            "duration": self.duration
        }

    @classmethod
    def from_dict(cls, data):
        """Create career from dictionary

        Args:
            data: Dictionary with career data

        Returns:
            Career object
        """
        career = cls(
            career_type=data.get("career_type"),
            branch=data.get("branch"),
            rank=data.get("rank"),
            specialty=data.get("specialty"),
            promotion=data.get("promotion", False),
            start_age=data.get("start_age")
        )

        # Set duration
        career.duration = data.get("duration", 6)

        # Add skills
        for skill_data in data.get("skills_gained", []):
            career.add_skill(skill_data["skill"], skill_data["level"])

        return career

    def describe(self):
        """Get a text description of the career

        Returns:
            Text description
        """
        description = ""

        if self.start_age is not None:
            description += f"Age {self.start_age}-{self.get_end_age()}: "

        description += f"{self.career_type}"

        if self.branch:
            description += f" - {self.branch}"

        if self.rank:
            description += f" ({self.rank})"

        if self.specialty:
            description += f", specializing in {self.specialty}"

        if self.promotion:
            description += " [Promoted]"

        if self.skills_gained:
            skills_text = ", ".join([f"{s['skill']} ({s['level']})" for s in self.skills_gained])
            description += f"\nSkills gained: {skills_text}"

        return description