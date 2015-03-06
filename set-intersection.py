import sys

def solve(problem):
    s1, s2 = problem.split(';')
    s1 = set(s1.split(','))
    s2 = set(s2.split(','))
    
    return ','.join(set.intersection(s1, s2))

def main():
    with open(sys.argv[1]) as input_file:
        for problem in input_file.readlines():
            print(solve(problem.strip()))

if __name__ == '__main__':
    main()
