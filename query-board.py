import sys

class QueryBoard():
    def __init__(self, width=256, height=256):
        self.width = width
        self.height = height
        self.board = []
        
        # Zero out board
        for y in range(height):
            self.board.append([0 for x in range(width)])

    def setRow(self, i, x):
        self.board[i] = [x for i in range(self.width)]        

    def setCol(self, j, x):
        for row in self.board:
            row[j] = x

    def queryRow(self, i):
        return sum(self.board[i])

    def queryCol(self, j):
        return sum([row[j] for row in self.board])

def main():
    b = QueryBoard()
    actions = []
    
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            actions.append(line.strip())
    
    actions = [x.split() for x in actions]
    
    for action in actions:
        if action[0] == 'SetCol':
            b.setCol(int(action[1]), int(action[2]))
        elif action[0] == 'SetRow':
            b.setRow(int(action[1]), int(action[2]))
        elif action[0] == 'QueryCol':
            print(b.queryCol(int(action[1])))
        elif action[0] == 'QueryRow':
            print(b.queryRow(int(action[1])))
        else:
            print('unknown action {}'.format(action))
    
if __name__ == '__main__':
    main()
