def is_even(num):
    return num % 2 == 0

# Test cases
assert is_even(0) == True  # 0 is an even number
assert is_even(2) == True  # 2 is an even number
assert is_even(4) == True  # 4 is an even number
assert is_even(10) == True  # 10 is an even number
assert is_even(-2) == True  # -2 is an even number

assert is_even(1) == False  # 1 is an odd number
assert is_even(3) == False  # 3 is an odd number
assert is_even(7) == False  # 7 is an odd number
assert is_even(11) == False  # 11 is an odd number
assert is_even(-3) == False  # -3 is an odd number

print("All test cases passed!")