import sys
import string
from collections import Counter

def find_max_beauty(phrase):
    letter_freq = Counter(''.join([x for x in phrase.lower() if x in string.ascii_lowercase]))
    values = list(letter_freq.values())
    return sum([val * score for val, score in zip(sorted(values, reverse=True), range(26, 26-len(values), -1))])

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            print(find_max_beauty(line.strip()))

if __name__ == '__main__':
    main()
