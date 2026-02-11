#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
  print("none")
else:
  txt = input("What was the parameter? ").strip()

  if str(sys.argv[1]) == txt:
    print("Good job!")
  else:
    print("Nope, sorry...")
