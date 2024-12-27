# https://leetcode.com/problems/reverse-integer/description/


def reverse(x: int) -> int:
    if x == 0 or x > 2147483647 or x < -2147483648: return 0
    result = str(x).rstrip('0')
    if x > 0:
        return int(result[::-1]) if int(result[::-1]) < 2147483647 else 0
    return int('-' + (result[::-1]).rstrip('-')) if int('-' + (result[::-1]).rstrip('-')) > -2147483648 else 0


print(reverse(1534236469))



