from __future__ import annotations


def solve(n: int) -> int:
    ans = 0

    for i in range(1, n):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    return ans


if __name__ == '__main__':
    # Problem 1"
    print(solve(1000))
