import sys
import re

def substring_to_regex(substring):
    return re.sub(r'[^\\]\*', '.', substring)

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            test_string, substring = line.strip().split(',')
            regex = substring_to_regex(substring)
            
            try:
                if re.findall(regex, re.escape(test_string)):
                    print('true')
                else:
                    print('false')
            except:
                print('false')

if __name__ == '__main__':
    main()
