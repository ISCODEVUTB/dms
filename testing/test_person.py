import unittest
from logic.classes.person import Person


class TestPerson(unittest.TestCase):
    person = Person(1, "ian", "montoya", "1234567890", "example@example.com")

    def test_instance(self):
        self.assertIsInstance(self.person, Person, "Its instance!")

    def test_id(self):
        self.assertEqual(self.person.id, 1)

    def test_name(self):
        self.assertEqual(self.person.name, "ian")

    def test_last_name(self):
        self.assertEqual(self.person.last_name, "montoya")

    def test_phone(self):
        self.assertEqual(self.person.phone, "1234567890")

    def test_mail(self):
        self.assertEqual(self.person.mail, "example@example.com")

    def test__str__(self):
        self.assertEqual(self.person.__str__(), {'id': 1, 'name': "ian", 'last_name': "montoya",
                                                 'phone': "1234567890", 'mail': "example@example.com"})


if __name__ == '__main__':
    unittest.main()
