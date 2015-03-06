import sys

def solve(problem):
    lowercase = sum(map(lambda x: 1 if x.islower() else 0, list(problem)))
    uppercase = sum(map(lambda x: 1 if x.isupper() else 0, list(problem)))
    output = 'lowercase: {:.2f} uppercase: {:.2f}'
    length = len(problem)
    return output.format((lowercase*100 / length), (uppercase*100 / length))

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            print(solve(line.strip()))

if __name__ == '__main__':
    main()
