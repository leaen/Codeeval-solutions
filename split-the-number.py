import sys
import string

alphabet = dict(zip(string.ascii_lowercase, range(26)))
numbers = '0123456789' 

def solve(problem):
    number, equation = problem.split()
    n1 = ''
    n2 = ''
    operator = ''
    for sym in equation:
        if sym not in alphabet:
            operator = sym
            continue
        
        if operator != '':
            n2 += number[alphabet[sym]]
        else:
            n1 += number[alphabet[sym]]
    
    if operator == '+':
        return int(n1) + int(n2)
    elif operator == '-':
        return int(n1) - int(n2)
    else:
        print('unknown operator {}'.format(operator))

def main():
    with open(sys.argv[1]) as input_file:
        for problem in input_file:
            print(solve(problem.strip()))

if __name__ == '__main__':
    main()
