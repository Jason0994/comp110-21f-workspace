"""Input two numbers and do ">" ">=" "==" "!="""
__author__ = "730409936"
left = int(input("Left-hand side: "))
right = int(input("Right-hand side: "))
print(f"{left} < {right} is {left<right}")
print(f"{left} >= {right} is {left>=right}")
print(f"{left} == {right} is {left==right}")
print(f"{left} != {right} is {left!=right}")