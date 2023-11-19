
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

# Write a program that reads a sentence from the user and prints the number of words in the sentence.
sentence = input("Enter a sentence: ")

def count_words(string):
  return len(string.split())

print(count_words(sentence))

# Write a program that reads a list of numbers from the user and prints the maximum and minimum numbers in the list.
numbers = input("Enter a list of numbers, separated by spaces: ")
numbers_list = [int(num) for num in numbers.split()]

print(f'Max: {max(numbers_list)}\nMin: {min(numbers_list)}')

# TODO: Write a program that reads a file name from the user and prints the contents of the file.

# Your code goes here...
