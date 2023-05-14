import unittest
from datetime import date
from logic.classes.pdocument import PDocument


class TestFDocument(unittest.TestCase):
    doc = PDocument(1, "ian", "The Art of Programming", 29.99,
                    "Computer Science", "English", date.today(), "Tech Pub")

    def test_instance(self):
        self.assertIsInstance(self.doc, PDocument, "Its instance!")

    def test_id(self):
        self.assertEqual(self.doc.id, 1)

    def test_author(self):
        self.assertEqual(self.doc.author, "ian")

    def test_title(self):
        self.assertEqual(self.doc.title, "The Art of Programming")

    def test_price(self):
        self.assertEqual(self.doc.price, 29.99)

    def test_topic(self):
        self.assertEqual(self.doc.topic, "Computer Science")

    def test_language(self):
        self.assertEqual(self.doc.language, "English")

    def test_pub_date(self):
        self.assertEqual(self.doc.pub_date, date.today())

    def test_publisher(self):
        self.assertEqual(self.doc.publisher, "Tech Pub")

    def test__str__(self):
        self.assertEqual(self.doc.__str__(), {'id': 1, 'author': 'ian', 'title': 'The Art of Programming', 'price': 29.99, 'topic': 'Computer Science',
                                              'language': 'English', 'pub_date': date.today().strftime("%Y/%m/%d"), 'publisher': 'Tech Pub'})


if __name__ == '__main__':
    unittest.main()
