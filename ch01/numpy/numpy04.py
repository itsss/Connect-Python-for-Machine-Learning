import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

#정수 인덱싱과 슬라이싱을 혼합해서 사용하면 낮은 rank의 배열이 생성됨
row_r1 = a[1,:]
#슬라이싱만 사용하면 원본 배열과 동일한 rank의 배열이 생성됨.
row_r2 = a[1:2, :]
print(row_r1, row_r1.shape) #[5,6,7,8] (4,)
print(row_r2, row_r2.shape) #[[5,6,7,8]] (1,4)

#행이 아닌 열도 동일하게 적용됨
col_r1 = a[:, 1]
col_r2 = a[:, 1:2]
print(col_r1, col_r1.shape) #[2 6 10] (3,)
print(col_r2, col_r2.shape)
# [[2]
#  [6]
#  [10]]
# (3,1)
