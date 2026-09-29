#CALCULATOR 
def calculator():
    print("Welcome to the CLI Calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. modulus")
    print("6. float division")
    print("7. exponent")

    choice = input("Enter choice (1/2/3/4/5/6/7): ")

    if choice in ['1', '2', '3', '4', '5', '6', '7']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("the additions of two number is:", num1 + num2)
        elif choice == '2':
            print("the subtraction of two number is:", num1 - num2)
        elif choice == '3':
            print("the multiplication of two number is:", num1 * num2)
        elif choice == '4':
            if num2 != 0:
                print("the division of two number is:", num1 / num2)
            else:
                print("Error! Division by zero.")
        elif choice == '5':
            print("the modulus of two number is:", num1 % num2)
        elif choice == '6':
            if num2 != 0:
                print("the float division of two number is:", num1 // num2)
            else:
                print("Error! Division by zero.")
        elif choice == '7':
            print("the exponent of two number is:", num1 ** num2)
    else:
        print("Invalid choice, please select between 1-7")
calculator()
