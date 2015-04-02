import math
import sys

def find_summing_squares(n):
    i = 0
    j = int(1 + math.sqrt(n))
    count = 0
    # 'i' will always be increased, and j will always be decreased. We will
    # stop if i > j, so we can avoid duplicate pairs.
    while i <= j:
        s = i * i + j * j
        if s < n:
            # If any answers exist for this i, they were with higher j values.
            # So, increment i.
            i +=  1
        elif s > n:
            # Likewise, if there was an answer with this j, it was found with
            # a smaller i.  so, decrement it.
            j -= 1
        else:
            # Found a solution. Count it, and then move both i and j, because
            # they will be found in at most one solution pair.
            count += 1
            i += 1
            j -= 1
    return count

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            print(find_summing_squares(int(line.strip())))

if __name__ == '__main__':
    main()
