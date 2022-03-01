# Docs and codes in python: https://www.askpython.com/

# Treasure Map

# Instructions
# You are going to write a program which will mark a spot with an X.

# In the starting code, you will find a variable called map.

# This map contains a nested list. When map is printed this is what the nested list looks like:

# ['⬜️', '⬜️', '⬜️'],
# ['⬜️', '⬜️', '⬜️'],
# ['⬜️', '⬜️', '⬜️']

# This is to try and simulate the coordinates on a real map.

# Your job is to write a program that allows you to mark a square on the map using a two-digit system. 
# The first digit is the vertical column number and the second digit is the horizontal row number.

# From https://stackoverflow.com/a/45808300
def index_of(a_list, value):
  try:
      return a_list.index(value)
  except ValueError:
      return -1

def treasure_map_game(rows = 3, columns = 3):
  print("Welcome to treasure map!")

  # This way does't worked:
  # rows_create, columns_create = (rows, columns)
  # treasure_map = [["_"] * rows_create] * columns_create
  # Every time it's done, this whats happened:
  # ['X', '_', '_' ]
  # ['X', '_', '_' ]
  # ['X', '_', '_' ]

  row1 = ["_", "_", "_"]
  row2 = ["_", "_", "_"]
  row3 = ["_", "_", "_"]
  treasure_map = [row1, row2, row3]

  def show_treasure_map(t_map):
    columns_letter = ["#", "A", "B", "C"]
    rows_number = ["1", "2", "3"]

    print("| " + (" | ").join(columns_letter) + " |")

    for index, item in enumerate(t_map):
      print("| " + rows_number[index] + " | " + (" | ").join(item) + " |")

  def is_completed(t_map):
    completed = True
    
    for index, item in enumerate(t_map):
      if index_of(item, "_") > -1:
        completed = False
        break

    return completed

  def ask():
    columns_letter = ["a", "b", "c"]
    rows_number = ["1", "2", "3"]

    column = columns_letter.index(input("Choose the column: A, B or C: ").lower())
    row = rows_number.index(input("Choose the row: 1, 2 or 3: "))

    return {"row": row, "column": column}

  while not is_completed(treasure_map):
    ask_answers = ask()
    
    ask_row = ask_answers["row"]
    ask_column = ask_answers["column"]

    treasure_map[ask_row][ask_column] = "X"
    
    show_treasure_map(treasure_map)

  print(treasure_map)
treasure_map_game()