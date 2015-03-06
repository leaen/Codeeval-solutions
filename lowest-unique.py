import sys

def lowest_unique_number(line):
    numbers = sorted(map(int, line.split()))
    for e in numbers:
        if numbers.count(e) == 1:
            return line.index(str(e))//2+1
    return 0

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            print(lowest_unique_number(line.strip()))

if __name__ == '__main__':
    main()
