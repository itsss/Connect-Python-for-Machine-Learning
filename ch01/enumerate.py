for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)

mylist =["a","b","c","d"]
list(enumerate(mylist)) #list에 있는 index와 값을 unpacking하여 list에 저장
{i:j for i,j in enumerate('Gachon University is an academic institute located in South Korea.'.split())}
#문장을 list로 만들고 list의 index와 값을 unpacking하여 dict로 저장
#{0: 'Gachon', 1: 'University', 2: 'is', 3: 'an', 4: 'academic', 5: 'institute', 6: 'located', 7: 'in', 8: 'South', 9: 'Korea.'}
