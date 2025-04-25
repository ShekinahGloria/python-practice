# The function takes a list of numbers and returns their total sum
def sum_list(numbers):
    total = 0  # Start with 0
    for num in numbers:
        total += num  # Keep adding each number to total
    return total  # Give back the total after the loop finishes

# Test it by calling the function and printing the result
print("Adding up the numbers 1, 2, 3, 4:")
print(sum_list([1, 2, 3, 4]))  # Expected output: 10

# A test with different numbers
print("Adding up the numbers 2, 4, 6, 8:")
print(sum_list([2, 4, 6, 8]))  # Expected output: 20
