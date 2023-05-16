import unittest
from datetime import date
from logic.classes.sell import Sell
from logic.classes.document import Document


class TestSell(unittest.TestCase):

    doc = Document(12345, 'ian', 'My Document', 10000,
                   'Science', 'spanish', date.today())
    sell = Sell(123, date(2023, 5, 3), 'credit card', 20.5, [doc.__str__()])

    def test_instance(self):
        self.assertIsInstance(self.sell, Sell, "It's an instance of Sell")

    def test_id(self):
        self.assertEqual(self.sell.id, 123)

    def test_date(self):
        self.assertEqual(self.sell.date, date(2023, 5, 3))

    def test_pay_method(self):
        self.assertEqual(self.sell.pay_method, 'credit card')

    def test_total_price(self):
        self.assertEqual(self.sell.total_price, 20.5)

    def test_items(self):
        self.assertEqual(self.sell.items, [self.doc.__str__()])

    def test_setters(self):
        self.sell.id = 123
        self.sell.date = date(2023, 5, 3)
        self.sell.pay_method = 'credit card'
        self.sell.total_price = 20.5
        self.sell.items = [self.doc.__str__()]

    def test__str__(self):
        self.assertEqual(self.sell.__str__(), {'id': 123, 'date': date(
            2023, 5, 3), 'pay_method': 'credit card', 'total_price': 20.5, 'items': [self.doc.__str__()]})

    def test__eq__(self):
        self.assertEqual(self.sell.__eq__(self.sell), True)


if __name__ == '__main__':
    unittest.main()
