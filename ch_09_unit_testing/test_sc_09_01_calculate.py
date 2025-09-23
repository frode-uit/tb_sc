# file: tb_sc/ch_09_unit_testing/test_sc_09_01_calculate.py
import unittest
from sc_09_01_calculate import calculate # det vi skal teste

class TestCalculate(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate(2, 3, "add"), 5)

    def test_subtraction(self):
        self.assertEqual(calculate(5, 2, "sub"), 3)

    def test_illegal_operation(self):
        self.assertIsNone(calculate(1, 1, "mult"))

if __name__ == "__main__":
    unittest.main()
