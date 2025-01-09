# https://leetcode.com/problems/string-matching-in-an-array/?envType=daily-question&envId=2025-01-07
from typing import List


def stringMatching(words: List[str]) -> List[str]:
    # v1
    # answer = []
    # for i in range(len(words)):
    #     for j in range(len(words)):
    #         if words[j] in words[i] and len(words[i]) > len(words[j]):
    #             answer.append(words[j])
    # return list(set(answer))

    # v2
    # return list(set([words[j] for i in range(len(words)) for j in range(len(words)) if
    #                  words[j] in words[i] and len(words[i]) > len(words[j])]))

    # v3
    # return list(set(words[j] for i in range(len(words)) for j in range(len(words)) if
    #          words[j] in words[i] and len(words[i]) > len(words[j])))

    # v4                   # v4 -> v1                                                # v4 -> v2
    return list(i for i in words if " ".join(words).count(i) > 1)  # or  [i for i in words if " ".join(words).count(i) > 1]


print(stringMatching(["mass", "as", "hero", "superhero"]))