import unittest

class TestMath(unittest.TestCase):
    def test_simple(self):
        with self.subTest(msg="Test addisjon"):
            self.assertEqual(2 + 2, 5)
        with self.subTest(msg="Test multiplikasjon"):
            self.assertEqual(3 * 3, 8)
        with self.subTest(msg="Test subtraksjon"):
            self.assertEqual(5 - 2, 4)

if __name__ == "__main__":
    unittest.main()