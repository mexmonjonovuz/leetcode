# https://leetcode.com/problems/counting-bits/description/
from typing import List


def countBits(n: int) -> List[int]:

    # version 1
    # result = []
    # for i in range(n + 1):
    #     result.append(bin(i).count("1"))
    # return result

    # version 2
    # result = []
    # i = 0
    # while i <= n:
    #     result.append(bin(i).count("1"))
    #     i += 1
    # return result

    # version 3
    # return [bin(i).count("1") for i in range(n + 1)]

    # version 4
    result = [0] * (n + 1)
    for i in range(1, n + 1):
        result[i] = result[i & (i - 1)] + 1
    return result



print(countBits(5))