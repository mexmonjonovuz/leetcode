# https://leetcode.com/problems/lexicographical-numbers/description/
from typing import List


def lexicalOrder(n: int) -> List[int]:

    # version 1
    # temp = []
    # result = []
    # for i in range(1, n + 1):
    #     temp.append(str(i))
    # temp.sort()
    # for j in temp:
    #     result.append(int(j))
    # return result

    # version 2
    # return [int(j) for j in sorted([str(i) for i in range(1, n + 1)])]

    # version 3
    answer = []
    curr = 1

    for _ in range(n):
        answer.append(curr)
        if curr * 10 <= n:
            curr *= 10
        else:
            while curr % 10 == 9 or curr + 1 > n:
                curr //= 10
            curr += 1
    return answer


print(lexicalOrder(100))
