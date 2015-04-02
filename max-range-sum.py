import sys

def max_gains(history, width):
    best_total = -10000001
    section = []
    for e in history:
        section.append(e)
        if len(section) < width:
            continue
        best_total = max(best_total, sum(section))
        #print(','.join(map(str, section)))
        del section[0]

    return best_total

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            width, history = line.strip().split(';')
            width = int(width)
            history = list(map(int, history.split()))
            
            #print(','.join(map(str, history)))
            print(max_gains(history, width))

if __name__ == '__main__':
    main()
