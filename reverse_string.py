def reverse_string(s):
    start = 0
    end = len(s) - 1  # Start from the end of the string
    s_list = list(s)  # Convert the string to a list so we can swap things
    while start < end:
        # Swap characters
        s_list[start], s_list[end] = s_list[end], s_list[start]
        start += 1
        end -= 1
    return ''.join(s_list)  # Convert the list back to a string

# Example
print(reverse_string("python"))  # Outputs "nohtyp"
