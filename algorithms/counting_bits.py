# https://leetcode.com/problems/counting-bits/description/
from typing import List


def countBits(n: int) -> List[int]:
    result = []
    i = 0
    while i <= n:
        result.append(bin(i).count("1"))
        i += 1
    return result


print(countBits(5))