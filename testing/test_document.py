import unittest
from document import Document
from datetime import date


class TestDocument(unittest.TestCase):
    document = Document(12345, 'ian', 'My Document', 10000, 'Science', 'spanish',date.today())

    def test_instance(self):
        self.assertIsInstance(self.document, Document, "Its instance!")

    def test_id(self):
        self.assertEqual(self.document.id, 12345)

    def test_author(self):
        self.assertEqual(self.document.author, 'ian')

    def test_title(self):
        self.assertEqual(self.document.title, 'My Document')

    def test_price(self):
        self.assertEqual(self.document.price, 10000)

    def test_topic(self):
        self.assertEqual(self.document.topic, 'Science')

    def test_language(self):
        self.assertEqual(self.document.language, 'spanish')
    
    def test_pub_date(self):
        self.assertEqual(self.document.pub_date, date.today())
    
    def test__str__(self):
        self.assertEqual(self.document.__str__(),{'id': 12345, 'author': "ian", 'title': "My Document", 'price': 10000, 'topic': "Science",'language':"spanish",'pub_date': date.today().strftime("%Y/%m/%d")})
          
if __name__ == '__main__':
    unittest.main()