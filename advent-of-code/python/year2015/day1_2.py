from __future__ import annotations


def solve(data: str) -> int:
    data = data.strip()
    ans = 0

    for i, val in enumerate(data):
        if val == '(':
            ans += 1
        elif val == ')':
            ans -= 1

        if ans == -1:
            return i+1
    return ans
