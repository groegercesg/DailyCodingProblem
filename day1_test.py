import unittest
import day1

class Day1UnitTests(unittest.TestCase):
    def test_listed_example(self):
        self.assertEqual(day1.AddToK([10, 15, 3, 7], 17), True, "10+7 ?= 17")


if __name__ == "__main__":
    unittest.main()