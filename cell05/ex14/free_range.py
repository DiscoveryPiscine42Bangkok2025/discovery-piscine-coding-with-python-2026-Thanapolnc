#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
  print("none")
else:
  first_param = str(sys.argv[1])
  secone_param = str(sys.argv[2])
  num1 = int(first_param)
  num2 = int(secone_param)
  arr = []
  for i in range(num1, num2+1):
    arr.append(i)
  print(arr)