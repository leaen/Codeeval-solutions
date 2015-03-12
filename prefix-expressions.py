import sys

operate = { '+' : lambda x, y: x+y,
            '/' : lambda x, y: x//y,
            '*' : lambda x, y: x*y,
            '-' : lambda x, y: x-y }

def evaluate(line):
    line = line.split()
    s = []

    for symbol in line[::-1]:
        if symbol not in ('-', '*', '/', '+'):
            s.append(int(symbol))
        else:
            operand1 = s.pop()
            operand2 = s.pop()
            result = operate[symbol](operand1, operand2)
            s.append(result)
        
    return s.pop()

def main():
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            print(evaluate(line.strip()))

if __name__ == '__main__':
    main()
