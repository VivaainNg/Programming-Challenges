from __future__ import annotations


def solve(n: int) -> int:
    """
    Use memoization to store values and build the Fibonacci values from
    ground-up using arrays.
    """

    fib = []

    # Initial two values:
    # fib[0] = 1
    # fib[1] = 2
    # fib[2] = 3  # starts with index i=2
    fib.append(1)
    fib.append(2)
    i = 2

    ans = 2  # Based on even numbers initialized for 1st two values

    while True:
        fib_i = fib[i-2] + fib[i-1]

        # As long as final Fibonacci's value in array doesn't exceed n
        if fib_i < n:
            fib.append(fib_i)
            i += 1
        else:
            break

        # Compute sum of even numbers
        if fib_i % 2 == 0:
            ans += fib_i

    return ans


if __name__ == '__main__':
    solve(10)
