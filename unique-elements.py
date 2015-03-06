import sys

def remove_duplicates(line):
        return dict.fromkeys(line.strip().split(',')).keys()

    with open(sys.argv[1]) as input_file:
            for line in input_file.readlines():
                        print(','.join(sorted(remove_duplicates(line))))

