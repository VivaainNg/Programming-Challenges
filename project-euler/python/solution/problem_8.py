from __future__ import annotations


def solve(n: str, adj: int) -> int:
    """
    - n represents the multi-line 1000-digit number in string
    - adj represents the number of adjacent digits.
    """

    # Clean the input to remove newline spaces and
    # join into a single numeric line
    numeric_line = ''.join([i for i in n.split()])

    ans = 0

    # Brute force method by using sliding window with a size of adj
    for i in range(0, len(numeric_line) - adj + 1):
        window = numeric_line[i:i+adj]

        val = 1
        for num in window:
            val *= int(num)

        ans = max(ans, val)

    return ans
