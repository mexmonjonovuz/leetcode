# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/description/


def findTheLongestBalancedSubstring(s: str) -> int:
    """
    berilgan satr ichidan "01" substringni bor yo'qligi orqali tekshirib chiqamiz va shu substringni kengaytirib boramiz.
    0 <- 01 -> 1 shunda 0011 --> (000111) length shu ko'rinishda string kengayib boraveramiz berilgan string max leng
    uzunligigacha . Oxirida manual qo'shgan '01' uzunligimizni ayirib tashlashimiz zarur shunda
    substring max lenthga erishamiz .
    """

    # v1
    # tmp = "01"
    # for i in range(len(s)):
    #     if tmp in s:
    #         tmp = "0" + tmp + "1"
    # return len(tmp) - 2

    # v2
    tmp = "01"
    while tmp in s:
        tmp = "0" + tmp + "1"
    return len(tmp) - 2


print(findTheLongestBalancedSubstring("01000111"))
