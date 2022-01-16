# STONE-PAPER-SEIZER GAME

# Imported random module to play computer mode to take random int values.
import random

# Function for game and here we passed 2 argu as (comp, you).
def game_win(comp, you):
  if comp == you:
    return None
  elif comp == 'r':
    if you == 'k':
      return False
    elif you == 'p':
      return True
  elif comp == 'p':
    if you == 'r':
      return False
    elif you == 'k':
      return True
  elif comp == 'k':
    if you == 'p':
      return False
    elif you == 'r':
      return True

# Here computer selects random no. for game.
print("Comp Turn : Stone(r) Paper(p) or Seizer(k) ?")
randNo = random.randint(1, 3)
print(randNo)

# and here that random no. converts into String type.
if randNo == 1:
  comp = 'r'
elif randNo == 2:
  comp ='p'
elif randNo == 3:
  comp = 'k'


# print("Comp choose ",comp)   # It show what computer selected before you play

# Taking input from user for game turn
you = str(input("your Turn : Stone(r) Paper(p) or Siezer(k) ? "))

a = game_win(comp, you)

print("You choose ",you)

if a == None:
  print("The game is tie !!")
elif a:
  print("You win !!")
else:
  print("You lose !!")

