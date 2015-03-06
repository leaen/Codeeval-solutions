import sys
from itertools import permutations

def find_permutations(s):
    return sorted([''.join(p) for p in permutations(s)])

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            print(','.join(find_permutations(line.strip())))

if __name__ == '__main__':
    main()
