alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a,b in zip(alist, blist): #병렬적으로 값을 추출
    print(a,b

#a1 b1
#a2 b2
#a3 b3

a,b,c=zip((1,2,3), (10,20,30), (100,200,300)) #각 tuple의 같은 index끼리 묶음
print(a)
print(b)
print(c)
#(1, 10, 100)
#(2, 20, 200)
#(3, 30, 300)

print([sum(x) for x in zip ((1,2,3),(10,20,30),(100,200,300))])
# [111, 222, 333]
