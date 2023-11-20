import os

# Write a program that prompts the user to enter their name and prints a welcome message.
name = input("What is your name? ")
print(f"Hello, {name}!")

# Write a program that reads a number from the user and prints its square.
number = int(input("Enter a number: "))

def square(num):
    return num ** 2
    
print(square(number))

# Write a program that reads two numbers from the user and prints their sum.
number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

def add(num1, num2):
  return num1 + num2

print(add(number1, number2))


file_name = input("Enter a file name: ")

# Check if the file path is relative or absolute
if not os.path.isabs(file_name):
  # Resolve the relative file path to an absolute path
  file_name = os.path.abspath(file_name)

with open(file_name, "r") as file:
  print(file.read())

