from p2 import solve
import unittest

"""
Run this file with:
    $python -m unittest test_p2.py
    $pytest -v --no-header --durations=1 -vv test_p2.py
"""


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solve([1, 2, 3, 4, 5], [1, 2, 3, 4, 6]), 2)

    def test_2(self):
        self.assertEqual(solve([1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]), 0)

    def test_3(self):
        self.assertEqual(solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [
                         10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 0)

    def test_4(self):
        self.assertEqual(solve([1, 2, 3, 4, 5], [1, 2, 3, 4, 1]), 1)

    def test_5(self):
        self.assertEqual(solve([2, 2, 2, 2], [1, 2, 1, 2]), 2)

    def test_6(self):
        self.assertEqual(
            solve(
                [0, 10, 10, 10, 10, 100, 1000, 10000, 100000],
                [9, 9, 9, 9, 9, 1000, 100, 10000, 1]
            ),
            11
        )

    def test_7(self):
        self.assertEqual(
            solve(
                [1, 2, 3, 4, 5, 99, 1, 99, 1, 99, 1, 99],
                [6, 7, 8, 9, 10, 1, 99, 1, 99, 1, 1, 1]
            ),
            11
        )


if __name__ == "__main__":
    unittest.main()
