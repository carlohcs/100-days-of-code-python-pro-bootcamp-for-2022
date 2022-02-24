
# Modules
import random

# Alias
# import random as r
# n = r.randint(1, 5)

# Importing from modules

# You can import a specific thing from a
# module. e.g. a function/class/constant
# You do this with the from keyword.
# It can save you from having to type the same
# thing many times.

# from random import randint
# n = randint(1, 5)

# Importing Everything
# from random import *
# list = [1, 2, 3]

# AVOID THIS!
# choice(list)

# More readable/understood
#random.choice(list)

# Print

# Prints a string into the console.
print("Hello world!")

# Variables + input

my_name = "User"

# Prints a string into the console,
# and asks the user for a string input.
# my_name = input("What's your name?")

# F-Strings

# You can insert a variable into a string
# using f-strings.
# The syntax is simple, just insert the variable
# in-between a set of curly braces {}.
print(f"Hello {my_name}!")

# Data types

# Integers
my_integer = 32;

print(type(my_integer))

# Floating
my_float = 32.2; # int

print(type(my_float)) # float

# Boolean

print(True)
print(False)

# String
my_string = "Move on!";

print(type(my_string)) # str

# String concatenation
print("Hello" + "Carlos") # HelloCarlos

# Escaping a String
print("Hello \"my real friend\"!") # Hello "my real friend"

# F-Strings
days = 365
print(f"There area {days} in the year")

# Converting Data Types

# You can convert a variable from 1 data type to another.
# Converting to float:
# float()
# Converting to int:
# int()
# Converting to string:
# str()

n = 354
new_n = float(n)
print(new_n) #result 354.0

# Maths

# Arithmetic Operators

# You can do mathematical calculations with
# Python as long as you know the right
# operators.

print(f"3+2 = {3+2}") #Add
print(f"4-1 = {4-1}") #Subtract
print(f"2*3 = {2*3}") #Multiply
print(f"5/2 = {5/2}") #Divide
print(f"5**2 = {5**2}") #Exponent

# The += Operator

my_number = 10
my_number += 10
print(f"My number now is: {my_number}")

# The Modulo Operator

print(f"5 % 2 = {5%2}")

# Functions

def add(n1, n2):
  print(f"Calc of {n1} + {n2} is: {n1 + n2}!")

add(5, 2)

# Scopes
n = 2

def my_function():
  n = 3
  print(n)

print(n) #Prints 2
my_function() #Prints 3

# Keyword Arguments

# When calling a function, you can provide
# a keyword argument or simply just the value.
# Using a keyword argument means that
# you don't have to follow any order
# when providing the inputs.

def divide(n1, n2):
  calc = n1 / n2

  return calc

#Option 1:
print(divide(10, 2))

#Option 2:
print(divide(n2 = 10, n1 = 20))

# Conditionals

age = 18
if age >= 18:
  print("Drive!")
else:
  print("Don't drive!")

weather = "sunny"
if weather == "rain":
  print("bring umbrella")
elif weather == "sunny":
  print("bring sunglasses")
elif weather == "snow":
  print("bring gloves")

# and
s = 58
if s < 60 and s > 50:
  print("Your grade is C")

# or
age = 12
if age < 16 or age > 200:
  print("Can't drive")

# not
if not 3 > 1:
  print("something")
  #Will not be printed.

# Comparison operators

# These mathematical comparison operators
# allow you to refine your conditional checks

# > Greater than
# < Lesser than
# >= Greater than or equal to
# <= Lesser than or equal to
# == Is equal to
# != Is not equal to

# LOOPS

# While

n = 1
while n < 10:
  n += 1
  print(f"N is: {n}")

# For Loop

all_fruits = ["apple", "banana", "orange"]
for fruit in all_fruits:
  print(fruit)

# _ in a For Loop

# If the value your for loop is iterating through,
# e.g. the number in the range, or the item in
# the list is not needed, you can replace it with
# an underscore.

for _ in range(10):
  print("Running...")
  #Do something 100 times.

# break
scores = [34, 67, 99, 105]

for s in scores:
  if s > 100:
    print("Invalid")
    break
  print(s)

# continue
number = 1
while number < 10:
  number += 1
  if number % 2 == 0:
    continue
  print(f"Continuing: {number}")
#Prints all the odd numbers

# Infinite Loops
run_infinite = 0

if run_infinite == 1:
  while 5 > 1:
    print("I'm a survivor")

# List Methods

# You can extend a list with another list by
# using the extend keyword, or the + symbol.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

new_list = list1 + list2
print(new_list)

# Adding an Item to a List

all_fruits = ["apple", "banana", "orange"]
all_fruits.append("pear")

print(all_fruits)

# List Index

# To get hold of a particular item from a
# list you can use its index number.
# This number can also be negative, if you
# want to start counting from the end of the list.

letters = ["a", "b", "c"]
print(letters[0])

print(letters[-1])

print(letters[-1])

# list[start:end]
letters = ["a", "b", "c", "d"]
print(letters[1:3]) # Result: ["b", "c"]

# Built in functions

# Often you will want to generate a range
# of numbers. You can specify the start, end
# and step.
# Start is included, but end is excluded:
# start >= range < end

# range(start, end, step)
for i in range(6, 0, -2):
  print(i)
# result: 6, 4, 2
# 0 is not included.


# randint(start, end)
n = random.randint(2, 5)
print(f"RANDOM: {n}")
#n can be 2, 3, 4 or 5.

# round
print(round(4.6)) # result 5

# abs
print(abs(-4.6)) # result 4.6

# Classes and Objects

class Car:
  color = "black"
  def __init__(self, name):
    print("Initialing a new object...")
    self.name = name

  def drive(self):
    print("Moving...")

my_car = Car("Chevrolet")
my_car.drive()
print(f"Car name: {my_car.name}")

# Inheritance
class Animal:
  def breathe(self):
    print("breathing")

class Fish(Animal):
  def breathe(self):
    super().breathe()
    print("underwater")

nemo = Fish()
nemo.breathe()

# Result:
# breathing
# underwater

print(f"Car color: {my_car.color}")