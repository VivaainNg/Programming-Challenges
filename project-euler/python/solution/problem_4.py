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

    # TODO: Optimize this to find a better solution

    startNum = 10 ** (n-1)
    endNum = 10 ** n
    ans = 0

    for i in range(startNum, endNum):
        for j in range(startNum, endNum):
            product = i * j

            if str(product)[::-1] == str(product):
                ans = max(ans, product)

    return ans


if __name__ == '__main__':
    # ans = solve(2)
    ans = solve(3)
    print(ans)
