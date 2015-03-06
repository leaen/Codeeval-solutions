import sys

def replace_strings(line):
    phrase, replacements = line.strip().split(';')
    
    




with open(sys.argv[1]) as input_file:
    for line in input_file.readlines():
        print(replace_strings(line))
