# https://leetcode.com/problems/ransom-note/
from collections import Counter


def canConstruct(ransomNote: str, magazine: str) -> bool:
    # v1
    # if len(ransomNote) > len(magazine):
    #     return False
    #
    # if ransomNote in magazine:
    #     return True
    #
    # count_n = Counter(ransomNote)
    # count_m = Counter(magazine)
    # return True if magazine.startswith(ransomNote) or magazine.endswith(
    #     ransomNote[::-1]) or count_n <= count_m else False

    # v2
    # if len(ransomNote) > len(magazine):
    #     return False
    #
    # count_n = Counter(ransomNote)
    # count_m = Counter(magazine)
    # return True if magazine.startswith(ransomNote) or magazine.endswith(
    #     ransomNote[::-1]) or ransomNote in magazine or count_n <= count_m else False

    # v3
    # for i in set(ransomNote):
    #     if magazine.count(i) > ransomNote.count(i):
    #         return False
    # return True

    # v4
    return Counter(magazine) >= Counter(ransomNote)

print(canConstruct("aa", "aab"))