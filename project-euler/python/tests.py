from __future__ import annotations

import unittest

from solution.problem_1 import solve as solve_1
from solution.problem_2 import solve as solve_2
from solution.problem_4 import solve as solve_4


class TestProjectEuler(unittest.TestCase):
    """
    Entire test suite of Project Euler challenges.
    """

    def test_1(self):
        """Problem 1 test case"""
        self.assertEqual(23, solve_1(10))

    def test_2(self):
        """Problem 2 test case"""
        self.assertEqual(4613732, solve_2(4000000))

    def test_4(self):
        """Problem 4 test case"""
        self.assertEqual(9009, solve_4(2))
        self.assertEqual(906609, solve_4(3))


if __name__ == '__main__':
    unittest.main()
