nilai = set({3,6,9,2,5,7})

for i in range(1,11):
    nilai.add(i)

print(nilai)

tbremoved = set({1,3,4,5,7,8,10})

print(nilai.difference(tbremoved))