a = set({100,7,8})
b = set({200,4,5})
c = set({300,2,3})
d = set({100,200,300})

print(a.union(d))
print(b.union(d))
print(b.union(c.union(d)))
print(a.union(b.union(c.union(d))))