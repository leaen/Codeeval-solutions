import sys

def lcs(s1, s2):
    # Setup matrix
    c = []
    for i in range(len(s2) + 1):
        c.append([0 for j in range(len(s1) + 1)])
   
    # Fill matrix 
    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if s1[j-1] == s2[i-1]:
                # Matching elements.
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max([c[i-1][j], c[i][j-1]])

    # Read subsequence from matrix
    result = []
    x, y = len(s2), len(s1)
    while x > 0 and y > 0:
        if c[x][y] == c[x-1][y]:
            x -= 1
        elif c[x][y] == c[x][y-1]:
            y -= 1
        else:
            result = [s2[x-1]] + result
            x -= 1
            y -= 1

    return ''.join(result)

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            s1, s2 = line.strip().split(';')
            print(lcs(s1, s2))

if __name__ == '__main__':
    main()
