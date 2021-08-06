# Project 1
#
# Name: Nathan Diekema
# Instructor: Padilpsky
# Section: 03

import unittest
from funcs import *

class TestCases(unittest.TestCase):

    def test_poundsToKG_1(self):
        self.assertAlmostEqual(poundsToKG(0), 0.0)
    def test_poundsToKG_2(self):
        self.assertAlmostEqual(poundsToKG(120), 54.43104)

    def test_getMassObject_1(self):
        self.assertEqual(getMassObject('t'), 0.1)
    def test_getMassObject_2(self):
        self.assertEqual(getMassObject('w'), 0.0)
    def test_getMassObject_3(self):
        self.assertEqual(getMassObject('l'), 9.07)
    def test_getMassObject_4(self):
        self.assertEqual(getMassObject('p'), 1.0)
    def test_getMassObject_5(self):
        self.assertEqual(getMassObject('r'), 3.0)
    def test_getMassObject_6(self):
        self.assertEqual(getMassObject('g'), 5.3)


    def test_getVelocityObject_1(self):
        self.assertAlmostEqual(getVelocityObject(0), 0.0)
    def test_getVelocityObject_2(self):
        self.assertAlmostEqual(getVelocityObject(99), 22.02498581)
    def test_getVelocityObject_3(self):
        self.assertAlmostEqual(getVelocityObject(5), 4.94974747)
    def test_getVelocityObject_4(self):
        self.assertAlmostEqual(getVelocityObject(20), 9.89949494)

    def test_getVelocitySkater_1(self):
        self.assertAlmostEqual(getVelocitySkater(100, 0, 100), 0.0)
    def test_getVelocitySkater_2(self):
        self.assertAlmostEqual(getVelocitySkater(60, 1, 30), 0.5)
    def test_getVelocitySkater_3(self):
        self.assertAlmostEqual(getVelocitySkater(30, 9, 19), 5.7)
    def test_getVelocitySkater_4(self):
        self.assertAlmostEqual(getVelocitySkater(1956, 3, 145), 0.2223926)

if __name__ == '__main__':
    unittest.main()
