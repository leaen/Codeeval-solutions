import sys

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            words = line.strip().split(' ')
            words = [word[0].title() + word[1:] for word in words]

            print(' '.join(words))

if __name__ == '__main__':
    main()
