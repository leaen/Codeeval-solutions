import sys

def unscramble(phrase):
    text, order = phrase.split(';')
    text = text.split()
    order = map(int, order.split())
    
    return ' '.join([text[x-1] for x in order])

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            print(unscramble(line.strip()))

if __name__ == '__main__':
    main()
