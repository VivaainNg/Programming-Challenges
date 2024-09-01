from __future__ import annotations

import unittest

from solution.problem_1 import solve as solve_1


class TestProjectEuler(unittest.TestCase):
    """
    Entire test suite of Project Euler challenges.
    """

    def test_1(self):
        self.assertEqual(23, solve_1(10))


if __name__ == '__main__':
    unittest.main()
