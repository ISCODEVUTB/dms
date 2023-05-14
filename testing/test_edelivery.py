import unittest
from datetime import date
from delivery import Delivery
from person import Person
from edelivery import EDelivery

class TestEDelivery(unittest.TestCase):
    buyer = Person("John", "Doe", "johndoe@example.com")
    e_delivery = EDelivery(123, buyer.__str__(), date.today(), "johndoe@example.com")

    def test_instance(self):
        self.assertIsInstance(self.e_delivery, EDelivery, "It's an instance of EDelivery")

    def test_id(self):
        self.assertEqual(self.e_delivery.id, 123)

    def test_buyer(self):
        self.assertEqual(self.e_delivery.buyer, self.buyer.__str__())

    def test_date(self):
        self.assertEqual(self.e_delivery.date, date.today())

    def test_deliver_mail(self):
        self.assertEqual(self.e_delivery.deliver_mail, "johndoe@example.com")
    def test__str__(self):
        self.assertEqual(self.e_delivery.__str__(), {'id': 123, 'buyer': self.buyer.__str__(), 'date': date.today(),'deliver_mail':"johndoe@example.com"})

if __name__ == '__main__':
    unittest.main()