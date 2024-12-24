# https://leetcode.com/problems/valid-perfect-square/description/


def isPerfectSquare(num: int) -> bool:
    # version 1
    # return int(num ** 0.5) * int(num ** 0.5) == num

    # version 2
    return (num ** 0.5) % 1 == 0


print(isPerfectSquare(14))
