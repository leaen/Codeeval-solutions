import sys

with open(sys.argv[1]) as input_file:
    for line in input_file.readlines():
        numbers = sorted(map(float, line.strip().split()))
        print(' '.join(['{0:.3f}'.format(x) for x in numbers]))
