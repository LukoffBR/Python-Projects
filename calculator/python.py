import math

print("Welcome to my calculator")
print("------------------------------------------------")

while True:
    number1 = int(input("Put a first number: "))
    operation = input("Put the operation symbol you want (e.g., +, -, *, /, **, square): ")

    if operation == 'square':
        result = math.sqrt(number1)
        print(f"The result is: {result}")
    else:
        number2 = int(input("Put a second number: "))
        if operation == "+":
            result = number1 + number2
        elif operation == '-':
            result = number1 - number2
        elif operation == '*':
            result = number1 * number2
        elif operation == '/':
            result = number1 / number2
        elif operation == '**':
            result = pow(number1, number2)
        else:
            print("You put a wrong operation symbol")
            continue

        print(f"The result is: {result}")

    choice = input("Do you want to continue (Y/N)? ").lower()
    if choice != "y":
        print("Thanks for using my calculator!")
        break
