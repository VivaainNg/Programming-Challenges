from __future__ import annotations

import unittest

from solution.problem_1 import solve as solve_1
from solution.problem_16 import solve as solve_16
from solution.problem_2 import solve as solve_2
from solution.problem_4 import solve as solve_4
from solution.problem_6 import solve as solve_6


class TestProjectEuler(unittest.TestCase):
    """
    Entire test suite of Project Euler challenges.
    """

    def test_1(self):
        """Problem 1 test case"""
        self.assertEqual(23, solve_1(10))
        self.assertEqual(233168, solve_1(1000))

    def test_2(self):
        """Problem 2 test case"""
        self.assertEqual(10, solve_2(10))
        self.assertEqual(44, solve_2(100))
        self.assertEqual(4613732, solve_2(4000000))

    def test_4(self):
        """Problem 4 test case"""
        self.assertEqual(9009, solve_4(2))
        self.assertEqual(906609, solve_4(3))

    def test_6(self):
        """Problem 6 test case"""
        self.assertEqual(2640, solve_6(10))
        self.assertEqual(25164150, solve_6(100))

    def test_16(self):
        """Problem 16 test case"""
        self.assertEqual(26, solve_16(15))
        self.assertEqual(1366, solve_16(1000))


if __name__ == '__main__':
    unittest.main()
