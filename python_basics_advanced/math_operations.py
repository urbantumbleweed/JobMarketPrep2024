# Creating a module
# Create a module called math_operations.py with the following functions:
# add - takes two numbers as arguments and returns their sum
# subtract - takes two numbers as arguments and returns their difference

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

if __name__ == "__main__":
    print(add(4, 5))
    print(subtract(4, 5))