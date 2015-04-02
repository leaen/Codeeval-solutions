import sys

# Basic implementation of a stack, all the features we need for
# this purpose (no peeking).

class Stack(object):
    def __init__(self):
        self.memory = []

    def push(self, val):
        self.memory += (val,)

    def pop(self):
        if len(self.memory) > 0:
            ret = self.memory[-1]
            del self.memory[-1]
            return ret
        else:
            Exception("Stack empty cannot pop")

    def items(self):
        return len(self.memory)

def solve(problem):
    output = []

    # Create stack and push all items onto it.

    stack = Stack()
    for item in problem.strip().split(' '):
        stack.push(item)

    # Run through stack until it's empty, printing every 2nd item.

    printed_last = False
    while (stack.items() > 0):
        if (printed_last == False):
            # We want to print this one.

            output += (stack.pop(),)
            printed_last = not printed_last

        else:
            # We don't want to print this one.

            stack.pop()
            printed_last = not printed_last

    # Return solution as a string.

    return ' '.join(output)

def solve_cheating(problem):
    # This is just obviously an abuse of the problem but I thought
    # i'd leave it in. Also it's far faster, for obvious reasons.

    items = []
    for item in problem.strip().split(' ')[::-2]:
        items += (item,)
    return ' '.join(items)

def main():
    with open(sys.argv[1]) as input_file:
        for problem in input_file.readlines():
            print(solve(problem))

if __name__ == '__main__':
    main()
