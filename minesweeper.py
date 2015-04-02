import sys
import itertools

class Minesweeper(object):
    def neighbours(self, pos):
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            x = pos[0] + dx
            y = pos[1] + dy

            if 0 <= x < self.width and 0 <= y < self.height:
                yield (x, y)

    def __init__(self, board):
        # Parse input
        coords, board = board.split(';')
        coords = coords.split(',')
        coords = [int(x) for x in coords]
        self.width = coords[0]
        self.height = coords[1]
        self.board = [board[n:n+self.width] for n in range(0, len(board), 3)]
        self.board = list(map(list, self.board))
        print(self.board)

    def getSerializedBoard(self):
        for i in range(self.height):
            for j in range(self.width):
                print('({},{})'.format(i, j))
                if self.board[i][j] == '.':
                    mines = 0
                    for n in self.neighbours((i,j)):
                        if n == '*':
                            mines += 1
                    self.board[i][j] = str(mines)
        board_str = ''.join(list(itertools.chain(*self.board)))
        print(board_str)
        return board_str

def main():
        with open(sys.argv[1]) as input_file:
        for game in input_file.readlines():
            m = Minesweeper(game.strip())
            print(m.getSerializedBoard())

if __name__ == '__main__':
    main()
