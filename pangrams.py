import sys
import string

def find_missing_letters(pangram):
    missing_letters = []
    for letter in string.ascii_lowercase:
        if letter not in pangram:
            missing_letters.append(letter)
    
    if len(missing_letters) == 0:
        return 'NULL'
    else:
        return ''.join(missing_letters)

def main():
    with open(sys.argv[1]) as input_file:
        for pangram in input_file:
            print(find_missing_letters(pangram.strip().lower()))

if __name__ == '__main__':
    main()
