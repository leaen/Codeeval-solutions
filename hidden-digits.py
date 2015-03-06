import sys

def find_hidden_digits(message):
    table = dict(zip('abcdefghij', range(0,10)))
    return ''.join(map(lambda x: x if x in '0123456789' else str(table[x]) if x in table else '', message)) 

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            decoded = find_hidden_digits(line.strip())
            if decoded == '':
                print('NONE')
            else:
                print(decoded)

if __name__ == '__main__':
    main()
