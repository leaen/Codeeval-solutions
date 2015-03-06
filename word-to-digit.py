import sys

lookup = { 'zero'  : '0',
           'one'   : '1',
           'two'   : '2',
           'three' : '3',
           'four'  : '4',
           'five'  : '5',
           'six'   : '6',
           'seven' : '7',
           'eight' : '8',
           'nine'  : '9' }

def words_to_digits(phrase):
    numbers = phrase.split(';')
    return ''.join(map(lambda x: lookup[x], numbers))

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            print(words_to_digits(line.strip()))

if __name__ == '__main__':
    main()
