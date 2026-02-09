#!/usr/bin/env python3

first_number = int(input("Enter the first number:\n"))
secone_number = int(input("Enter the second number:\n"))

mult = first_number*secone_number
result = ""
if mult > 0:
  result = "positive"
elif mult < 0:
  result = "negative"
elif mult == 0:
  result = "positive and negative"
print(f"{first_number} x {secone_number} = {mult}")
print(f"The result is {result}.")
