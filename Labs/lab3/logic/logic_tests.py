import unittest
from logic import *

class TestCases(unittest.TestCase):
    def test_function_names(self):
        is_even(0)
        in_an_interval(0)

    def test_in_an_interval_1(self):
        self.assertTrue(in_an_interval(103))

    def test_in_an_interval_2(self):
        self.assertFalse(in_an_interval(12))
                
    def test_in_an_interval_3(self):
        self.assertTrue(in_an_interval(2))

    def test_is_even_1(self):
        self.assertTrue(is_even(42))

    def test_is_even_2(self):
        self.assertFalse(is_even(19))

    def test_is_even_3(self):
        self.assertTrue(is_even(19876))


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

