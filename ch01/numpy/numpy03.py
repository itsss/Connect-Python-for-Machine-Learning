import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

b = a[:2, 1:3] #0~2 행 중 1~2 열 [2,3 \ 6,7]

#슬라이싱된 배열은 원본 배열과 같은 데이터를 참조함, 슬라이싱된 배열을 수정하면 원본 배열도 똑같이 변경
print(a[0,1])
b[0,0] = 77
print(a[0,1])
