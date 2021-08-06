import unittest
import funcs

class TestCases(unittest.TestCase):

    def test_f_1(self): 
        self.assertEqual(0, funcs.f(0))

    def test_f_2(self):
        self.assertEqual(185, funcs.f(5))
      
    def test_g_1(self):
        self.assertRaises(ZeroDivisionError, funcs.g, 0, 3)

    def test_g_2(self):
        self.assertAlmostEqual(20/3, funcs.g(4,8))
      
    def test_hypotenuse_1(self):
        self.assertEqual(5, funcs.hypotenuse(3,4))

    def test_hypotenuse_2(self):
        self.assertEqual(13, funcs.hypotenuse(5,12))

    def test_is_positive_1(self):
        self.assertTrue(funcs.is_positive(14))

    def test_is_positive_2(self):
        self.assertFalse(funcs.is_positive(-8))
   


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

