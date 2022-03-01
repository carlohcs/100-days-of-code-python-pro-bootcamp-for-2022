# Highest score

# Instructions

# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

# Important you are not allowed to use the max or min functions. 
# The output words must match the example. i.e

# Example Input
# 78 65 89 86 55 91 64 89

# Example Output
# The highest score in the class is: 91

def find_max(numbers = []):
  max_number = 0

  for current_number in numbers:
    if current_number > max_number:
      max_number = current_number
      continue

  return max_number

print(f"The highest is: {find_max([78, 65, 89, 86, 55, 91, 64, 89])}")



