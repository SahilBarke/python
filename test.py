# This file is for cheking the functions in the mypkg package

from mypkg import addition, multiplication

# Test the addition function
result_add = addition(2, 3)
print(f"Addition of 2 and 3 is: {result_add}")

# Test the multiplication function
result_multiply = multiplication(2, 3)
print(f"Multiplication of 2 and 3 is: {result_multiply}")