import unittest
import day1

class Day1UnitTests(unittest.TestCase):
    def test_listed_example(self):
        self.assertEqual(day1.AddToK([10, 15, 3, 7], 17), True, "10+7 == 17")
        
    def test_none_case(self):
        self.assertEqual(day1.AddToK([10, 15, 3, 7], 2), None, "10+15 =/= 2")
    
    def test_small_true(self):
        self.assertEqual(day1.AddToK([9,2], 11), True, "9+2 == 11")
        
    def test_large_true(self):
        self.assertEqual(day1.AddToK([1,2,3,4,5,6,7,8,9,10,11,32,1231,123,252,412,523,52134521,15,14], 29), True, "15+14 == 29")
        
    def test_small_none(self):
        self.assertEqual(day1.AddToK([9,2], 10), None, "9+2 =/= 10")
        
    def test_large_none(self):
        self.assertEqual(day1.AddToK([1,2,3,4,5,6,7,8,9,10,11,32,1231,123,252,412,523,52134521,15,14], 1001), None, "1+2 =/= 1001")


if __name__ == "__main__":
    unittest.main()