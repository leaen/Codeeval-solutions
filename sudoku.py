import sys

def check_sudoku():


def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            width, sudoku_grid = line.strip().split(';')
            width = int(width)


if __name__ == '__main__':
    main()
