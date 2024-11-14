import time
import random
import matplotlib.pyplot as plt



def merge(A, B):
    res = []
    i = 0
    j = 0
    while i < len(A):
        if A[i] > B[j]:
            A, B = B, A
            i, j = j, i
        res.append(A[i])
        i += 1
    res += A[i:] + B[j:]
    return res

def mergesort(A):
    if len(A) < 2:
        return A
    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]
    return merge(mergesort(left), mergesort(right))


n = 10
Y=[]
X=[int(x) for x in range(1,500)]
for i in range(1,500):
    data_sample = [random.randint(1, 10000) for j in range(i)]
    total_time = 0
    for i in range(n):
        data_copy = data_sample.copy()
        start = time.time()
        mergesort(data_copy)
        end = time.time()

        total_time += (end - start)
    average_time = total_time / n
    Y.append(average_time)
plt.plot(X,Y,label='mergesort')

def qsort(A, left = 0, right =  None):
    if right is None:
        right = len(A)-1
    if left >= right:
        return
    i = left
    j = right
    pivot = A[left]
    while i <= j:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i <= j:
            A[i],  A[j] = A[j], A[i]
            i += 1
            j -= 1
    qsort(A, left, j)
    qsort(A,i,right)

B=[]
A=[int(x) for x in range(1,500)]
for i in range(1,500):
    data_sample = [random.randint(1, 10000) for j in range(i)]
    total_time = 0
    for i in range(n):
        data_copy = data_sample.copy()
        start = time.time()
        qsort(data_copy)
        end = time.time()

        total_time += (end - start)
    average_time = total_time / n
    B.append(average_time)
plt.plot(A,B,label='qsort', alpha = 0.8)


def heap_pop(A):
    res = A[0]
    if len(A) == 1:
        return res
    A[0] = A.pop()
    i = 0
    j = 2 * i + 1
    k = 2 * i + 2
    while j < len(A):
        c = j
        if k < len(A) and A[j] < A[k]:
            c = k
        if A[i] < A[c]:
            A[i], A[c] = A[c], A[i]
            i = c
        else:
            break
        j = 2 * i + 1
        k = 2 * i + 2
    return res

def heap_sort(A):
    heap = []
    for element in A:
        heap_add(heap, element)
    for i in range(len(A)):
        A[len(A) - 1 - i] = heap_pop(heap)

E=[]
F=[int(x) for x in range(1,500)]
for i in range(1,500):
    data_sample = [random.randint(1, 10000) for j in range(i)]
    total_time = 0
    for i in range(n):
        data_copy = data_sample.copy()
        start = time.time()
        qsort(data_copy)
        end = time.time()

        total_time += (end - start)
    average_time = total_time / n
    E.append(average_time)
plt.plot(F,E,label='heap_sort', alpha = 0.8)
plt.legend()
plt.show()