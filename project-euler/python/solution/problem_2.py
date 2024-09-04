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
    # fib[2] = 3...
    fib.append(1)
    fib.append(2)
    i = 2

    while True:
        fib_i = fib[i-2] + fib[i-1]

        # We consider n to be limit of the Fibonacci's term
        if fib_i < n:
            fib.append(fib_i)
            i += 1
        else:
            break

    # Compute sum of even numbers
    ans = 0
    for i in fib:
        if i % 2 == 0:
            ans += i

    return ans


if __name__ == '__main__':
    solve(10)
