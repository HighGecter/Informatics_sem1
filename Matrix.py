import numpy as np
num = input().split()
n = int(num[0])
m = int(num[1])
matrix = np.zeros((n,m))
x,y = 0, 0
matrix[0][0]=1
k,l= 0,1
end = 2
while end <= n*m:
    if 0<=x+k<=n-1 and 0<=y+l<=m-1 and matrix[x+k][y+l] == 0:
        matrix[x + k][y + l]=end
        end+=1
        x=x+k
        y=y+l
    elif l == 1:
         l=0
         k=1
    elif k == 1:
         k=0
         l=-1
    elif l == -1:
         l=0
         k=-1
    elif k==-1:
         k=0
         l=1
print(matrix, end='\n''\n')
for i in range (n):
    print(matrix[i,:]*(i+1))