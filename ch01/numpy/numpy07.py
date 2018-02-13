import numpy as np

a = np.array([[1,2], [3,4], [5,6]])
bool_idx = (a > 2) #2 초과 요소 True, False로 구분
print(bool_idx) # True, False 구분 출력
print(a[bool_idx]) #2 초과 요소만 배열로 표시

print(a[a>2]) #2 초과 요소만 배열로 표시
