from collections import deque

deque_list = deque()
for i in range(5):
    deque_list.append(i) #Queue 오른쪽에 추가
print(deque_list)

deque_list.appendleft(100) #Queue 왼쪽에 100 추가
print(deque_list)

deque_list.rotate(2) #2칸 순환, 뒤에 있는 2칸은 앞으로
print(deque_list)

deque_list.rotate(2) #2칸 순환, 뒤에 있는 2칸은 앞으로
print(deque_list)

print(deque(reversed(deque_list))) #역순으로 데이터 뒤집기

print('a')
deque_list.extend([5, 6, 7])
print(deque_list)

deque_list.extendleft([5, 6, 7])
print(deque_list)
