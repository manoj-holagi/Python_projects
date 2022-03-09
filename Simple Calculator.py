print("Hello, choose operation to be performed")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")


option = int(input("Enter the option: "))

if option == 1:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    a = n1+n2
    print("Addition of two numbers is",a)
elif option == 2:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    s = n1-n2
    print("Subtraction of two numbers is",s)
elif option == 3:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    m = n1*n2
    print("Multiplication of two numbers is",m)
elif option == 4:
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    d = n1/n2
    print("Addition of two numbers is",d)
else:
    print("Invalid option")