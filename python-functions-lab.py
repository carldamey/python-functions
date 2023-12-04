# 1. Write a function named sum_to that accepts a single integer, n, and returns the sum of the integers from 1 to n.
# 
# For example:
# 
#  sum_to(6)  # returns 21
#  sum_to(10) # returns 55

def sum_to(n):
  sum = 0
  for num in range(1, n + 1):
    sum += num
  return sum

print("Challenge 1 -", sum_to(6), sum_to(10))

# 2. Write a function named largest that takes a list of numbers as an argument and returns the largest number in that list.
# 
# For example:
# 
#  largest([1, 2, 3, 4, 0])  # returns 4
#  largest([10, 4, 2, 231, 91, 54])  # returns 231

def largest(num_list):
  largest_num = 0
  for num in num_list:
    if num > largest_num:
      largest_num = num
  return largest_num

print("Challenge 2 -", largest([1, 2, 3, 4, 0]), largest([10, 4, 2, 231, 91, 54]))

# 3. Write a function named occurrences that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.
# 
# For example:
# 
#  occurrences('fleep floop', 'e')   # returns 2
#  occurrences('fleep floop', 'p')   # returns 2
#  occurrences('fleep floop', 'ee')  # returns 1
#  occurrences('fleep floop', 'fe')  # returns 0

def occurrences(str1, str2):
  matches = 0
  while str2 in str1:
    str1 = str1.replace(str2, "", 1)
    matches += 1
  return matches
  
print("Challenge 3 -", occurrences('fleep floop', 'e'), occurrences('fleep floop', 'p'), occurrences('fleep floop', 'ee'), occurrences('fleep floop', 'fe'))

# 4. Write a function named product that takes an arbitrary number of numbers, multiplies them all together, and returns the product.
# (HINT: Review your notes on *args).
# 
# For example:
# 
#  product(-1, 4) # returns -4
#  product(2, 5, 5) # returns 50
#  product(4, 0.5, 5) # returns 10.0

def product(*args):
  result = 1
  for factor in args:
    result *= factor
  return result

print("Challenge 4 -", product(-1, 4), product(2, 5, 5), product(4, 0.5, 5))

# Bonus Challenge
# Write a function named steps_to_zero that accepts a non-negative integer as an argument, and returns the number of steps it took to reduce the integer to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.
# 
# For example:
# 
#  steps_to_zero(14) # returns 6

def steps_to_zero(int):
  steps = 0
  while int:
    if int % 2:
      int -= 1
    else:
      int //= 2
    steps += 1
  return steps

print("Bonus Challenge -", steps_to_zero(14))
