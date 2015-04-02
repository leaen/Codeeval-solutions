import sys

with open(sys.argv[1]) as input_file:
    for line in input_file:
        print(sum(map(int, line.strip())))
