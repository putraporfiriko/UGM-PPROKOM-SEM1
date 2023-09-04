siswa_nilai = {}

for i in range(5):
    name = input("Masukkan nama siswa: ")
    score = int(input(f"Masukkan nilai {name.capitalize}: "))

    siswa_nilai[name] = score

print(siswa_nilai)

# check every score in each key if it meets the criteria of minimum score=75
for i in siswa_nilai:
    if(siswa_nilai[i]>=75):
        print(f"Siswa {i} lulus")
    else:
        print(f"Siswa {i} tidak lulus")