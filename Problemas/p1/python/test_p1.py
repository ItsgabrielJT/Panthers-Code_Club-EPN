from p1 import solve
import unittest

"""
Run this file with:
    $python -m unittest test_p1.py
    $pytest -v --no-header --durations=1 -vv test_p1.py
"""


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solve([1, 1, 1, 1, 1]), 1)

    def test_2(self):
        self.assertEqual(solve([10, 9, 8]), 10)

    def test_3(self):
        self.assertEqual(solve([1, 2, 3]), 3)

    def test_4(self):
        self.assertEqual(solve([1, 2, 2]), 2)

    def test_5(self):
        self.assertEqual(solve([1, 1000000]), 500001)

    def test_6(self):
        self.assertEqual(solve([3, 8, 6, 7, 4, 1, 2, 4, 10, 1]), 9)


if __name__ == "__main__":
    unittest.main()
