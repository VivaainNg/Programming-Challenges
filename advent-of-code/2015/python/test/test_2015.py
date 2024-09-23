from __future__ import annotations

import unittest

from solution.day1 import solve as solve_1


class TestAOC2015(unittest.TestCase):
    """
    Test suite for year 2015.
    """

    def test_day1(self):
        """Day 1 test case"""
        self.assertEqual(123, solve_1())
