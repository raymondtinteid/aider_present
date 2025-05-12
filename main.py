#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Optional
from person import Person  # Import Person from person.py


@dataclass
class Programmer(Person):
    """
    A dataclass representing a programmer, inheriting from Person.

    :param name: The programmer's full name
    :param age: The programmer's age in years
    :param email: The programmer's email address
    :param languages: List of programming languages the programmer knows
    :param skills: List of skills the programmer has
    :param address: The programmer's address
    """
    languages: List[str] = None

    def __post_init__(self):
        """Initialize default values after the main initialization."""
        super().__post_init__()
        if self.languages is None:
            self.languages = []

    def add_language(self, language: str) -> None:
        """
        Add a new programming language to the programmer's languages list.

        :param language: The programming language to add
        :return: None
        """
        self.languages.append(language)


@dataclass
class Boss(Person):
    """
    A dataclass representing a boss, inheriting from Person.

    :param name: The boss's full name
    :param age: The boss's age in years
    :param email: The boss's email address
    :param skills: List of skills the boss has
    :param address: The boss's address
    :param language: The boss's primary language (default: 'powerpoint')
    """
    language: str = "powerpoint"

    def __post_init__(self):
        """Initialize default values after the main initialization."""
        super().__post_init__()


def main():
    """Main function to demonstrate the Person, Programmer, and Boss dataclasses."""
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

    # Add a programmer instance
    programmer = Programmer(
        name="John Smith",
        age=32,
        email="john.smith@example.com",
        skills=["Problem Solving", "Algorithms"],
        languages=["Python", "Java"]
    )
    programmer.add_skill("System Design")
    programmer.add_language("C++")
    print(f"Programmer: {programmer}")
    print(f"Skills: {', '.join(programmer.skills)}")
    print(f"Languages: {', '.join(programmer.languages)}")

    # Add a boss instance
    boss = Boss(
        name="Bob Bossman",
        age=45,
        email="bob.bossman@example.com",
        skills=["Leadership", "Strategy"]
    )
    boss.add_skill("Vision")
    print(f"Boss: {boss}")
    print(f"Skills: {', '.join(boss.skills)}")
    print(f"Language: {boss.language}")
    
    return 1


if __name__ == "__main__":
    main()
