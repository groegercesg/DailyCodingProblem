import unittest
from day3 import Node


class Day3UnitTests(unittest.TestCase):
    def test_listed_example(self):
        node = Node('root', Node('left', Node('left.left')), Node('right'))
        self.assertEqual(Node.deserialize(Node.serialize(node)).left.left.val,
                         'left.left', "listed example")


if __name__ == "__main__":
    unittest.main()
