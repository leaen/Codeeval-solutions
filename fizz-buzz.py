import sys

def fizzbuzz(fizz_number, buzz_number, limit):
    def map_fizzbuzz(number):
        if (number%fizz_number==0 and number%buzz_number==0):
            return "FB"
        if (number%fizz_number==0):
            return "F"
        if (number%buzz_number==0):
            return "B"
        return str(number)
    solution = map(map_fizzbuzz, range(1,limit+1))
    return ' '.join(list(solution))

def main():
    with open(sys.argv[1]) as input_file:
        for game in input_file:
            fizz, buzz, limit = game.strip().split(' ')
            print(fizzbuzz(int(fizz), int(buzz), int(limit)))

if __name__ == '__main__':
    main()
