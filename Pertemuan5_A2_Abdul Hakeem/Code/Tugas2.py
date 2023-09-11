awal = int(input("input your monthly allowance!\t: "))
sisa = awal

while True:
    pengeluaran = int(input("input your spendings for today (-1 to exit): "))
    if pengeluaran == -1:
        print("remaining balance:", sisa)
        break
    sisa = sisa - pengeluaran

    if sisa<0:
        print("balance insufficient.")
        print("remaining balance: ", sisa+pengeluaran)
        break