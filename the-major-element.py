import sys

def find_major_element(problem):
    problem = problem.split(',')
    stop_len = len(problem) // 2

    history = {}

    for e in problem:
        if e not in history:
            history[e] = 0

        history[e] += 1
        if history[e] > stop_len:
            return e

def main():
    with open(sys.argv[1]) as input_file:
        for problem in input_file:
            print(find_major_element(problem.strip()))

if __name__ == '__main__':
    main()
