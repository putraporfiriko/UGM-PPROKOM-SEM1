def menu():
    print("""
Pilih bentuk 2D:

1. Persegi Panjang
2. Lingkaran
3. Segitiga
4. Keluar
          """)
    
def persegi():
    print("Menghitung Luas Persegi Panjang")
    p = int(input("Masukkan panjang: "))
    l = int(input("Masukkan lebar: "))
    luas = p * l
    print(f"Luas persegi panjang adalah {luas}")
    print()

    redo = input("Coba lagi? (y/n) ").strip().upper()
    if redo == "Y":
        persegi()
    else:
        menu()
    
def lingkaran():
    print("Menghitung Luas Lingkaran")
    r = int(input("Masukkan jari-jari: "))
    luas = 3.14 * r**2
    print(f"Luas lingkaran adalah {luas}")
    print()

    redo = input("Coba lagi? (y/n) ").strip().upper()
    if redo == "Y":
        lingkaran()
    else:
        menu()

def segitiga():
    print("Menghitung Luas Segitiga")
    a = int(input("Masukkan alas: "))
    t = int(input("Masukkan tinggi: "))
    luas = 0.5 * a * t
    print(f"Luas segitiga adalah {luas}")
    print()

    redo = input("Coba lagi? (y/n) ").strip().upper()
    if redo == "Y":
        segitiga()
    else:
        menu()

while True:
    menu()
    menu_option = input("Pilih bentuk 2D (1/2/3/4): ")
    if menu_option == "1":
        persegi()
    elif menu_option == "2":
        lingkaran()
    elif menu_option == "3":
        segitiga()
    elif menu_option == "4":
        print("\nTerima kasih!")
        break
    else:
        print("Pilihan tidak valid. Silahkan pilih 1, 2, 3, atau 4.")