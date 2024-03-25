#!/usr/bin/python3
""" python script to filter al the pass that are not 11 chars """
from sys import argv

dest = "passords.txt" if len(argv) < 3 else argv[2]
count = 0

with open(argv[1]) as f:
    lines = f.readlines()
    with open(dest, 'a+') as d:
        d.seek(0)
        old = d.read()
        for line in lines:
            if len(line) == 12 and line not in old:
                d.write(line)
                count += 1
print(count)

