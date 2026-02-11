#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
  print("none")
else:
  first_param = str(sys.argv[1])
  zcount = first_param.count("z")

  if zcount == 0:
    print("none")
  else:
    print("z" * zcount)