"""Counting letters in a string."""

__author__ = "730409936"


# Begin your solution here...
letter: str = "  What letter do you want to seach for?"
word: str = " Enter a word "
number: int =1
count = 0

while number <= len(word):
    if letter == word[len(word) - 1]:
        count = count +1 
    else: 
        count = count + 0
number = number +1

print: int = count 
