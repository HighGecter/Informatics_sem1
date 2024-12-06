D = dict()
N = int(input())
K = int(input())
A = []
for i in range(N):
    A.append(input())
for i in A:
    if i in D:
        D[i]+=1
    else:
        D[i]=1

A = list(D.values())
B = list(D.keys())
L = [[key, D[key]] for key in D]
L.sort(key=lambda x: x[0])
L = L[::-1]
print(L[:K])