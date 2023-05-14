import unittest
from datetime import date
from logic.classes.pdelivery import PDelivery
from logic.classes.person import Person
from logic.classes.address import Address


class TestDelivery(unittest.TestCase):
    buyer = Person(1, "Edwin", "Puertas", "30228", "example@email.com")
    contact = Person(2, "samuel", "montoya", "30228", "example@email.com")
    myaddress = Address("colombia", "bolivar", "cartagena",
                        "1101", "Horizonte", "mzn3", "house")
    delivery = PDelivery(3, buyer.__str__(), date.today(),
                         myaddress.__str__(), contact.__str__(), "Documents")

    def test_instance(self):
        self.assertIsInstance(self.delivery, PDelivery, "Its instance!")

    def test_id(self):
        self.assertEqual(self.delivery.id, 3)

    def test_buyer(self):
        self.assertEqual(self.delivery.buyer, self.buyer.__str__())

    def test_date(self):
        self.assertEqual(self.delivery.date, date.today())

    def test_myaddres(self):
        self.assertEqual(self.delivery.address, self.myaddress.__str__())

    def test_contac(self):
        self.assertEqual(self.delivery.contact, self.contact.__str__())

    def test_company(self):
        self.assertEqual(self.delivery.company, "Documents")

    def test__str__(self):
        self.assertEqual(self.delivery.__str__(), {'id': 3, 'buyer': self.buyer.__str__(),
                                                   'date': date.today(), 'address': self.myaddress.__str__(), 'contact': self.contact.__str__(),
                                                   'company': 'Documents'})


if __name__ == '__main__':
    unittest.main()
