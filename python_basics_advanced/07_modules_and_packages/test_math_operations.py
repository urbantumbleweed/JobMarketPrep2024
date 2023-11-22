from math_operations import subtract

# Test cases for subtract function
def test_subtract():
    # Test case 1: Subtracting two positive numbers
    assert subtract(5, 2) == 3

    # Test case 2: Subtracting a positive number from zero
    assert subtract(0, 3) == -3

    # Test case 3: Subtracting zero from a positive number
    assert subtract(7, 0) == 7

    # Test case 4: Subtracting two negative numbers
    assert subtract(-5, -2) == -3

    # Test case 5: Subtracting a negative number from zero
    assert subtract(0, -3) == 3

    # Test case 6: Subtracting zero from a negative number
    assert subtract(-7, 0) == -7

    # Test case 7: Subtracting a positive number from a negative number
    assert subtract(-5, 2) == -7

    # Test case 8: Subtracting a negative number from a positive number
    assert subtract(5, -2) == 7

    # Test case 9: Subtracting zero from zero
    assert subtract(0, 0) == 0

    print("All test cases passed!")

# Run the test cases
test_subtract()