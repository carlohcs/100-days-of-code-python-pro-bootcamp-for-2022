#Password Generator Project
from nis import match
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

log = False
go_way = 2

def gen_letter():
  # Common way
  # return str(letters[random.randint(0, len(letters) - 1)])
  # Python way
  return random.choice(letters)

def gen_symbol():
  # return str(symbols[random.randint(0, len(symbols) - 1)])
  return random.choice(symbols)

def gen_number():
  # return str(numbers[random.randint(0, len(numbers) - 1)])
  return random.choice(numbers)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
def easy_way():
  password = ""
  for _ in range(0, nr_letters):
    password += gen_letter()

  for _ in range(0, nr_symbols):
    password += gen_symbol()

  for _ in range(0, nr_numbers):
    password += gen_number()

  print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
def hard_way():
  password = ""
  runned_letters = 0
  runned_numbers = 0
  runned_symbols = 0
  total_items = nr_letters + nr_numbers + nr_symbols
  
  while runned_letters + runned_numbers + runned_symbols != total_items:
    to_generate = random.randint(0, 2)

    if log:
      print(f"Runned: {runned_letters + runned_numbers + runned_symbols} / {total_items}")

    if to_generate == 0 and runned_letters < nr_letters:
      runned_letters += 1
      password += gen_letter()
      if log:
        print("Generating letter...")
    elif to_generate == 1 and runned_numbers < nr_numbers:
      runned_numbers += 1
      password += gen_number()
      if log:
        print("Generating number...")
    elif to_generate == 2 and runned_symbols < nr_symbols:
      runned_symbols += 1
      password += gen_symbol()
      if log:
        print("Generating symbol...")
  
  print(password)

def hard_simple_way():
  password = ""
  password_list = []

  for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)

  for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

  for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

  random.shuffle(password_list)

  for char in password_list:
    password += char

  print(password)

if go_way == 0:
  easy_way()
elif go_way == 1:
  hard_way()
else:
  hard_simple_way()