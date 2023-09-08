from pandas import *
from sys import *

xls = sys.argv[1]
df = xls.parse(xls.sheet_names[0])


siswa_nilai = {}

for i in range(5):
    name = input("Masukkan nama siswa: ")
    score = int(input(f"Masukkan nilai {name.capitalize()}: "))

    siswa_nilai[name] = score

print(siswa_nilai)

# check every score in each key if it meets the criteria of minimum score=75
for i in siswa_nilai:
    if(siswa_nilai[i]>=75):
        print(f"{i} lulus")
    else:
        print(f"{i} tidak lulus")