import sys
import json

def get_valid_ids(line):
    return [x['id'] for x in json.loads(line)['menu']['items'] if x != None and 'label' in x]

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            print(sum(get_valid_ids(line.strip())))

if __name__ == '__main__':
    main()
