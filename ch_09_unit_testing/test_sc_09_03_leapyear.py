# file: test_sc_09_03_leapyear.py
import unittest
from sc_09_03_leapyear import is_leap_year
test_data = [
            (2000, True),  # Divisible by 400
            (1900, False), # Divisible by 100 but not by 400
            (2004, True),  # Divisible by 4 but not by 100
            (2008, False), # Not divisible by 4
        ]
class TestLeapYear(unittest.TestCase):
    
    def test_leap_years_v1(self):
        # Enkel løkke og egendefinert melding
        for year, expected in test_data:
           self.assertEqual(is_leap_year(year),
                            expected,
                            msg=f"Feil for år {year}")
        
    def test_leap_years_v2(self):
        # Med subTest og egendefinert melding
        for year, expected in test_data:
           with self.subTest(year=year):
               self.assertEqual(is_leap_year(year),
                                expected,
                                msg=f"Feil for år {year}")                                             

unittest.main()