import sys
from collections import Counter

def isRotation(s1, s2):
    if Counter(s1) == Counter(s2):
        return True
    else:
        return False

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            s1, s2 = line.strip().split(',')
            print(isRotation(s1, s2))

if __name__ == '__main__':
    main()
