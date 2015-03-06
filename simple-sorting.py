import sys

with open(sys.argv[1]) as input_file:
    for line in input_file.readlines():
        print(' '.join(map(lambda x: '{0:.3f}'.format(x),sorted(map(float, line.strip().split())))))
