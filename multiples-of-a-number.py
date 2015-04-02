import sys

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            x, n = line.strip().split(',')
            x = int(x)
            n = int(n)
            v = int(n)
            while v < x:
                v += n
            print(v)

if __name__ == '__main__':
    main()
