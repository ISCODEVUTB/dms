import unittest
from datetime import date
from logic.classes.audiobook import AudioBook


class TestAudioBook(unittest.TestCase):
    book = AudioBook(
        id=1,
        author='J.K. Rowling',
        title='Harry Potter',
        price=9.99,
        topic='Fantasy',
        language='English',
        pub_date=date(1997, 6, 26),
        size=100,
        doi='10.1234/abcd',
        duration=3600,
        synopsis='A boy discovers he is a wizard and attends a school of magic.')

    def test_instance(self):
        self.assertIsInstance(self.book, AudioBook,
                              "It's an instance of AudioBook")

    def test_id(self):
        self.assertEqual(self.book.id, 1)

    def test_author(self):
        self.assertEqual(self.book.author, 'J.K. Rowling')

    def test_title(self):
        self.assertEqual(self.book.title, 'Harry Potter')

    def test_price(self):
        self.assertEqual(self.book.price, 9.99)

    def test_topic(self):
        self.assertEqual(self.book.topic, 'Fantasy')

    def test_language(self):
        self.assertEqual(self.book.language, 'English')

    def test_pub_date(self):
        self.assertEqual(self.book.pub_date, date(1997, 6, 26))

    def test_size(self):
        self.assertEqual(self.book.size, 100.0)

    def test_doi(self):
        self.assertEqual(self.book.doi, '10.1234/abcd')

    def test_duration(self):
        self.assertEqual(self.book.duration, 3600)

    def test_synopsis(self):
        self.assertEqual(
            self.book.synopsis, 'A boy discovers he is a wizard and attends a school of magic.')

    def test_setters(self):
        self.book.id = 2
        self.book.author = 'J.K. Rowling'
        self.book.title = 'Harry Potter'
        self.book.price = 9.99
        self.book.topic = 'Fantasy'
        self.book.language = 'English'
        self.book.pub_date = date(1997, 6, 26)
        self.book.size = 100.0
        self.book.doi = '10.1234/abcd'
        self.book.duration = 3600
        self.book.synopsis = 'A boy discovers he is a wizard and attends a school of magic.'

    def test__str__(self):
        self.assertEqual(self.book.__str__(), {'id': 1, 'author': "J.K. Rowling", 'title': "Harry Potter",  'price': 9.99, 'topic': "Fantasy",
                                               'language': "English", 'pub_date': date(1997, 6, 26).strftime("%Y/%m/%d"), 'size': 100, 'doi': "10.1234/abcd", 'duration': 3600,
                                               'synopsis': "A boy discovers he is a wizard and attends a school of magic."})

    def test__eq__(self):
        self.assertEqual(self.book.__eq__(self.book), True)


if __name__ == '__main__':
    unittest.main()
