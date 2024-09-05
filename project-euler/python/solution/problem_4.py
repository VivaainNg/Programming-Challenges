from __future__ import annotations


def solve(n: int) -> int:
    """
    * n represents the number of digits

    Brute-force way, starting from pairs as shown in pairs below:
    - (99 x 99)
    - (99 x 98)
    - (99 x 97)
    ...
    ...
    - (10 x 11)
    - (10 x 10)
    """

    startNum = 10 ** (n-1)
    endNum = 10 ** n
    ans = 0

    for i in range(startNum, endNum):
        for j in range(startNum, endNum):
            product = i * j

            if str(product)[::-1] == str(product):
                ans = max(ans, product)

    # TODO: Optimize this to find a better solution
    # If you print the above iterations, you would notice that
    # when i = 99 & j = 10, produce similar results as
    # when j = 10 & i = 99. Try to reduce redundant counting
    # like these.

    return ans


if __name__ == '__main__':
    ans = solve(2)
    print(ans)
