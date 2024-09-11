from __future__ import annotations

# import time


def solve(n: int) -> int:
    """
    * n = First n natural numbers

    """

    # Brute-force way

    # start = time.time()

    sum_of_squares = sum([i**2 for i in range(1, n+1)])
    squares_of_sum = sum([i for i in range(1, n+1)]) ** 2

    # end = time.time()

    # print(f"Elapsed time: {round(end - start, 2)} secs")

    return squares_of_sum - sum_of_squares


if __name__ == '__main__':
    ans = solve(10)
    print(ans)
