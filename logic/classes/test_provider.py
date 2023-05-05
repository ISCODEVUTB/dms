import unittest
from datetime import date
from person import Person
from address import Address
from document import Document
from provider import Provider


class TestProvider(unittest.TestCase):
    address = Address("colombia","bolivar","cartagena","1101","Horizonte","mzn3","house")
    document = Document(12345, 'ian', 'My Document', 10000, 'Science', 'spanish',date.today())
    provider = Provider(1, 'John', 'Doe', '555-555-5555', 'john@example.com', address.__str__(), [document.__str__()])

    def test_instance(self):
        self.assertIsInstance(self.provider, Provider)

    def test_id(self):
        self.assertEqual(self.provider.id, 1)

    def test_name(self):
        self.assertEqual(self.provider.name, 'John')

    def test_last_name(self):
        self.assertEqual(self.provider.last_name, 'Doe')

    def test_phone(self):
        self.assertEqual(self.provider.phone, '555-555-5555')

    def test_mail(self):
        self.assertEqual(self.provider.mail, 'john@example.com')

    def test_address(self):
        self.assertEqual(self.provider.address, self.address.__str__())

    def test_inventory(self):
        self.assertEqual(self.provider.inventory, [self.document.__str__()])
     
    def test__str__(self):
        self.assertEqual(self.provider.__str__(), {'id': 1, 'name': 'John', 'last_name': 'Doe', 'phone': '555-555-5555', 'mail': 'john@example.com', 
                                                   'address': self.address.__str__(), 
                                                   'inventory': [self.document.__str__()]})

if __name__ == '__main__':
    unittest.main()