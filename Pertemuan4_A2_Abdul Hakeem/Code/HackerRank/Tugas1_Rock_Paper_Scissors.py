n = input("")

# valid inputs: [], (), 8<

# pemain 1 menang

if(n == "[] ()"):
    print("Pemain A menang")
elif(n == "() 8<"):
    print("Pemain A menang")
elif(n == "8< []"):
    print("Pemain A menang")

# draw

elif (n == "[] []"):
    print("Draw")
elif (n == "() ()"):
    print("Draw")
elif (n == "8< 8<"):
    print("Draw")

# pemain 2 menang

elif(n == "() []"):
    print("Pemain B menang")
elif(n == "8< ()"):
    print("Pemain B menang")
elif(n == "[] 8<"):
    print("Pemain B menang")

# invalid inputs:
else:
    print("Invalid input.")