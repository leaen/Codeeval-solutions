import sys
from itertools import product

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            length, letters = line.strip().split(',')
            
            combinations = product(letters, repeat=int(length))
            combinations = [''.join(x) for x in combinations]
            
            combinations = [x+y for x in letters for y in letters]

            print(','.join(map(str, combinations)))

if __name__ == '__main__':
    main()
