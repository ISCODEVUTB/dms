import unittest
from logic.classes.invbook import InvBook
from datetime import date


class TestInvBook(unittest.TestCase):
    inv_book = InvBook(123, "ian", "The Science of Cooking", 29.99, "Food Science", "English", date(
        2020, 1, 1), 10.5, "10.1000/182", 350, "An exploration of the chemistry and physics behind cooking techniques")
    print(inv_book.__str__())

    def test_instance(self):
        self.assertIsInstance(self.inv_book, InvBook,
                              "It's an instance of InvBook")

    def test_id(self):
        self.assertEqual(self.inv_book.id, 123)

    def test_author(self):
        self.assertEqual(self.inv_book.author, "ian")

    def test_title(self):
        self.assertEqual(self.inv_book.title, "The Science of Cooking")

    def test_price(self):
        self.assertEqual(self.inv_book.price, 29.99)

    def test_topic(self):
        self.assertEqual(self.inv_book.topic, "Food Science")

    def test_language(self):
        self.assertEqual(self.inv_book.language, "English")

    def test_pub_date(self):
        self.assertEqual(self.inv_book.pub_date, date(2020, 1, 1))

    def test_size(self):
        self.assertEqual(self.inv_book.size, 10.5)

    def test_doi(self):
        self.assertEqual(self.inv_book.doi, "10.1000/182")

    def test_pages(self):
        self.assertEqual(self.inv_book.pages, 350)

    def test_abstract(self):
        self.assertEqual(self.inv_book.abstract,
                         "An exploration of the chemistry and physics behind cooking techniques")

    def test_setters(self):
        self.inv_book.id = 123
        self.inv_book.author = 'ian'
        self.inv_book.title = 'The Science of Cooking'
        self.inv_book.price = 29.99
        self.inv_book.topic = 'Food Science'
        self.inv_book.language = 'English'
        self.inv_book.pub_date = date(2020, 1, 1)
        self.inv_book.size = 10.5
        self.inv_book.doi = "10.1000/182"
        self.inv_book.pages = 350
        self.inv_book.abstract = "An exploration of the chemistry and physics behind cooking techniques"

    def test__str__(self):
        self.assertEquals(self.inv_book.__str__(), {'id': 123, 'author': 'ian', 'title': 'The Science of Cooking', 'price': 29.99,
                                                    'topic': 'Food Science', 'language': 'English', 'pub_date': date(2020, 1, 1).strftime("%Y/%m/%d"), 'size': 10.5,
                                                    'doi': '10.1000/182', 'pages': 350, 'abstract': 'An exploration of the chemistry and physics behind cooking techniques'})

    def test__eq__(self):
        self.assertEquals(self.inv_book.__eq__(self.inv_book), True)


if __name__ == '__main__':
    unittest.main()
