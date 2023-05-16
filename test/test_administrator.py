
import unittest
from logic.classes.administrator import Administrator


class TestAdministrator(unittest.TestCase):
    admin = Administrator(10, 'ian', 'montoya',
                          '3032846010', 'montoya@mail.com')

    def test_instance(self):
        self.assertIsInstance(self.admin, Administrator, "Its instance!")

    def test_id(self):
        self.assertEqual(self.admin.id, 10)

    def test_name(self):
        self.assertEqual(self.admin.name, 'ian')

    def test_last_name(self):
        self.assertEqual(self.admin.last_name, 'montoya')

    def test_phone(self):
        self.assertEqual(self.admin.phone, '3032846010')

    def test_mail(self):
        self.assertEqual(self.admin.mail, 'montoya@mail.com')

    def test_setters(self):
        self.admin.name = 'ian'
        self.admin.last_name = 'montoya'
        self.admin.phone = '3032846010'
        self.admin.mail = 'montoya@mail.com'

    def test__str__(self):
        self.assertEqual(self.admin.__str__(), {
                         'id': 10, 'name': "ian", 'last_name': "montoya",  'phone': "3032846010", 'mail': "montoya@mail.com"})

    def test__eq__(self):
        self.assertEqual(self.admin.__eq__(self.admin), True)


if __name__ == '__main__':
    unittest.main()
