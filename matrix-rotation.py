import sys
import math
import itertools

def rotate_serial_matrix(matrix):
    chars = matrix.split()
    width = int(math.sqrt(len(chars)))
    
    rotated_matrix = [chars[n:n+width] for n in range(0, len(chars), width)]
    rotated_matrix = [[row[i] for row in rotated_matrix] for i in range(width)]
    rotated_matrix = [reversed(row) for row in rotated_matrix]
    return ' '.join(list(itertools.chain(*rotated_matrix)))

with open(sys.argv[1]) as input_file:
    for line in input_file:
        print(rotate_serial_matrix(line))

