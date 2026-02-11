#!/usr/bin/env python3
import sys

arr = list(sys.argv)
arr.reverse()

if len(sys.argv) < 3:
  print("none")
else:
  for i in range(len(arr)):
    if i == (len(arr) - 1):
      break
    else:
      print(arr[i])
      