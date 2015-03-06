import sys

def isArmstrongNumber(n):
    n_str = str(n)
    total = sum(map(lambda x: int(x) ** len(n_str), list(n_str)))
    
    return total == n

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file.readlines():
            n = line.strip()
            print(isArmstrongNumber(int(n)))

if __name__ == '__main__':
    main()
