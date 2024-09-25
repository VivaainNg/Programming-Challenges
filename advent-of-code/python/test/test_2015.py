from __future__ import annotations

import os

import unittest

from year2015.day1 import solve as solve1


class TestAOC2015(unittest.TestCase):
    """
    Entire test suite of year 2015.
    """

    PATH_TO_INPUT_DIRECTORY = "../../inputs/2015"

    def test_1_1(self):
        """Day 1 Part 1 test case"""

        file_name = "day1_1.txt"

        current_path = os.path.dirname(__file__)

        input_path = os.path.join(current_path, self.PATH_TO_INPUT_DIRECTORY, file_name)

        ans = 0

        if os.path.exists(input_path):
            f = open(input_path)
            data = f.read()
            ans = solve1(data)
            f.close()


        self.assertEqual(0, solve1("(())"))
        self.assertEqual(0, solve1("()()"))
        self.assertEqual(3, solve1("((("))
        self.assertEqual(3, solve1("(()(()("))
        self.assertEqual(3, solve1("))((((("))
        self.assertEqual(-1, solve1("())"))
        self.assertEqual(-1, solve1("))("))
        self.assertEqual(-3, solve1(")))"))
        self.assertEqual(-3, solve1(")())())"))
        self.assertEqual(280, solve1(data))
