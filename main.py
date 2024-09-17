import random

def rollDice(sides):
   while True:
    random_number = random.randint(1, sides)
    print("You rolled", random_number)
    print()
    playGame = input("Roll again? ")
    if playGame == "yes":
      continue
    else:
      break

print()
print("Infinity Dice 🎲")
print()
sides = int(input("How many sides: "))
rollDice(sides)