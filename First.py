def calculadora():
    while True:
        print("Simple Calculator")
        print()
        print("1 - Add")
        print("2 - Subtract")
        print("3 - Multiplication")
        print("4 - Division")
        print("s - Exit")
        operacao = input("Select an operator or 's' to exit: ")


        if operacao == "s" or operacao == "S":
            print("Thank you for using!!!")
            break

        if operacao not in ['1', '2', '3', '4']:
            print("Invalid Operator")
            continue

        numero_1 = float(input("Number 1: "))
        numero_2 = float(input("Number 2: "))

        if operacao == '1':
            result = numero_1 + numero_2
            print("The sum is: ", result)
        elif operacao == '2':
            result = numero_1 - numero_2
            print("The subtraction is: ", result)
        elif operacao == '3':
            result = numero_1 * numero_2
            print("The multiplication is: ", result)
        else:
            if numero_2 == 0:
                print("The division by zero is impossible, try again :).")
                continue
            else:
                result = numero_1 / numero_2
                print("The division is: ", result)
        print()

calculadora()