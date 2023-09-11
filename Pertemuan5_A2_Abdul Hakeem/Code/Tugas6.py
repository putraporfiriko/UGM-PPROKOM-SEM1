# var declaration:
nilai = 0
i = 1

# while loop:
while (nilai<10):
    print("Perulangan pertama ke ", nilai)
    while (i < 3):
        print("Perulangan ke", nilai,", ", i)
        i += 1
    #outside i loop:
    i = 1
    nilai += 1
#outside nilai loop:
print("nilai = ", int(nilai), "= 10. bernilai False")