a = set({'a','b','c','d'})
b = set({'c','d','e'})
c = set({})

print(a.difference(b))
print(b.difference(a))
print(a.difference(c))
print(b.difference(c))
