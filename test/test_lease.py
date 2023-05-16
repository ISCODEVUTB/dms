import unittest
from datetime import date
from logic.classes.document import Document
from logic.classes.lease import Lease


class TestLease(unittest.TestCase):
    doc = Document(2, 'author', 'title', 10.0,
                   'topic', 'spanish', date.today())
    lease = Lease(1, date.today(), date(date.today().year,
                  date.today().month+1, 20), "card", 10.0, [doc.__str__()])

    def test_instance(self):
        self.assertIsInstance(self.lease, Lease, "Its instance!")

    def test_id(self):
        self.assertEqual(self.lease.id, 1)

    def test_start_date(self):
        self.assertEqual(self.lease.start_date, date.today())

    def test_finish_date(self):
        self.assertEqual(self.lease.finish_date,  date(
            date.today().year, date.today().month+1, 20))

    def test_pay_method(self):
        self.assertEqual(self.lease.pay_method, 'card')

    def test_total_price(self):
        self.assertEqual(self.lease.total_price, 10.0)

    def test_items(self):
        self.assertEqual(self.lease.items, [self.doc.__str__()])

    def test_setters(self):
        self.lease.id = 1
        self.lease.start_date = date.today()
        self.lease.finish_date = date(
            date.today().year, date.today().month+1, 20)
        self.lease.pay_method = "card"
        self.lease.total_price = 10.0
        self.lease.items = [self.doc.__str__()]

    def test__str__(self):
        self.assertEqual(self.lease.__str__(), {'id': 1, 'start_date': date.today(), 'finish_date': date(date.today().year, date.today().month+1, 20),
                                                'pay_method': "card", 'total_price': 10.0, 'items': [self.doc.__str__()]})

    def test__eq__(self):
        self.assertEqual(self.lease.__eq__(self.lease), True)


if __name__ == '__main__':
    unittest.main()
