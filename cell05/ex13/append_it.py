#!/usr/bin/env python3
import sys

if len(sys.argv) < 2:
  print("none")
else:
  txt = list(sys.argv)
  for i in range(len(txt)):
    if i == 0:
      continue
    else:
      if txt[i][-3:] == "ism":
        continue
      else:
        print(f"{txt[i]}ism")