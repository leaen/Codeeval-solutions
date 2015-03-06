import sys

def decrypt(phrase):
    sentence = list(map(int, phrase.split()[4:]))
    offset = 32 - min(sentence)
    return ''.join(map(lambda x: chr(x + offset), sentence))    

def main():
    with open(sys.argv[1]) as input_file:
        for phrase in input_file:
            print(decrypt(phrase.strip()))

if __name__ == '__main__':
    main()
