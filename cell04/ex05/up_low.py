#!/usr/bin/env python3

txt = input("")

for i in txt:
  if i.isupper():
    print(i.lower(), end="")
  elif i.islower():
    print(i.upper(), end="")
  else:
    print(i, end="")
print()
