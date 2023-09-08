siswa_nilai = {}

for i in range(5):
    name = input("Masukkan nama siswa: ")
    score = int(input(f"Masukkan nilai {name.capitalize()}: "))

    siswa_nilai[name] = score


for i in siswa_nilai:
    if(siswa_nilai[i]>=75):
        print(f"{i.capitalize()} lulus")
    else:
        print(f"{i.capitalize()} tidak lulus")   