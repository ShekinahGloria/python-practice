# python-practice
**Name**: Otieno Shekinah Gloria

**Admission number**: 182989
**Python Functions Collection**

**Description** 

This project contains some simple Python functions. Each function does a small task like adding numbers, reversing strings, summing digits, checking even or odd, and finding factorials.

**List of Functions**

**1. sum_list.py**

This adds up all the numbers in a list and returns the total.

Step-by-step :

1.Start with total = 0.

2.Go through each number in the list.

3.Add each number to total.

4.After the loop, return total.

Example:

print(sum_list([2, 4, 6, 8])) Output is 2+4+8+6=20

**2. check_even_or_odd.py**

This checks if a number is even or odd.

Step-by-step:

1.Use the % (modulus) operator to check if the number divides by 2 with no remainder.

2.If remainder is 0, it's Even.

3.If not, it's Odd.

Example:
print(check_even_or_odd(6))  Output: Even

print(check_even_or_odd(3))  Output: Odd

**3. factorial_loop.py**

This calculates the factorial of a number using a for loop.

Step-by-step:

1.Start with result = 1.

2.For every number from 1 up to n, multiply result by that number.

3.After the loop, return result.

Example:

print(factorial_loop(6))  Output=720 

**4. reverse_string.py**

This takes a string and returns it reversed.

Step-by-step:

1.Take the original string.

2.Write it backwards.

3.Return the reversed string.

Example:

print(reverse_string("python")) Outputs "nohtyp"

**5. factorial_recursive.py**

This calculates the factorial of a number using recursion.

Step-by-step:
1.If n is 0 or 1, return 1 .

2.Otherwise, return n * factorial(n-1).

3.Keep calling until you reach 1, then multiply back up.


Example:

print(factorial(7)) The output should be 5040

print(factorial(4))  The output should be 24 

**6. sum_digits.py**

This sums up all the digits of a given number.

Step-by-step:

1.Turn the number into a string to separate digits.

2.Go through each character (digit).

3.Turn each character back into an integer.

4.Add them up and return the total.

Example:

print(sum_digits(345))  Output: 3 + 4+ 5= 12

**Steps on how to use**
1. Make sure you have python installed.

2. Open the terminal in the project folder.

3. Run the file you want.


