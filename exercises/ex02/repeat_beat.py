"""Repeating a beat in a loop."""

__author__ = "730409936"


# Begin your solution here...
counter: int =1
beat: str = input("What beat do you want to repeat? ")
time: int = int(input("How many times do you want to repeat it?"))
    
while counter <= time:
    if counter == 1:
        beat: str = beat + beat 
    counter = counter +1 
print(beat)