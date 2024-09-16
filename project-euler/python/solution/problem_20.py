from __future__ import annotations


def solve(n: int) -> int:

    # TODO: Optimize this brute-force method
    factorial, ans = 1, 0

    for i in range(2, n+1):
        factorial *= i

    while factorial > 0:
        ans += factorial % 10
        factorial = factorial // 10

    return ans


if __name__ == '__main__':
    solve(10)
