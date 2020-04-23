import unittest
import day1

class LearningCase(unittest.TestCase):
    def test_starting_out(self):
        self.assertEqual(day1.multiply(3, 4), 12)

def main():
    unittest.main()

if __name__ == "__main__":
    main()