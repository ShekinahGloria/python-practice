def sum_digits(n):
    # Step 1: Change the number into a string
    n = str(n)
    
    # Step 2: Start total at 0
    total = 0
    
    # Step 3: Go through each digit
    for digit in n:
        total += int(digit)  # Turn digit back to number and add it
    
    # Step 4: Return the total
    return total

# Example :
print(sum_digits(345))  # Output: 3 + 4+ 5= 12
