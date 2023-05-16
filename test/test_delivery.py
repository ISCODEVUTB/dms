import unittest
from logic.classes.client import Client
from datetime import date
from logic.classes.delivery import Delivery


class TestDelivery(unittest.TestCase):
    buyer = Client(73577376, "Edwin", "Puertas", "example@email.com")
    delivery = Delivery(123, buyer.__str__(), date.today())

    def test_instance(self):
        self.assertIsInstance(self.delivery, Delivery, "Its instance!")

    def test_id(self):
        self.assertEqual(self.delivery.id, 123)

    def test_buyer(self):
        self.assertEqual(self.delivery.buyer, self.buyer.__str__())

    def test_date(self):
        self.assertEqual(self.delivery.date, date.today())

    def test_setters(self):
        self.delivery.id = 123
        self.delivery.buyer = self.buyer.__str__()
        self.delivery.date = date.today()

    def test__str__(self):
        self.assertEqual(self.delivery.__str__(), {
                         'id': 123, 'buyer': self.buyer.__str__(), 'date': date.today(), })

    def test__eq__(self):
        self.assertEqual(self.delivery.__eq__(self.delivery), True)


if __name__ == '__main__':
    unittest.main()
