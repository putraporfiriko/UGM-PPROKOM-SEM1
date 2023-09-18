a = set({100,7,8})
b = set({200,4,5})
c = set({300,2,3})
d = set({100,200,300})

print(a.intersection(d))
print(b.intersection(d))
print(c.intersection(d))
print(a.intersection(b.intersection(c.intersection(d))))