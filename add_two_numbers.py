#!/usr/bin/env python3

import sys
print("pass two numbers as arguments")

if len(sys.argv) == 3 :
    print(int(sys.argv[1])+int(sys.argv[2]))
else:
    print("no proper args passed")
