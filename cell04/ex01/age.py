#!/usr/bin/env python3

age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")
year = 10
for _ in range(3):
  print(f"In {year} years, you'll be {year + age} years old.")
  year+=10