#!/usr/bin/env python3

import sys

print(sys.argv)

for i in range(len(sys.argv)):
    if i==0:
        print("Function name is %s :" % sys.argv[0])
    else:
        print("%d.argument %s:" % (i,sys.argv[i]))



print(sys.platform)
print(sys.version)
