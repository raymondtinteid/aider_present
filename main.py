#!/usr/bin/env python3

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


def main():
    """Main function to demonstrate the Person dataclass."""
    # Create a person instance
    developer = Person(
        name="Jane Doe",
        age=28,
        email="jane.doe@example.com",
        skills=["Python", "JavaScript"]
    )
    
    # Add a new skill
    developer.add_skill("Data Science")
    
    # Print the person details
    print(f"Developer: {developer}")
    print(f"Skills: {', '.join(developer.skills)}")
    
    # Add another person instance
    manager = Person(
        name="Alice Smith",
        age=35,
        email="alice.smith@example.com",
        skills=["Management", "Communication"]
    )
    manager.add_skill("Leadership")
    print(f"Manager: {manager}")
    print(f"Skills: {', '.join(manager.skills)}")
    
    return 1


if __name__ == "__main__":
    main()
