from __future__ import annotations


def solve(data: str) -> int:
    """Simply return values based on input string data."""

    ans = 0
    data = data.strip()

    for i in data:
        if i == "(":
            ans += 1
        elif i == ")":
            ans -= 1

    return ans
