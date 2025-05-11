import unittest
from main import Person

class TestPerson(unittest.TestCase):
    """
    Unit tests for the Person dataclass.
    """

    def test_person_initialization(self):
        """
        Test that a Person object is initialized with the correct attributes.
        """
        person = Person(
            name="Alice Smith",
            age=30,
            email="alice@example.com",
            skills=["Python", "C++"],
            address="123 Main St"
        )
        self.assertEqual(person.name, "Alice Smith")
        self.assertEqual(person.age, 30)
        self.assertEqual(person.email, "alice@example.com")
        self.assertEqual(person.skills, ["Python", "C++"])
        self.assertEqual(person.address, "123 Main St")

    def test_person_skills_default(self):
        """
        Test that the skills list is initialized as empty if not provided.
        """
        person = Person(
            name="Bob Jones",
            age=25,
            email="bob@example.com"
        )
        self.assertEqual(person.skills, [])

    def test_add_skill(self):
        """
        Test that add_skill correctly adds a skill to the skills list.
        """
        person = Person(
            name="Charlie Brown",
            age=40,
            email="charlie@example.com",
            skills=[]
        )
        person.add_skill("Go")
        self.assertIn("Go", person.skills)
        self.assertEqual(len(person.skills), 1)

    def test_add_skill_multiple(self):
        """
        Test adding multiple skills to the skills list.
        """
        person = Person(
            name="Dana White",
            age=35,
            email="dana@example.com"
        )
        person.add_skill("Java")
        person.add_skill("Rust")
        self.assertEqual(person.skills, ["Java", "Rust"])

if __name__ == "__main__":
    unittest.main()
