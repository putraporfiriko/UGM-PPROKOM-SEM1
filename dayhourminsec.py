n = int(input("berapa detik waktu yang anda miliki? ")) #n adalah jumlah detik
a = 60*60*24 # buat var a

hari = n // a # bagi n dgn a, assign to hari
b = hari * a # a*hari, assign to b
c = n - b # n - b, assign to c
jam = c // (60 * 60) # c/60*60, assign to d
d = jam * (60 * 60) # assign d to jam*60*60
e = c - d
menit = e / 60
detik = menit % 60

print(f"waktu yang anda miliki adalah {hari} hari, {jam} jam, {menit} menit, {detik} detik.")
