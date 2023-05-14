import unittest
from datetime import date
from logic.classes.edocument import EDocument


class TestEDocument(unittest.TestCase):
    doc = EDocument(
        id=123,
        author="Jane Doe",
        title="My Awesome Book",
        price=9.99,
        topic="Science",
        language="spanish",
        pub_date=date.today(),
        size=2.5,
        doi="https://doi.org/10.1234"
    )

    def test_instance(self):
        self.assertIsInstance(self.doc, EDocument, "Its instance!")

    def test_id(self):
        self.assertEqual(self.doc.id, 123)

    def test_author(self):
        self.assertEqual(self.doc.author, "Jane Doe")

    def test_title(self):
        self.assertEqual(self.doc.title, "My Awesome Book")

    def test_price(self):
        self.assertEqual(self.doc.price, 9.99)

    def test_topic(self):
        self.assertEqual(self.doc.topic, "Science")

    def test_language(self):
        self.assertEqual(self.doc.language, "spanish")

    def test_pub_date(self):
        self.assertEqual(self.doc.pub_date, date.today())

    def test_size(self):
        self.assertEqual(self.doc.size, 2.5)

    def test_doi(self):
        self.assertEqual(self.doc.doi, "https://doi.org/10.1234")

    def test__str__(self):
        self.assertEqual(self.doc.__str__(), {'id': 123, 'author': "Jane Doe", 'title': "My Awesome Book", 'price': 9.99,
                                              'topic': "Science", 'language': "spanish", 'pub_date': date.today().strftime("%Y/%m/%d"), 'size': 2.5, 'doi': "https://doi.org/10.1234"})


if __name__ == '__main__':
    unittest.main()
