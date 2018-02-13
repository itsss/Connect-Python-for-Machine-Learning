import numpy as np

x = np.array([[1,2],[3,4]], dtype = np.float64)
y = np.array([[5,6],[7,8]], dtype = np.float64)

#[[6.0 8.0][10.0 12.0]] 1+5, 2+6, 3+7, 4+8
print(x+y)
print(np.add(x,y))

#[[-4.0 -4.0][-4.0 -4.0]] 1-5, 2-6, 3-7, 4-8
print(x-y)
print(np.subtract(x,y))

#[[5.0 12.0][21.0 32.0]] 1*5, 2*6, 3*7, 4*8
print(x*y)
print(np.multiply(x,y))

#[[0.2 0.333][0.428 0.5]] 1/5, 2/6, 3/7, 4/8
print(x/y)
print(np.divide(x,y))

#[[1 1.414][1.732 2.]]
print(np.sqrt(x))
