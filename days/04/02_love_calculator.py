# Love calculator

# Instructions
# You are going to write a program that tests the compatibility between two people.

# To work out the love score between two people:

# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.

# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."

# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."

# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

# e.g.

# name1 = "Angela Yu"

# name2 = "Jack Bauer"

# T occurs 0 times

# R occurs 1 time

# U occurs 2 times

# E occurs 2 times

# Total = 5

# L occurs 1 time

# O occurs 0 times

# V occurs 0 times

# E occurs 2 times

# Total = 3

# Love Score = 53

# Print: "Your score is 53."

# Example Input 1
# name1 = "Kanye West"
# name2 = "Kim Kardashian"

# Example Output 1
# Your score is 42, you are alright together.

# Example Input 2
# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"

# Example Output 2
# Your score is 73.

def love_calculator(name1 = False, name2 = False):
  print("Welcome to the love calculator!")
  name1 = name1 if name1 else input("Whats your name? \n")
  name2 = name2 if name2 else input("Whats your name? \n")
  message = "Your score is "

  trueLetters = ["t", "r", "u", "e"]
  loveLetters = ["l", "o", "v", "e"]

  countTrueLetters = 0
  countLoveLetters = 0

  name1 = name1.lower()
  name2 = name2.lower()

  for letter in trueLetters:
    countTrueLetters += name1.count(letter)
    countTrueLetters += name2.count(letter)

  for letter in loveLetters:
    countLoveLetters += name1.count(letter)
    countLoveLetters += name2.count(letter)

  result = int(str(countTrueLetters) + str(countLoveLetters))

  message += f"{result}"

  if result < 10 or result > 90:
    message += ", you go together like coke and mentos."
  elif result >= 40 and result <= 50:
    message += ", you are alright together."
  else:
    message += "."

  return message

print(love_calculator("Kanye West", "Kim Kardashian")) # Your score is 42, you are alright together.

print(love_calculator("Brad Pitt", "Jennifer Aniston")) # Your score is 73.

print(love_calculator())