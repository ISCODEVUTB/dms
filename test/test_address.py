import unittest
from logic.classes.address import Address


class TestAddress(unittest.TestCase):

    myaddress = Address("colombia", "bolivar", "cartagena",
                        "1101", "Horizonte", "mzn3", "house")

    def test_instance(self):
        self.assertIsInstance(self.myaddress, Address,
                              "It's an instance of Address!")

    def test_country(self):
        self.assertEqual(self.myaddress.country, "colombia")

    def test_department(self):
        self.assertEqual(self.myaddress.department, "bolivar")

    def test_city(self):
        self.assertEqual(self.myaddress.city, "cartagena")

    def test_post_Code(self):
        self.assertEqual(self.myaddress.post_code, "1101")

    def test_neighborhood(self):
        self.assertEqual(self.myaddress.neighborhood, "Horizonte")

    def test_street(self):
        self.assertEqual(self.myaddress.street, "mzn3")

    def test_complement(self):
        self.assertEqual(self.myaddress.complement, "house")

    def test_setters(self):
        self.myaddress.country = "colombia"
        self.myaddress.department = "bolivar"
        self.myaddress.city = "cartagena"
        self.myaddress.post_code = "1101"
        self.myaddress.neighborhood = "Horizonte"
        self.myaddress.street = "mzn3"
        self.myaddress.complement = "house"

    def test__str__(self):
        self.assertEqual(self.myaddress.__str__(), {'country': "colombia", 'department': "bolivar", 'city': "cartagena",
                         'post_code': "1101", 'neighborhood': "Horizonte", 'street': "mzn3", 'complement': "house"})

    def test__eq__(self):
        self.assertEqual(self.myaddress.__eq__(self.myaddress), True)


if __name__ == '__main__':
    unittest.main()
