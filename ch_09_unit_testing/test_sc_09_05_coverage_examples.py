# file: test_sc_09_05_coverage_examples.py
import unittest
from sc_09_05_coverage_examples import greet, is_even, add, subtract, is_valid

class TestCoverageExamples(unittest.TestCase):

    # Line coverage: tester at linjen i greet() blir kjørt
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    # Branch coverage: tester både if og else i is_even()
    def test_is_even_true(self):
        self.assertTrue(is_even(4))

    def test_is_even_false(self):
        self.assertFalse(is_even(3))

    # Function/method coverage: tester add(), men ikke subtract()
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    # Condition coverage: tester is_valid() med ulike sannhetsverdier
    def test_is_valid_true(self):
        self.assertTrue(is_valid(5))  # True and True

    def test_is_valid_false_low(self):
        self.assertFalse(is_valid(-1))  # False and True

    def test_is_valid_false_high(self):
        self.assertFalse(is_valid(15))  # True and False

if __name__ == "__main__":
    unittest.main()