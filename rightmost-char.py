import sys

def find_rightmost_char(line):
    phrase, target = line.strip().split(',')
    
    for i, c in enumerate(phrase[::-1]):
        if c == target:
            return len(phrase) - i - 1

with open(sys.argv[1]) as input_file:
    for line in input_file.readlines():
        print(find_rightmost_char(line))

