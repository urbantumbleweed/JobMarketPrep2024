
# Step 1: Define a function named "divide_numbers" that takes two parameters, "numerator" and "denominator".
# Step 2: Inside the function, use a try-except block to handle the potential exception that may occur when dividing the numbers.
# Step 3: In the try block, divide the numerator by the denominator and assign the result to a variable named "result".
# Step 4: Print the value of "result" if the division is successful.
# Step 5: In the except block, catch the ZeroDivisionError and print an error message indicating that division by zero is not allowed.
# Step 6: Outside the function, call the "divide_numbers" function with different values for the numerator and denominator to test the exception handling.

def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
        print(result)
    except ZeroDivisionError:
        print("Division by zero is not allowed.")

divide_numbers(10, 0)