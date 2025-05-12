from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Person:
    """
    A dataclass representing a person.
    
    :param name: The person's full name
    :param age: The person's age in years
    :param email: The person's email address
    :param skills: List of skills the person has
    """
    name: str
    age: int
    email: str
    skills: List[str] = None
    address: Optional[str] = None
    
    def __post_init__(self):
        """Initialize default values after the main initialization."""
        if self.skills is None:
            self.skills = []
    
    def add_skill(self, skill: str) -> None:
        """
        Add a new skill to the person's skill list.
        
        :param skill: The skill to add
        :return: None
        """
        self.skills.append(skill)
