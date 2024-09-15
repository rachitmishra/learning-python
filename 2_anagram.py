# def is_anagram(a, b):
#     blist = list(b)
#     for i in a:
#         for j in blist:
#             print(i + " " + j)
#             if i == j:
#                 blist.remove(j)
#
#     if len(blist) == 0:
#         return True
#     return False
#

# ∑i=1n, i=n(n+1)2=1/2n2+1/2n
# ∑i=1n, i=n(n+1)2=1/2n2+1/2n

#     alist = list(a)
#     alist.sort()
#     blist = list(b)
#     blist.sort()
#     isanagram = True
#     for i in range(0, len(alist)):
#         if alist[i] == blist[i]:
#             isanagram = True
#         else:
#             isanagram = False
#
#     return isanagram
#

# O(n2) or O(nlogn) because of sort calls

#     c1 = [0] * 26
#     c2 = [0] * 26
#
#     for i in range(len(a)):
#         pos = ord(a[i]) - ord('a')
#         c1[pos] = c1[pos] + 1
#
#     for i in range(len(b)):
#         pos = ord(b[i]) - ord('a')
#         c2[pos] = c2[pos] + 1
#
#     j = 0
#     isanagram = True
#     while j < 26 and isanagram:
#         if c1[j] == c2[j]:
#             j = j + 1
#         else:
#             isanagram = False
#
#     return isanagram


# print(is_anagram('apple', 'pleap'))

# 2n + 26 = O(n)
