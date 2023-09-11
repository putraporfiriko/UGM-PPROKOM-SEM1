datact = int(input("How much data you want to input? "))
dsum = 0

for i in range (0, datact):
    datainput = int(input("Input the data: "))
    dsum += datainput

davg = dsum/datact
print(davg)