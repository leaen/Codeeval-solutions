import sys
import math

def distance(x1, x2, y1, y2):
    return math.sqrt(math.pow(y2-y1, 2) + math.pow(x2-x1, 2))

def main():
    points = []
    num_of_points = 0

    with open(sys.argv[1]) as input_file:
        num_of_points = int(input_file.readline())
        for _ in range(num_of_points):
            line = input_file.readline()
            x, y = list(map(int, line.strip().split()))
            points.append([x,y])

    best_distance = float("inf")

    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            best_distance = min(best_distance,
                                distance(p1[0], p2[0], p1[1], p2[1]))

    print("{:.4f}".format(round(best_distance, 4)))

if __name__ == '__main__':
    main()
