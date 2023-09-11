# var declaration
val = 0
j = 1

# for loop
for val in range(0,10):
    print("Perulangan pertama ke ", val)
    while j < 3:
        print("Perulangan ke ", val,", ", j)
        j += 1
    # outside j loop
    j = 1
# outside val loop
print("var_nilai = ", int(val)+1, "= 10. Bernilai false")