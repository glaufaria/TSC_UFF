#!/usr/bin/env python
# coding: UTF-8
#
##
# @package DNAStrandTest
#
#   DNAStrand test class.
#
#   @author Glauber Faria
#   @since 10/04/2020
#
import sys
from DNAStrand import DNAStrand
import unittest


class TestDNAStrand(unittest.TestCase):

    d1 = DNAStrand("TCAT")
    d2 = DNAStrand("AGAGCAT")
    m = 'A'
    ls = 2
    rs = 3

    def test_createComplement(self):
        msg = 'createComplement() should return a DNAStrand complement'
        dna_strand1 = 'AGTA'
        dna_strand2 = 'TCTCGTA'
        self.assertEqual(self.d1.createComplement().strand, dna_strand1, msg)
        self.assertEqual(self.d2.createComplement().strand, dna_strand2, msg)

    def test_is_Valid(self):
        msg = 'isValid() should return True'
        self.assertTrue(self.d1.isValid(), msg)
        self.assertTrue(self.d2.isValid(), msg)

    def test_countMatchesWithLeftShif(self):
        msg = 'countMatchesWithLeftShift() should return the value of matches in two DNA strands'
        value1 = 1
        value2 = 1
        self.assertEqual(self.d1.countMatchesWithLeftShift(self.d2, 5), value1, msg)
        self.assertEqual(self.d2.countMatchesWithLeftShift(self.d1, 3), value2, msg)

    def test_findMatchesWithLeftShift(self):
        msg = 'findMatchesWithLeftShift() should return a dna string with capitalized matching characters'
        dna_strand1 = 'Tcat'
        dna_strand2 = 'agAgcat'
        self.assertEqual(self.d1.findMatchesWithLeftShift(self.d2, 5), dna_strand1, msg)
        self.assertEqual(self.d2.findMatchesWithLeftShift(self.d1, 1), dna_strand2, msg)

    def test_countMatchesWithRightShift(self):
        msg = 'countMatchesWithRightShift() should return the value of matches in two DNA strands'
        value1 = 1
        value2 = 2
        self.assertEqual(self.d1.countMatchesWithRightShift(self.d2, 3), value1, msg)
        self.assertEqual(self.d2.countMatchesWithRightShift(self.d1, 0), value2, msg)

    def test_findMatchesWithRightShift(self):
        msg = 'findMatchesWithRightShift() should return a dna string with capitalized matching characters'
        dna_strand1 = 'tcaT'
        dna_strand2 = 'agAGcAt'
        self.assertEqual(self.d1.findMatchesWithRightShift(self.d2, 1), dna_strand1, msg)
        self.assertEqual(self.d2.findMatchesWithRightShift(self.d1, 2), dna_strand2, msg)

    def test_findMaxPossibleMatches(self):
        msg = 'findMaxPossibleMatches() should return the maximum value of matches in two DNA strands'
        value = 3
        self.assertEqual(self.d1.findMaxPossibleMatches(self.d2), value, msg)
        self.assertEqual(self.d2.findMaxPossibleMatches(self.d1), value, msg)

    def test_letterCoun(self):
        msg = 'letterCount() should return the number of times that a letter appears in a DNA strand'
        value1 = 1
        value2 = 2
        self.assertEqual(self.d1.letterCount('C'), value1, msg)
        self.assertEqual(self.d2.letterCount('G'), value2, msg)

    def test_matches(self):
        msg = 'matches() should return True'
        self.assertTrue(self.d1.matches('A', 'T'), msg)
        self.assertTrue(self.d2.matches('C', 'G'), msg)

    def test_matches_notvalid(self):
        msg = 'matches() should return False'
        self.assertFalse(self.d1.matches('A', 'C'), msg)
        self.assertFalse(self.d2.matches('G', 'T'), msg)


if __name__ == '__main__':
    unittest.main()
