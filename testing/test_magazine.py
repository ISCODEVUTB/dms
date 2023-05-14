import unittest
from logic.classes.magazine import Magazine
from datetime import date


class TestMagazine(unittest.TestCase):
    magazine = Magazine(123, "ian", "forbes", 9.99, "Fashion",
                        "english", date.today(), 10.0, "doi123", 2, 50)

    print(magazine.__str__())

    def test_instance(self):
        self.assertIsInstance(self.magazine, Magazine, "Its instance!")

    def test_id(self):
        self.assertEqual(self.magazine.id, 123)

    def test_author(self):
        self.assertEqual(self.magazine.author, "ian")

    def test_title(self):
        self.assertEqual(self.magazine.title, "forbes")

    def test_price(self):
        self.assertEqual(self.magazine.price, 9.99)

    def test_topic(self):
        self.assertEqual(self.magazine.topic, "Fashion")

    def test_language(self):
        self.assertEqual(self.magazine.language, "english")

    def test_pub_date(self):
        self.assertEqual(self.magazine.pub_date, date.today())

    def test_size(self):
        self.assertEqual(self.magazine.size, 10.0)

    def test_doi(self):
        self.assertEqual(self.magazine.doi, "doi123")

    def test_edition(self):
        self.assertEqual(self.magazine.edition, 2)

    def test_pages(self):
        self.assertEqual(self.magazine.pages, 50)

    def test__str__(self):
        self.assertEquals(self.magazine.__str__(), {'id': 123, 'author': 'ian', 'title': 'forbes', 'price': 9.99,
                                                    'topic': 'Fashion', 'language': 'english', 'pub_date': date.today().strftime("%Y/%m/%d"),
                                                    'size': 10.0, 'doi': 'doi123', 'edition': 2, 'pages': 50})


if __name__ == '__main__':
    unittest.main()
