import unittest
from convertor import fahr_to_celsius


class TestConvertor(unittest.TestCase):

    def test_fahr_to_celsius(self):
        self.assertEqual(fahr_to_celsius(32), 0)
