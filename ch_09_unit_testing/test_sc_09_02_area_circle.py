# file: tb_sc/ch_09_unit_testing/test_sc_09_02_area_circle.py
import unittest
from sc_09_02_area_circle import area_circle

class TestArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area_circle(1), 3.14159, places=3)
        self.assertAlmostEqual(area_circle(2), 12.56736, places=3)

unittest.main()