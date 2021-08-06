# Project 4 - Word Search
# Author: Nathan Diekema
# Instructor: Padlipsky

import unittest
from funcs import *
class TestCases(unittest.TestCase):

    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for x in range(len(l1)):
            for z in range(4):
                self.assertEqual(l1[x][z],l2[x][z])

    def test_search_vertical_1(self):
        puzzle = []
        puzzle.append("WAQHTTWEEC")
        puzzle.append("FYUOETFCMV")
        puzzle.append("ERFGJPLIQA")
        puzzle.append("ZCDFAEUJGT")
        puzzle.append("PWRTYUFCVB")
        puzzle.append("EDGLPWSDFG")
        puzzle.append("DRVHTTWEEC")
        puzzle.append("XKWINPINLD")
        puzzle.append("SOVOEMSPPW")
        puzzle.append("FRTKSJFOAU")
        words = []
        words.append("FEZP")
        words.append("FGOH")
        vertical = search_vertical(puzzle,words)
        self.assertListAlmostEqual(vertical, [["FEZP","(DOWN)",1,0],["FGOH","(UP)",3,3]])

    def test_search_vertical_2(self):
        puzzle = []
        puzzle.append("WAQHTTWEEC")
        puzzle.append("FYUOETFCMV")
        puzzle.append("ERFGJPLIQA")
        puzzle.append("ZCDFAEUJGT")
        puzzle.append("PWRTYUFCVB")
        puzzle.append("EDGLPWSDFG")
        puzzle.append("DRVHTTWEEC")
        puzzle.append("XKWINPINLD")
        puzzle.append("SOVOEMSPPW")
        puzzle.append("FRTKSJFOAU")
        words = []
        words.append("TFGO")
        words.append("QUFD")
        vertical = search_vertical(puzzle,words)
        self.assertListAlmostEqual(vertical, [["QUFD","(DOWN)",0,2],["TFGO","(UP)",4,3]])

    def test_search_diagonal_1(self):
        puzzle = []
        puzzle.append("WAQHTTWEEC")
        puzzle.append("FYUOETFCMV")
        puzzle.append("ERFGJPLIQA")
        puzzle.append("ZCDFAEUJGT")
        puzzle.append("PWRTYUFCVB")
        puzzle.append("EDGLPWSDFG")
        puzzle.append("DRVHTTWEEC")
        puzzle.append("XKWINPINLD")
        puzzle.append("SOVOEMSPPW")
        puzzle.append("FRTKSJFOAU")
        words = []
        words.append("WCQT")
        words.append("WGHN")
        vertical = search_diagonal(puzzle,words)
        self.assertListAlmostEqual(vertical, [["WCQT","(DIAGONAL)",0,6],["WGHN","(DIAGONAL)",4,1]])

    def test_search_diagonal_2(self):
        puzzle = []
        puzzle.append("WAQHTTWEEC")
        puzzle.append("FYUOETFCMV")
        puzzle.append("ERFGJPLIQA")
        puzzle.append("ZCDFAEUJGT")
        puzzle.append("PWRTYUFCVB")
        puzzle.append("EDGLPWSDFG")
        puzzle.append("DRVHTTWEEC")
        puzzle.append("XKWINPINLD")
        puzzle.append("SOVOEMSPPW")
        puzzle.append("FRTKSJFOAU")
        words = []
        words.append("WCQT")
        words.append("WGHN")
        diagonal = search_diagonal(puzzle,words)
        self.assertListAlmostEqual(diagonal, [["WCQT","(DIAGONAL)",0,6],["WGHN","(DIAGONAL)",4,1]])

    def test_search_horizontal_1(self):
        puzzle = []
        puzzle.append("WAQHTTWEEC")
        puzzle.append("FYUOETFCMV")
        puzzle.append("ERFGJPLIQA")
        puzzle.append("ZCDFAEUJGT")
        puzzle.append("PWRTYUFCVB")
        puzzle.append("EDGLPWSDFG")
        puzzle.append("DRVHTTWEEC")
        puzzle.append("XKWINPINLD")
        puzzle.append("SOVOEMSPPW")
        puzzle.append("FRTKSJFOAU")
        words = []
        words.append("ERFGJ")
        words.append("VMCFT")
        horizontal = search_horizontal(puzzle,words)
        self.assertListAlmostEqual(horizontal, [["VMCFT","(BACKWARD)",1,9],["ERFGJ","(FORWARD)",2,0]])

    def test_search_horizontal_2(self):
        puzzle = []
        puzzle.append("WAQHTTWEEC")
        puzzle.append("FYUOETFCMV")
        puzzle.append("ERFGJPLIQA")
        puzzle.append("ZCDFAEUJGT")
        puzzle.append("PWRTYUFCVB")
        puzzle.append("EDGLPWSDFG")
        puzzle.append("DRVHTTWEEC")
        puzzle.append("XKWINPINLD")
        puzzle.append("SOVOEMSPPW")
        puzzle.append("FRTKSJFOAU")
        words = []
        words.append("TWEEC")
        words.append("DSWP")
        horizontal = search_horizontal(puzzle,words)
        self.assertListAlmostEqual(horizontal, [["TWEEC","(FORWARD)",0,5],["DSWP","(BACKWARD)",5,7],["TWEEC","(FORWARD)",6,5]])

if __name__ == '__main__':
   unittest.main()