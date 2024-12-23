# https://leetcode.com/problems/counting-bits/description/
from typing import List


def countBits(n: int) -> List[int]:
    return [bin(i).count("1") for i in range(n + 1)]


print(countBits(5))