# array declaration
buku = []

#showdata()

def showdata():
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))

#insertdata()
def insertdata():
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)

#editdata()
def editdata():
    showdata()
    indeks = int(input("Inputkan ID buku: "))
    if(indeks > len(buku)):
        print("ID salah")
    else:
        judul_baru = input("Judul baru: ")
        buku[indeks] = judul_baru

#deletedata()
def deletedata():
    showdata()
    indeks = int(input("Inputkan ID buku: "))
    if(indeks > len(buku)):
        print("ID salah")
    else:
        buku.remove(buku[indeks])

#menu()
def menu():
    print("\n")
    print("====Menu====")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    menu = int(input("Pilih menu: "))
    print("\n")
    if menu == 1:
        showdata()
    elif menu == 2:
        insertdata()
    elif menu == 3:
        editdata()
    elif menu == 4:
        deletedata()
    elif menu == 5:
        exit()
    else:
        print("Input Invalid!")

while True:
    menu()
