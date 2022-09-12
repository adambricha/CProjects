#Adam Bricha
#U9233-5585
# This program has a menu that lets the user pick a program to run. If the user wants to add two complex numbers, subtract,
#multiply or divide, the user can choose. The program will print the expression to the user and the user will have an
#option to run the code again. This program is a calculator for complex numbers.

def displaymenu():
    print("Welcome to the Complex Number Program!")
    print("Here are your choices:")
    print("1. Adding two complex numbers ")
    print("2. Subtracting two complex numbers ")
    print("3. Multiplying two complex numbers ")
    print("4. Dividing two complex numbers ")
def addition():
    ((a+c) + (b+d))
def subtraction():
    (a - c) + (b - d)
def multiplication():
    ((a * c) - (b * d) + (a * d) + (b * c))
def division():
    ((a * c) + (b * d) + (b * c) - (a * d))

displaymenu()
choice = int(input("Enter your choice (1 - 4):"))
while choice <1 or choice >4:
    choice = int(input("Invalid entry. Re-enter your choice (1 - 4):"))
a = int(input("Enter the first complex expression (enter real part):"))
b = int(input("Enter the first complex expression (enter imaginary part):"))
c = int(input("Enter the secound complex expression (enter real part): "))
d = int(input("Enter the secound complex expression (enter imaginary part): "))


if choice == 1:
    print("The two added complex expressions is:")
    print((a+c),"+",(b+d),end="i")

elif choice ==2:
    print("The two complex expressions subtracted is:")
    print((a - c), "+", (b - d), end="i")

elif choice == 3:
    print("The two complex expressions multiplied is:")
    print((a * c) - (b * d), "+", (a * d) + (b * c), end="i")

elif choice == 4:
    print("The two complex expressions divided is:")
    print((a * c) + (b * d), "+", (b*c) - (a * d), end="i")
    print("/",end="")
    print(c**2 +d**2)

print()
run_again = input("Would you like to run the program again? Enter yes or no: ")
if run_again =="no":
    quit()
else:
    while run_again != "no":
        displaymenu()
        choice = int(input("Enter your choice (1 - 4):"))
        while choice < 1 or choice > 4:
            choice = int(input("Invalid entry. Re-enter your choice (1 - 4):"))
        a = int(input("Enter the first complex expression (enter real part):"))
        b = int(input("Enter the first complex expression (enter imaginary part):"))
        c = int(input("Enter the secound complex expression (enter real part): "))
        d = int(input("Enter the secound complex expression (enter imaginary part): "))

        if choice == 1:
            print("The two added complex expressions is:")
            print((a + c), "+", (b + d), end="i")

        elif choice == 2:
            print("The two complex expressions subtracted is:")
            print((a - c), "+", (b - d), end="i")

        elif choice == 3:
            print("The two complex expressions multiplied is:")
            print((a * c) - (b * d), "+", (a * d) + (b * c), end="i")

        elif choice == 4:
            print("The two complex expressions divided is:")
            print((a * c) + (b * d), "+", (b * c) - (a * d), end="i")
            print("/", end="")
            print(c ** 2 + d ** 2)

        print()
        run_again = input("Would you like to run the program again? Enter yes or no: ")

        print(complex(3,6))