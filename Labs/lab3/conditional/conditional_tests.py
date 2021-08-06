import unittest
from conditional import *

class TestCases(unittest.TestCase):
    def test_function_names(self):
        max_101(0, 0)
        max_of_three(0, 0, 0)
        rental_late_fee(0)
    
    #test max_101
    def test_max_101_1(self):
        self.assertEqual(max_101(5,3),5)
    def test_max_101_2(self):
        self.assertEqual(max_101(94,95),95)
    def test_max_101_3(self):
        self.assertEqual(max_101(6,6),"Equal")

    #test max_of_three
    def test_max_of_three_1(self):
        self.assertEqual(max_of_three(5,4,3),5)
    def test_max_of_three_2(self):
        self.assertEqual(max_of_three(7,5,9),9)
    def test_max_of_three_3(self):
        self.assertEqual(max_of_three(54,650,90),650)
    def test_max_of_three_4(self):
        self.assertEqual(max_of_three(-18,3,15), 15)

    #test rental_late_fee
    def test_rental_late_fee_1(self):
        self.assertEqual(rental_late_fee(0),0)
    def test_rental_late_fee_2(self):
        self.assertEqual(rental_late_fee(9),5)
    def test_rental_late_fee_3(self):
        self.assertEqual(rental_late_fee(25),100)
    def test_rental_late_fee_4(self):
        self.assertEqual(rental_late_fee(15),7)
    def test_rental_late_fee_5(self):
        self.assertEqual(rental_late_fee(24), 19)
    

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

