import os

def clearscreen():
    receiveinput()
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    print("""
• Addition (A)
• Subtraction (S)
• Multiplication (M)
• Division (D)
• Exit (X)
    """)
    option=input("Enter your choice: ")

    if option.upper() == "A":
        add()
    if option.upper() == "S":
        subtract()
    if option.upper() == "M":
        mult()
    if option.upper() == "D":
        division()
    if option.upper() == "X":
        exit()
    else:
        print("Invalid option!")
        main()

def receiveinput():
    global int1, int2
    int1 = int(input("Enter first number: "))
    int2 = int(input("Enter second number: "))


def add():
    receiveinput()
    clearscreen()
    print("Final operation:", int1 + int2)
    main()

def subtract():
    receiveinput()
    clearscreen()
    print("Final operation", int1 - int2)
    main()

def mult():
    receiveinput()
    clearscreen()
    print("Final operation", int1 * int2)
    main()

def division():
    receiveinput()
    clearscreen()
    print("Final operation", int1 / int2)
    main()

if __name__ == "__main__":
    main()


