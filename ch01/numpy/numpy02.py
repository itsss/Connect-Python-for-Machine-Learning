import numpy as np

a = np.zeros((2,2))
print(a) #모든 값이 0인 2*2 행렬

b = np.ones((1,2))
print(b) #모든 값이 1인 1*2 행렬

c = np.full((2,2), 7)
print(c) #모든 값이 7인 2*2 행렬

d = np.eye(2) #2*2 단위 행렬 생성
print(d)

e = np.random.random((2,2)) #임의의 값으로 채워진 행렬 생성
print(e)
