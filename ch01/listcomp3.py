case_1 = ["A", "B", "C"]
case_2 = ["D", "E", "A"]

result = [i+j for i in case_1 for j in case_2]
print(result)

result = [i+j for i in case_1 for j in case_2 if not(i==j)]
print(result)

result.sort()
print(result)


#['AD', 'AE', 'AA', 'BD', 'BE', 'BA', 'CD', 'CE', 'CA']
#['AD', 'AE', 'BD', 'BE', 'BA', 'CD', 'CE', 'CA']
#['AD', 'AE', 'BA', 'BD', 'BE', 'CA', 'CD', 'CE']
