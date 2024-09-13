from __future__ import annotations


def solve(n: int) -> int:
    """n represents the power"""

    num = 2 ** n
    ans = 0

    while num > 0:
        ans += num % 10
        num = num // 10

    return ans


if __name__ == '__main__':
    solve(15)
