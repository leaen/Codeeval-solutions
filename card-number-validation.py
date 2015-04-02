import sys
from functools import reduce

def check_card(card):
    # Reverse the digits to make selecting every second digit easier.
    card = list(reversed(card))

    # Multiply the value of every second digit by 2.
    card[1::2] = map(lambda x: str(int(x)*2), card[1::2])

    # Digits 10 or larger have their own digits added together.
    for index, digit in enumerate(card):
        card[index] = reduce(lambda a, x: int(a) + int(x), digit)

    # Ensure all elements are integers and find the sum of all digits.
    card = [int(x) for x in card]
    total = sum(card)

    # Check if the modulo is equal to 0.
    if (total%10 == 0):
        return True
    else:
        return False

def main():
    with open(sys.argv[1]) as input_file:
        for card_string in input_file.readlines():
            card_string = card_string.strip().replace(' ', '')
            if check_card(card_string):
                print(1)
            else:
                print(0)

if __name__ == '__main__':
    main()
