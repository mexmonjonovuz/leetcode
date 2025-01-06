# https://leetcode.com/problems/remove-element/description/
from typing import List


def removeElement(nums: List[int], val: int) -> int:
    idx = 0
    i = 0
    while i < len(nums):
        if nums[i] != val:
            nums[idx] = nums[i]
            idx += 1
        i += 1
    return idx


print(removeElement([3, 2, 2, 3], 2))
