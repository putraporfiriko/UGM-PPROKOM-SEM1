import math

a = int(input("Masukkan A: "))
b = int(input("Masukkan B: "))
c = int(input("Masukkan C: "))

d = (b**2) - (4*a*c)

x_1 = (-b + math.sqrt(d)) / (2*a)
x_2 = (-b - math.sqrt(d)) / (2*a)

print(f"solusinya adalah {x_1} dan {x_2}")

    