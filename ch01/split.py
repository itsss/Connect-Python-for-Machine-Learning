items = 'zero one two three'.split() #빈칸을 기준으로 문자열 나누기
print(items) # ['zero', 'one', 'two', 'three']

example = 'python,jquery,javascript'
example.split(",") # ','을 기준으로 문자열 나누기
a, b, c = example.split(",") #리스트에 있는 각 값을 a, b, c로 Unpacking
print(a)
print(b)
print(c)

example = 'cs50.gachon.edu'
subdomain, domain, tid = example.split(".") #리스트에 있는 각 값을 '.' 을 기준으로 subdomain, domain, tid 로 분리
print(subdomain)
print(domain)
print(tid)
