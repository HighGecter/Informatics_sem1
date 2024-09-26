import numpy as np
y = np.array(list(input())).astype(int)
x= np.array(list(input())).astype(int)
a=(np.mean(x*y)-np.mean(x)*np.mean(y))/(np.mean(x**2)-np.mean(x)**2)
b=np.mean(y)-a*np.mean(x)
print(a)
print(b)