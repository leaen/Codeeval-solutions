import sys

def find_writer(puzzle):
    digest, hints = puzzle.split('|')
    hints = hints.split()
    return ''.join([digest[int(x) - 1] for x in hints])

def main():
    with open(sys.argv[1]) as input_file:
        for puzzle in input_file:
            print(find_writer(puzzle.strip()))

if __name__ == '__main__':
    main()
