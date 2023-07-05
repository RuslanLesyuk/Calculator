#!/bin/env python3
colors = {
    'black': '\033[30m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'reset': '\033[0m'
}



def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed."

print("Welcome to the Calculator Program!")

while True:
    print("\nPlease select an operation:")
    print(colors['green'] + "1. Addition" + colors['reset']) 
    print(colors['green'] + "2. Subtraction" + colors['reset'])
    print(colors['green'] + "3. Multiplication" + colors['reset'])
    print(colors['green'] + "4. Division" + colors['reset'])
    print(colors['magenta'] + "5. Exit" + colors['reset'])

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print(colors['cyan'] + "Exiting the calculator. Goodbye!" + colors['reset'])
        break
    elif choice not in ["1", "2", "3", "4"]:
        print(colors['red'] + "Invalid choice. Please try again." + colors['reset'])
        continue
    
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print(colors['red'] + "Invalid input. For example you need to type Integer like: (1, 2, 3,...) or Float like: (1.1, 1.2, 1.3,... )" + colors['reset'])
            

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print(colors['red'] + "Invalid input. For example you need to type Integer like: (1, 2, 3,...) or Float like: (1.1, 1.2, 1.3,... )" + colors['reset'])
          
            
           
    if choice == "1":
        result = addition(num1, num2)
        print(colors['yellow'] + "Result:" + colors['reset'], result)
    elif choice == "2":
        result = subtraction(num1, num2)
        print(colors['yellow'] + "Result:" + colors['reset'], result)
    elif choice == "3":
        result = multiplication(num1, num2)
        print(colors['yellow'] + "Result:" + colors['reset'], result)
    elif choice == "4":
        result = division(num1, num2)
        print(colors['yellow'] + "Result:" + colors['reset'], result)
    else:
        print(colors['red'] + "Sorry something went wrong, try again..." + colors['reset'])

