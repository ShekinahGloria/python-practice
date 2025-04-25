# This function checks if a number is even or odd.
def check_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Test the function
print(check_even_or_odd(6))  # Output: Even
print(check_even_or_odd(3))  # Output: Odd
