
# Define a function called "greet" that takes a name as an argument and prints a greeting message
def greet(name):
    print(f"Hello, {name}!")

# Call the "greet" function with your name as the argument
name = input("What is your name? ")
greet(name)

# Define a function called "add_numbers" that takes two numbers as arguments and returns their sum
def add_numbers(num1, num2):
    return num1 + num2

# Call the "add_numbers" function with two numbers of your choice and print the result
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(add_numbers(num1, num2))

# Define a function called "calculate_average" that takes a list of numbers as an argument and returns their average
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Call the "calculate_average" function with a list of numbers of your choice and print the result
numbers = input("Enter a list of numbers, separated by spaces: ")
numbers_list = [int(num) for num in numbers.split()]

print(calculate_average(numbers_list))

# Define a function called "is_even" that takes a number as an argument and returns True if it is even, False otherwise
def is_even(num):
    return num % 2 == 0

# Call the "is_even" function with a number of your choice and print the result
number = int(input("Is it Even? Enter a number: "))
print(is_even(number))

# Define a function called "get_max" that takes a list of numbers as an argument and returns the maximum number
# Call the "get_max" function with a list of numbers of your choice and print the result

def get_max(numbers):
    return max(numbers)

numbers = input("Get the max. Enter a list of numbers, separated by spaces: ")
numbers_list = [int(num) for num in numbers.split()]

print(get_max(numbers_list))
