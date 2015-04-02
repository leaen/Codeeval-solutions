import sys

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            cities = line.strip().split(';')[:-1]
            distances = []
            for city in cities:
                distances.append(int(city.split(',')[1]))
            
            last = 0
            result = []
            for d in sorted(distances):
                result.append(str(d-last))
                last = d

            print(','.join(result))

if __name__ == '__main__':
    main()
