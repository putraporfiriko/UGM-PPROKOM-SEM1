x = int(input(""))
y = int(input(""))
z = int(input(""))


if x<=100:
    if y<=100:
        if z<=100:
                avg = (x + y +z)/3
        else:
            print(f"Angka yang anda input invalid. ({z})")
            exit()
    else:
         print(f"Angka yang anda input invalid. ({y})")
         exit()
else:
    print(f"Angka yang anda input invalid. ({x})")
    exit()

    
if(avg>=50):
    print("LULUS")

else:
    print("GAGAL")