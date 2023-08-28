bil1 = float(input("masukkan angka pertama: "))
bil2 = float(input("masukkan angka kedua: "))

jumlah = bil1 + bil2
kurang = bil1 - bil2
kali = bil1 * bil2
bagi = bil1 / bil2
mod = bil1 % bil2

print(f"\nhasil dari %d + %d = %d"% (bil1,bil2,jumlah))
print(f"hasil dari %d - %d = %d"% (bil1,bil2,kurang))
print(f"hasil dari %d * %d = %d"% (bil1,bil2,kali))
print(f"hasil dari %d / %d = %d"% (bil1,bil2,bagi))
print(f"hasil dari {bil1} % {bil2} = {mod}")
print("  ")