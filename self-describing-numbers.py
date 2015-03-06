import sys

def isSDN(n):
    n_str = str(n)
    for i, e in enumerate(n_str):
        if n_str.count(str(i)) != int(e):
            return False
    return True

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            result = 1 if isSDN(int(line.strip())) else 0
            print(result)

if __name__ == '__main__':
    main()
