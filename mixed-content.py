import sys
import re

def seperate_content(content):
    words = ','.join(re.findall(r'[A-Za-z]+', content))
    numbers = ','.join(re.findall(r'[0-9]+', content))
    
    if len(words) == 0:
        return numbers 

    if len(numbers) == 0:
        return words

    return '|'.join([words, numbers])

def main():
    with open(sys.argv[1]) as input_file:
        for content in input_file:
            print(seperate_content(content.strip()))

if __name__ == '__main__':
    main()
