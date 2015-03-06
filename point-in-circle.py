import sys
import math

def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def solve(problem):
    # Parse input
    center, radius, point = problem.split(';')
    center = [float(x) for x in center[9:-1].split(', ')]
    radius = float(radius[9:])
    point = [float(x) for x in point[9:-1].split(', ')]

    #print('center: {}\nradius: {}\npoint: {}'.format(center, radius, point))

    if distance(center, point) < radius:
        # Inside circle
        return 'true'
    else:
        # Outside circle
        return 'false'

def main():
    with open(sys.argv[1]) as input_file:
        for problem in input_file:
            print(solve(problem.strip()).lower())

if __name__ == '__main__':
    main()
