#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
  print("none")
else:
  param = list(sys.argv)

  print(f"parameters: {len(param) - 1}")

  for i in range(len(param)):
    if i == 0:
      continue
    else:
      print(f"{param[i]}: {len(param[i])}")

