# Leap Year

# Instructions

# Write a program that works out whether if a given year is a leap year. 
# A normal year has 365 days, leap years have 366, with an extra day in February. 
# The reason why we have leap years is really fascinating, this video does it more justice:
# https://www.youtube.com/watch?v=xX96xng7sAE

# This is how you work out whether if a particular year is a leap year.

# on every year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400

# e.g. The year 2000:

# 2000 ÷ 4 = 500 (Leap)

# 2000 ÷ 100 = 20 (Not Leap)

# 2000 ÷ 400 = 5 (Leap!)

# So the year 2000 is a leap year.

# But the year 2100 is not a leap year because:

# 2100 ÷ 4 = 525 (Leap)

# 2100 ÷ 100 = 21 (Not Leap)

# 2100 ÷ 400 = 5.25 (Not Leap)

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input 1
# 2400

# Example Output 1
# Leap year.

# Example Input 2
# 1989

# Example Output 2
# Not leap year.

def is_leap_year(year):
  leap = False
  message = "Not leap year."

  if year % 4 == 0 and year % 100 != 0:
    leap = True

  if year % 400 == 0:
    leap = True

  # Ternay operators: https://book.pythontips.com/en/latest/ternary_operators.html
  message = "Leap year." if leap else message

  return message
  
print(is_leap_year(2000)) # True

print(is_leap_year(1989)) # False

print(is_leap_year(2015)) # False

print(is_leap_year(2016)) # True
    

