#задача про високосный год
a=int(input())
if a%4==0 and a%100!=0 or a%400==0:
    print('YES')
else:
 print('NO')

#задача про треугольник
a=input()
b=input()
c=input()
if a+b>c and a+c>b and c+b>a:
    print('YES')
else:
    print('NO')


#задача про корни квадратного уравнения
a=float(input())
b=float(input())
c=float(input())
d=(-b+(b**2-4*a*c)**0.5)/2*a
f=(-b-(b**2-4*a*c)**0.5)/2*a
if d!=0 and f!=0:
    print(d,f)
elif f!=0:
    print(f)
elif d!=0:
    print(d)
elif a==0:
    if c==0 and b==0:
        print('INFINITY')
    elif c!=0 and b!=0:
        print(-c/b)


#задача про ферзя
q_line=int(input())
q_row=int(input())
f_line=int(input())
f_row=int(input())
if q_row==f_row or q_line==f_line:
 print('YES')
elif q_line-f_line==q_row-f_row or q_line-f_line==f_row-q_row:
 print('YES')
else:
 print('NO')


#задача про линейный поиск
N=int(input())
A=[int(x) for x in input().split()]
x=int(input())
B=[]
for i in range(N):
    if A[i]==x:
        B.append(x)
print(len(B))


#поиск числа положительных чисел в массиве
N=int(input())
A=[int(x) for x in input().split()]
B=[]
for i in range(N):
    if A[i]>0:
        B.append(1)
print(len(B))


#поиск максимального числа в массиве
N=int(input())
A=[int(x) for x in input().split()]
max=A[0]
for i in range(len(A)):
    if A[i]>max:
      max=A[i]
print(max)


#циклический сдвиг
N=int(input())
A=[int(x) for x in input().split()]
B=[]
for i in range(len(A)):
    B.append(A[i-1])
print(B)


#ревизия
N=int(input())
A=[int(x) for x in input().split()]
a=min(A)
A.remove(min(A))
b=min(A)
A.remove(min(A))
print(a,b)