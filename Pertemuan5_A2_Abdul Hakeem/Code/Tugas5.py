# var declaration
var_nilai = 0
var_i = 1

# for loop:
for var_nilai in range(0,10):
    print("Perulangan pertama, ke ", var_nilai)
    for var_i in range (1,3):
        print("Perulangan ke ", f"{var_nilai}, ", var_i)
# outside var_i loop
var_i = 1
# outside var_nilai loop:
print("var_nilai = ", int(var_nilai)+1, "= 10. Bernilai false.")