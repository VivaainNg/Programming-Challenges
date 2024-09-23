from __future__ import annotations

import unittest

from year2015.day1 import solve as solve1


class TestAOC2015(unittest.TestCase):
    """
    Entire test suite of year 2015.
    """

    def test_1(self):
        """Day 1 test case"""
        self.assertEqual(23, solve1())
