#!/usr/bin/env python3

numbers = [2, 8, 9, 48, 8, 22, -12, 2]

newnumbers = []

for i in numbers:
  if i > 5:
    newnumbers.append(i+2)

print(numbers)
print(set(newnumbers))