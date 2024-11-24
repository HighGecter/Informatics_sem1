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



# A = [int(x) for x in input().split()]
# B = [0 for i in range(len(A))]
# def friends(A,B):
#     B[len(A)-1] = 0
#     for i in range(len(A)):
#         res = A[i]
#         for j in range(i, len(A)):
#             if res < A[j]:
#                 B[i] += 1
#                 res = A[j]
#     return B
#
# friends(A,B)
# print(*B)


# A = [int(x) for x in input().split()]
# B = [0 for i in range(len(A))]
# def friends(A,B):
#     B[len(A)-1] = 0
#     for i in range(len(A)):
#         res = A[i]
#         for j in range(i, len(A)):
#             if res < A[j]:
#                 B[i] += 1
#                 res = A[j]
#     return B
#
# friends(A,B)
# print(*B)











# def func(A):
#     B = [0 for i in range(len(A))]
#     i=-1
#     for word in A:
#         i+=1
#         for j in range(len(word)):
#             for k in range(j+1,len(word)):
#                 if word[j]>word[k] :
#                     B[i]+=1
#     C = [[A[i],B[i]] for i in range(len(A))]
#     for j in range(len(C) - 1):
#         for i in range(0, len(C) - 1 - j):
#             if C[i][1] > C[i + 1][1]:
#                 C[i], C[i + 1] = C[i + 1], C[i]
#
#
#     for word, _ in C:
#         print(word)
#     return
# K = int(input())
# for i in range(K):
#     n, m = map(int, input().split())
#     A = [0 for i in range(m)]
#     for j in range(m):
#       A[j] = input()
#     func(A)
#
#


A = [x for x in input().split()]
B = [0 for i in range(len(A))]
D = dict()
def insertion_sort(A):
    for i in range(1,len(A)):
        y = i
        while y > 0 and A[y] < A[y-1]:
            A[y], A[y-1] = A[y-1], A[y]
            y -= 1
    return A

for i in range(len(A)):
    B[i] = ''.join(insertion_sort(list(A[i])))
    if B[i] in D:
        D[B[i]].append(A[i])
    else:
        D[B[i]] = [A[i]]
L = [[key, D[key]] for key in D]
M = []
V = []
for i in range(1, len(L)):
    y = i
    while y > 0 and len(L[y][1]) > len(L[y-1][1]):
        L[y], L[y-1] = L[y-1], L[y]
        y -= 1
for key,words in L:
    if len(words)==1:
        N = insertion_sort(words)
        V+=N
    else:

       N = insertion_sort(words)
       M+=N
V = insertion_sort(V)

M+=V


print(*M)


