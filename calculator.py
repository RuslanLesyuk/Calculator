#!/bin/env python3

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
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Exiting the calculator. Goodbye!")
        break
    elif choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please try again.")
        continue
    
    
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the first number.")
            print("Please type the first number again.")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the second number.")
            print("Please type the second number again.") 
          
            
           
    if choice == "1":
        result = addition(num1, num2)
        print("Result:", result)
    elif choice == "2":
        result = subtraction(num1, num2)
        print("Result:", result)
    elif choice == "3":
        result = multiplication(num1, num2)
        print("Result:", result)
    elif choice == "4":
        result = division(num1, num2)
        print("Result:", result)
    else:
        print("Invalid choice. Please try again.")

