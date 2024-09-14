# MEDIUM
# https://leetcode.com/problems/reverse-integer/description/
# def reverse(x: int) -> int:
#     if x == 0 or x > 2147483647 or x < -2147483648: return 0
#     result = str(x).rstrip('0')
#     if x > 0:
#         return int(result[::-1]) if int(result[::-1]) < 2147483647 else 0
#     return int('-' + (result[::-1]).rstrip('-')) if int('-' + (result[::-1]).rstrip('-')) > -2147483648 else 0
#
#
# print(reverse(1534236469))


# words = map(str, input().split())
# a, b = map(int, input().split())
# result = ""


# words = map(str, input().split())
# result = ""
# for i in words:
#     if i.startswith('Inf') or i.startswith('Info'):
#         result += i + " "
# result.rstrip()
# print(result)


# def make_sentence(*args):
#
#
# # return "".join([i + " " for i in args]).rstrip()
# # return " ".join(args)
#
# f
# print(make_sentence("Hello", "World", "Hi"))

#
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
#
# class Solution:
#     def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:  # noqa
#         pass
#
# tree_values = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
# root = build_tree(tree_values)
# solution = Solution()
# result = solution.deepestLeavesSum(root)

#
# def reverse_string(words: str):
#     if len(words) <= 1:
#         return words
#     return words[-1] + reverse_string(words[:-1])
#
#
# print(reverse_string("Asadbek"))


# def func(string: str) -> int:
#     count = 0
#     for i in range(len(string)-1):
#         if string[i] == 'h' and string[i+1] == 'i':
#             count += 1
#
#
#     return count
#
#
# print(func("hihi"))


# class Dog:
#
#
#     spec = "xaxa"
#     def __init__(self):
#         pass
#
#
#
# a = Dog()
# del Dog.spec
# print(a.spec)


# l = [1, 2, 3]
# print(sys.getrefcount(l))
#
#
# r = l
# print(sys.getrefcount(r))
#
#
# del r
# print(sys.getrefcount(l))
#
# import gc
#
# gc.enable()

#
# class A:
#     pass
#
#
# def a(d, b):
#     pass
#
#
# print(dir(A))

#
# from string import ascii_lowercase
#
# l = []
# for i in ascii_lowercase:
#     l.append(i)
#
#
# print(l)


# def stringHash(s: str, k: int) -> str:
#     result = ""
#     for i in range(0, len(s)):
#         print(s[i:k+i])
#     return ""
#
#
# print(stringHash("asadbek", 2))
