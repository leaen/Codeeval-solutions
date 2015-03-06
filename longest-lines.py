import sys

def main():
    lines = []
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            lines.append(line)
    
    n = int(lines[0])
    number_of_lines = len(lines) - 1

    scores = sorted([(len(x), x.strip()) for i, x in enumerate(lines[1:])], reverse=True)
    
    for line in range(n):
        print(scores[line][1])

if __name__ == '__main__':
    main()
