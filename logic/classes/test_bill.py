import unittest
from datetime import date
from bill import Bill
from client import Client
from document import Document


class TestBill(unittest.TestCase):
    buyer = Client(123, "Juan", "Pérez", "1234", "juan@example.com")
    item = Document(1399,"ian","caminos",20000,"romance","spanish",date.today())
    bill = Bill(1, buyer.__str__(), date.today(), 20000, [item.__str__()])
    
    def test_instance(self):
        self.assertIsInstance(self.bill, Bill, "It's an instance of Bill class")

    def test_id(self):
        self.assertEqual(self.bill.id,1)

    def test_buyer(self):
        self.assertEqual(self.bill.buyer, self.buyer.__str__() )

    def test_date(self):
        self.assertEqual(self.bill.date, date.today())

    def test_price(self):
        self.assertEqual(self.bill.price, 20000)

    def test_items(self):
        self.assertEqual(self.bill.items, [self.item.__str__()])

    def test__str__(self):
        self.assertEqual(self.bill.__str__(), {'id': 1, 'buyer':f"{self.buyer.__str__()}" , 'date':date.today(), 'price': 20000, 'items': f"[{self.item.__str__()}]"})



if __name__ == '__main__':
    unittest.main()