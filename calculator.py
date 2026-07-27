num_1 = int(input("Enter the first number: ")) 
num_2 = int(input("Enter the second number:"))

opertor = input("Enter the operator (+, -, *, /, %):")


if opertor == '+':
    print("Addition = ", num_1 + num_2)
elif opertor == '-':
    print("Difference = ", num_1 - num_2)
elif opertor == '*':
    print("Multiplication = " , num_1 * num_2) 
elif opertor == '/':
    if num_2 == 0:
        print("Error, Zero can not be divided.")
    else:
        print("Division = " , num_1/num_2)
elif opertor == '%':
    print("Remainder = " , num_1 % num_2)
