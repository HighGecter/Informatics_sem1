import time
import random
import matplotlib.pyplot as plt

def bubble_sort(A):
    for j in range(len(A)-1):
         for i in range(0,len(A)-1-j):
             if A[i] > A[i+1]:
                 A[i] , A[i+1] = A[i+1] , A[i]
    return A

n = 10
Y=[]
X=[int(x) for x in range(1,200)]
for i in range(1,200):
    data_sample = [random.randint(1, 50) for j in range(i)]
    total_time = 0
    for i in range(n):
        data_copy = data_sample.copy()
        start = time.time()
        bubble_sort(data_copy)
        end = time.time()

        total_time += (end - start)
    average_time = total_time / n
    Y.append(average_time)
plt.plot(X,Y,label='bubble sort')


#choice sort
def func(A):
    res = 0
    for i in range(1, len(A)):
        if A[i] >= A[res]:
            res = i
    return res

def choice_sort(A):
    for i in range(len(A)-1):
        B=A[0:len(A)-i:]
        A[func(B)],A[len(A)-i-1]=A[len(A)-i-1],A[func(B)]
A = []
B = [int(x) for x in range(1,200)]
for i in range(1,200):
    data_sample = [random.randint(1, 50) for j in range(i)]
    total_time = 0
    for i in range(n):
        data_copy = data_sample.copy()
        start = time.time()
        choice_sort(data_copy)
        end = time.time()

        total_time += (end - start)
    average_time = total_time / n
    A.append(average_time)
plt.plot(B,A,'r',label='choice sort')


#insertion
def insertion_sort(A):
    for i in range(1,len(A)):
        y = i
        while y > 0 and A[y] < A[y-1]:
            A[y], A[y-1] = A[y-1], A[y]
            y -= 1
F = []
E = [int(x) for x in range(1,200)]
for i in range(1,200):
    data_sample = [random.randint(1, 50) for j in range(i)]
    total_time = 0
    for i in range(n):
        data_copy = data_sample.copy()
        start = time.time()
        insertion_sort(data_copy)
        end = time.time()

        total_time += (end - start)
    average_time = total_time / n
    F.append(average_time)
plt.plot(E,F,'y',label='insertion sort')
plt.show()