import unittest
from logic.classes.client import Client


class TestClient(unittest.TestCase):
    client = Client(1, 'John', 'Doe', '123-456-7890', 'johndoe@example.com')

    def test_instance(self):
        self.assertIsInstance(self.client, Client,
                              "It's an instance of Client!")

    def test_id(self):
        self.assertEqual(self.client.id, 1)

    def test_name(self):
        self.assertEqual(self.client.name, 'John')

    def test_last_name(self):
        self.assertEqual(self.client.last_name, 'Doe')

    def test_phone(self):
        self.assertEqual(self.client.phone, '123-456-7890')

    def test_mail(self):
        self.assertEqual(self.client.mail, 'johndoe@example.com')

    def test__str__(self):
        self.assertEqual(self.client.__str__(), {
                         'id': 1, 'name': 'John', 'last_name': 'Doe', 'phone': '123-456-7890', 'mail': 'johndoe@example.com'})


if __name__ == '__main__':
    unittest.main()
