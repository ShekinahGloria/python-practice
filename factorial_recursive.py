def factorial(n):
    # If the number is 0 or 1, just return 1 (because 0! = 1! = 1)
    if n == 0 or n == 1:
        return 1
    else:
        # Multiply the number by the factorial of the number before it
        return n * factorial(n - 1)

# Example:
print(factorial(7))  # The output should be 5040
print(factorial(4))  # The output should be 24 
