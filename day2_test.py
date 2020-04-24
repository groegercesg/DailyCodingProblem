import unittest
import day2

class Day2UnitTests(unittest.TestCase):
    def test_listed_example1(self):
        self.assertEqual(day2.SpecialArrayProduct([1, 2, 3, 4, 5]), [120, 60, 40, 30, 24], "basic example 1")
        
    def test_listed_example2(self):
        self.assertEqual(day2.SpecialArrayProduct([3, 2, 1]), [2, 3, 6], "basic example 2")


if __name__ == "__main__":
    unittest.main()