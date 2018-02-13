words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)

stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print(i)

#['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
#['THE', 'the', 3]
#['QUICK', 'quick', 5]
#['BROWN', 'brown', 5]
#['FOX', 'fox', 3]
#['JUMPS', 'jumps', 5]
#['OVER', 'over', 4]
#['THE', 'the', 3]
#['LAZY', 'lazy', 4]
#['DOG', 'dog', 3]
