import sys

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            l1, l2 = line.strip().split('|')
            print(' '.join([str(int(x) * int(y)) for x, y in zip(l1.split(), l2.split())]))
            
if __name__ == '__main__':
    main()
