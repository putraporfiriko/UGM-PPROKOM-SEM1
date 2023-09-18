a = set({'a','b','c','d'})
b = set({'c','d','e'})
c = set({})

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
print(a.symmetric_difference(c))
print(b.symmetric_difference(c))
