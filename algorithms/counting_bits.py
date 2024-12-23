# https://leetcode.com/problems/counting-bits/description/
from typing import List


def countBits(n: int) -> List[int]:
    result = []
    for i in range(n + 1):
        result.append(bin(i).count("1"))
    return result


print(countBits(5))