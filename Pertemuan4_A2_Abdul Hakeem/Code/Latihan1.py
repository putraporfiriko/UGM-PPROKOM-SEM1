# Program Persyaratan SIM

umur = int(input("Masukkan Umur Anda: "))
nilai = int(input("Masukkan Nilai Anda: "))

lulus = "Selamat, Anda berhak mendapatkan SIM Anda."
gagal = "Maaf, Anda tidak berhak mendapatkan sim anda.\nSilahkan coba lagi bulan atau tahun depan."

if(umur>17):
    if(nilai<60):
        print()
        print(gagal)
    else:
        print()
        print(lulus)
else:
    print()
    print(gagal)