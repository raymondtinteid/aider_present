import unittest
from main import Programmer

class TestProgrammer(unittest.TestCase):
    """
    Unit tests for the Programmer dataclass.
    """

    def test_programmer_initialization(self):
        """
        Test that a Programmer object is initialized with the correct attributes.
        """
        programmer = Programmer(
            name="Alex Johnson",
            age=28,
            email="alex@example.com",
            skills=["Problem Solving", "Algorithms"],
            languages=["Python", "Java", "C++"],
            address="456 Tech Ave"
        )
        self.assertEqual(programmer.name, "Alex Johnson")
        self.assertEqual(programmer.age, 28)
        self.assertEqual(programmer.email, "alex@example.com")
        self.assertEqual(programmer.skills, ["Problem Solving", "Algorithms"])
        self.assertEqual(programmer.languages, ["Python", "Java", "C++"])
        self.assertEqual(programmer.address, "456 Tech Ave")

    def test_programmer_languages_default(self):
        """
        Test that the languages list is initialized as empty if not provided.
        """
        programmer = Programmer(
            name="Sam Wilson",
            age=32,
            email="sam@example.com"
        )
        self.assertEqual(programmer.languages, [])
        self.assertEqual(programmer.skills, [])  # Inherited behavior

    def test_add_language(self):
        """
        Test that add_language correctly adds a language to the languages list.
        """
        programmer = Programmer(
            name="Taylor Swift",
            age=35,
            email="taylor@example.com",
            languages=[]
        )
        programmer.add_language("JavaScript")
        self.assertIn("JavaScript", programmer.languages)
        self.assertEqual(len(programmer.languages), 1)

    def test_add_language_multiple(self):
        """
        Test adding multiple languages to the languages list.
        """
        programmer = Programmer(
            name="Jamie Lee",
            age=29,
            email="jamie@example.com"
        )
        programmer.add_language("Ruby")
        programmer.add_language("Go")
        self.assertEqual(programmer.languages, ["Ruby", "Go"])

    def test_inheritance(self):
        """
        Test that Programmer inherits methods from Person.
        """
        programmer = Programmer(
            name="Chris Evans",
            age=40,
            email="chris@example.com"
        )
        programmer.add_skill("Leadership")
        programmer.add_language("Swift")
        self.assertIn("Leadership", programmer.skills)
        self.assertIn("Swift", programmer.languages)


if __name__ == "__main__":
    unittest.main()
