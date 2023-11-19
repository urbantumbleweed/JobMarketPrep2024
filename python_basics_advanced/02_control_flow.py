
# Control Flow Exercises

# 1. If Statements

# Use an if statement to check if a number is positive or negative
# If the number is positive, print "The number is positive"
# If the number is negative, print "The number is negative"

number = 5
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

# 2. For Loops

# Use a for loop to iterate over a list of numbers and print each number
# The list of numbers is [1, 2, 3, 4, 5]
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# Use a for loop to iterate over a string and print each character
# The string is "Hello, World!"
string = "Hello, World!"
for character in string:
    print(character)

# 3. While Loops

# Use a while loop to print numbers from 1 to 5
# Start with a variable `num` set to 1
# Increment `num` by 1 in each iteration
# Stop the loop when `num` is greater than 5
num = 1
while num <= 5:
    print(num)
    num += 1

# Use a while loop to find the factorial of a number
# The factorial of a number is the product of all positive integers less than or equal to that number
# Start with a variable `num` set to 5
# Initialize a variable `factorial` with a value of 1
# Multiply `factorial` by `num` in each iteration
# Decrement `num` by 1 in each iteration
# Stop the loop when `num` is less than or equal to 0
num = 5
factorial = 1
while num > 0:
    factorial *= num
    num -= 1

print(factorial)

# 4. Control Flow in Programs

# Write a program that asks the user for their age
# If the age is less than 18, print "You are a minor"
# If the age is between 18 and 65, print "You are an adult"
# If the age is greater than 65, print "You are a senior citizen"
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor")
elif age >= 18 and age <= 65:
    print("You are an adult")
else:
    print("You are a senior citizen")

# Write a program that asks the user for a number
# If the number is divisible by 3, print "Fizz"
# If the number is divisible by 5, print "Buzz"
# If the number is divisible by both 3 and 5, print "FizzBuzz"
# Otherwise, print the number itself
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

# Write a program that asks the user for a password
# If the password is "password123", print "Access granted"
# Otherwise, print "Access denied"
password = input("Enter your password: ")
if password == "password123":
    print("Access granted")
else:
    print("Access denied")

# Write a program that asks the user for a grade (a number between 0 and 100)
# If the grade is greater than or equal to 90, print "A"
# If the grade is between 80 and 89, print "B"
# If the grade is between 70 and 79, print "C"
# If the grade is between 60 and 69, print "D"
# If the grade is less than 60, print "F"

# Feel free to modify the code and add more exercises as you explore control flow in Python!
