import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11,12])

# 벡터의 내적 (Vx*Wx)+(Vy*Wy)
print(v.dot(w))
print(np.dot(v, w))

# 행렬과 벡터의 곱
print(x.dot(v))
print(np.dot(x, v)) #[29 67]

# 행렬곱 [[19 22][43 50]]
print(x.dot(y))
print(np.dot(x,y))

# numpy에서 유용한 sum
print(np.sum(x)) # 모든 요소를 합한 값을 연산 10
print(np.sum(x, axis=0)) # 각 열에 대한 합을 연산 [4 6]
print(np.sum(x, axis=1)) # 각 행에 대한 합을 연산 [3 7]

# 전치행렬 구하기
print(x.T) #[[1 3][2 4]]

# 단, rank 1인 배열을 전치하는 경우 아무런 일도 일어나지 않음
print(v.T) #[9 10]
