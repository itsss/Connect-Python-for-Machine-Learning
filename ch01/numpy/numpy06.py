import numpy as np

a = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
print(a)

b = np.array([0, 2, 0, 1])
print(a[np.arange(4), b]) # 1번째 행 0번째 데이터 - 1, 2번째 행 2번째 데이터 - 6, 3번째 행 0번째 데이터 - 7, 4번째 행 1번째 데이터 - 11

a[np.arange(4), b] += 10
print(a) #b Index에 해당하는 값에 전부 10을 더함 (11, 16, 17, 21)
