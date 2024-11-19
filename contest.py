# A = [int(x) for x in input().split()]
# def dig_root(A):
#     while A >= 10:
#         A = sum(int(d) for d in str(A))
#     return A
#
# def insertion_sort(A):
#     for i in range(1,len(A)):
#         y = i
#         while y > 0:
#             if dig_root(A[y]) <= dig_root(A[y-1]):
#                 A[y], A[y-1] = A[y-1], A[y]
#                 y -= 1
#             elif dig_root(A[y]) == dig_root(A[y-1]) and A[y]<A[y-1]:
#                 A[y], A[y - 1] = A[y - 1], A[y]
#                 y -= 1
#             else:
#                 break
#
#
# insertion_sort(A)
# print(*A)

# A =[int(x) for x in input().split()]
# B = [0 for i in range(len(A))]
# def building(A, B):
#     for i in range(len(A)):
#         B[0] = -1
#         y = i
#         while y > 0:
#             y -=1
#             if A[i] <= A[y]:
#                 B[i] = y
#                 break
#             elif A[i] > A[y] and y == 0:
#                 B[i] = -1
#
#     return B
#
# building(A,B)
# print(*B)

A = [int(x) for x in input().split()]
B = [0 for i in range(len(A))]
def friends(A,B):
    B[len(A)-1] = 0
    for i in range(len(A)):
        res = A[i]
        for j in range(i, len(A)):
            if res < A[j]:
                B[i] += 1
                res = A[j]
    return B

friends(A,B)
print(*B)
