result = []
for i in range(10):
    result.append(i)

print(result) #General

result = [i for i in range(10)]
print(result) #List Comprehension

result = [i for i in range(10) if i % 2 == 0]
print(result) #List Comprehension

#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#[0, 2, 4, 6, 8]
