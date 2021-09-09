"""conditional IF Else example"""

SECRET: int = 3
print("I'm thinking a number of 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
  print("You guess correctly!")
else: 
  print("You guess incorrectly :(")
  if guess > SECRET:
    print("You guess too high")
print("Game over!")
