import sys
import itertools

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            length, letters = line.strip().split(',')
            
            length = int(length)
            letters = letters.strip()

            result = set(''.join(e) for e in itertools.product(letters, repeat=length))
            result = sorted(result)
            
            print(','.join(result))
        
if __name__ == '__main__':
    main()
