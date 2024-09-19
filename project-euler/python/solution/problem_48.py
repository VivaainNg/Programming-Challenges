from __future__ import annotations


def solve(n: int) -> str:
    """
    Function to find the last 10 digits based on series of
    1^1 + 2^2 + 3^3 + ... + n ^ n.
    """

    # TODO: Optimize the brute force way
    num = sum([i ** i for i in range(1, n+1)])

    counter = 0
    ans = ''

    while counter < 10:
        digit = num % 10
        num = num // 10
        ans = f'{digit}{ans}'
        counter += 1

    return ans
