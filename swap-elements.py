import sys

def solve(problem):
    l, actions = problem.split(':')
    l = l.split()
    actions = actions.split(',')

    for action in actions:
        n, m = action.split('-')
        n = int(n)
        m = int(m)
        l[n], l[m] = l[m], l[n]

    return l

def main():
    with open(sys.argv[1]) as input_file:
        for problem in input_file:
            print(' '.join(solve(problem.strip())))

if __name__ == '__main__':
    main()
