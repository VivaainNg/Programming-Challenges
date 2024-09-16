from __future__ import annotations


def solve(num: str) -> int:
    """
    Argument num contains lines of numerical digits in string format,
    separated by newline.
    """

    # TODO: Is there a better way to optimize brute-force approach below?

    lines = list(num.split('\n'))

    # Format into list containing integer, and sum them up
    total = sum([int(line) for line in lines if line.strip()])

    # Returns only the first 10 digit
    ans = str(total)[:10]
    return int(ans)


if __name__ == '__main__':
    solve('0')
