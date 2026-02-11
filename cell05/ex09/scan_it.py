#!/usr/bin/env python3
import sys, re

if len(sys.argv) != 3:
  print("none")
else:
  first_param = sys.argv[1]
  second_param = sys.argv[2]
  match = re.findall(first_param, second_param)
  if len(match) == 0:
    print("none")
  else:
    print(len(match))