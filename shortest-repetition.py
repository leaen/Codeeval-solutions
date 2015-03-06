import re
import sys

def find_shortest_repeating_substring(text):
    r = re.compile(r"(.+?)(?=\1)")
    return len(r.findall(text))

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            print(find_shortest_repeating_substring(line.strip()))

if __name__ == '__main__':
    main()
