#! /usr/bin/env python3

import sys

out_of = int(sys.argv[1])
while 1:
    try:
        line = input()
    except EOFError:
        break
    total = 0
    for num in line.split(" "):
        total += int(num)
    print("Total: %d (%f%%)" % (total, total * (100.0 / out_of)))
print("Goodbye")
