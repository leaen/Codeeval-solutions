import sys

with open(sys.argv[1]) as input_file:
    for line in input_file.readlines():
        print(line.strip().swapcase())
