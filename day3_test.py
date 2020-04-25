import unittest
import day3


class Day3UnitTests(unittest.TestCase):
    def test_listed_example(self):
        node = day3.Node('root', day3.Node('left', day3.Node('left.left')),
                         day3.Node('right'))
        self.assertEqual(day3.deserialize(day3.serialize(node)).left.left.val,
                         'left.left', "listed example")


if __name__ == "__main__":
    unittest.main()
