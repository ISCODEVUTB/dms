import unittest
from datetime import date
from logic.classes.ebook import Ebook


class TestEbook(unittest.TestCase):
    book = Ebook(123456, "J.K. Rowling", "Harry Potter", 10.99, "Fantasy", "english",
                 date(1997, 6, 26), 2.5, "9780747532743", "Bloomsbury", 223,
                 " A boy discovers he is a wizard and attends a school of magic.")

    print(book.__str__())

    def test_instance(self):
        self.assertIsInstance(self.book, Ebook, "Its instance!")

    def test_id(self):
        self.assertEqual(self.book.id, 123456)

    def test_author(self):
        self.assertEqual(self.book.author, "J.K. Rowling")

    def test_title(self):
        self.assertEqual(self.book.title, "Harry Potter")

    def test_price(self):
        self.assertEqual(self.book.price, 10.99)

    def test_topic(self):
        self.assertEqual(self.book.topic, "Fantasy")

    def test_language(self):
        self.assertEqual(self.book.language, "english")

    def test_pub_date(self):
        self.assertEqual(self.book.pub_date, date(1997, 6, 26))

    def test_size(self):
        self.assertEqual(self.book.size, 2.5)

    def test_doi(self):
        self.assertEqual(self.book.doi, "9780747532743")

    def test_editor(self):
        self.assertEqual(self.book.editor, "Bloomsbury")

    def test_pages(self):
        self.assertEqual(self.book.pages, 223)

    def test_synopsis(self):
        self.assertEqual(
            self.book.synopsis, " A boy discovers he is a wizard and attends a school of magic.")

    def test_setters(self):
        self.book.id = 123456
        self.book.author = "J.K. Rowling"
        self.book.title = "Harry Potter"
        self.book.price = 10.99
        self.book.topic = "Fantasy"
        self.book.language = "english"
        self.book.pub_date = date(1997, 6, 26)
        self.book.size = 2.5
        self.book.doi = "9780747532743"
        self.book.editor = "Bloomsbury"
        self.book.pages = 223
        self.book.synopsis = " A boy discovers he is a wizard and attends a school of magic."

    def test__str__(self):
        self.assertEqual(self.book.__str__(), {'id': 123456, 'author': 'J.K. Rowling', 'title': 'Harry Potter', 'price': 10.99,
                                               'topic': 'Fantasy', 'language': 'english', 'pub_date': date(1997, 6, 26).strftime("%Y/%m/%d"), 'size': 2.5,
                                               'doi': '9780747532743', 'editor': 'Bloomsbury', 'pages': 223, 'synopsis': ' A boy discovers he is a wizard and attends a school of magic.'})

    def test__eq__(self):
        self.assertEqual(self.book.__eq__(self.book), True)


if __name__ == '__main__':
    unittest.main()
