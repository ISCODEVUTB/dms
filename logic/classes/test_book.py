import unittest
from datetime import date
from book import Book

class TestBook(unittest.TestCase):
    book = Book(1234, "ian", "art", 19.99, "fiction", "english", date.today(), "norma", "alba", 250, "A great book", "A great presentation")

    print(book.__str__())
    def test_instance(self):
        self.assertIsInstance(self.book, Book, "Its instance!")

    def test_id(self):
        self.assertEqual(self.book.id, 1234)

    def test_author(self):
        self.assertEqual(self.book.author, "ian")

    def test_title(self):
        self.assertEqual(self.book.title, "art")

    def test_price(self):
        self.assertEqual(self.book.price, 19.99)

    def test_topic(self):
        self.assertEqual(self.book.topic, "fiction")

    def test_language(self):
        self.assertEqual(self.book.language, "english")

    def test_pub_date(self):
        self.assertEqual(self.book.pub_date, date.today())

    def test_publisher(self):
        self.assertEqual(self.book.publisher, "norma")

    def test_editor(self):
        self.assertEqual(self.book.editor, "alba")

    def test_pages(self):
        self.assertEqual(self.book.pages, 250)

    def test_synopsis(self):
        self.assertEqual(self.book.synopsis, "A great book")

    def test_presentation(self):
        self.assertEqual(self.book.presentation, "A great presentation")

    def test__str__(self):
        self.assertEquals(self.book.__str__(),{'id': 1234, 'author': 'ian', 'title': 'art', 'price': 19.99, 
                                               'topic': 'fiction', 'language': 'english', 'pub_date': date.today().strftime("%Y/%m/%d"), 
                                               'publisher': 'norma', 'editor': 'alba', 'pages': 250, 
                                               'synopsis': 'A great book', 'presentation': 'A great presentation'})

if __name__ == '__main__':
    unittest.main()