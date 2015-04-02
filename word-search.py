import sys

orig_grid = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]

def neighbours(x, y):
    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        nx = x + dx
        ny = y + dy

        #print('next neighbour at ({},{})'.format(nx, ny))

        if nx < 0 or nx > 2 or ny < 0 or ny > 3:
            continue

        yield (nx, ny)

def check(x, y, word, grid):
    if grid[x][y] == word[0]:
        message = 'Found "{}" at ({},{}), still need to find "{}"'
        #print(message.format(word[0], x, y, word[1:]))

        # Good!, another letter, now let's recurse and try again
        if len(word) == 1:
            # That's the end! return True
            return True

        # Mark the cell as used
        grid[x][y] = '.'

        # Check neighbours
        for next_x, next_y in neighbours(x, y):
            if check(next_x, next_y, word[1:], grid):
                return True

    # No luck here
    return False

def isWordOnGrid(word):
    grid = list(orig_grid)
    for i, row in enumerate(grid):
        for j, _ in enumerate(row):
            #print('checking ({},{})'.format(i, j))
            if check(i, j, word, grid.copy()):
                return True
    return False

def printGrid(grid):
    print('\n'.join([''.join(x) for x in grid]))

def main():
    with open(sys.argv[1]) as input_file:
        for word in input_file:
            #print('-'*50)
            #print()
            #printGrid(grid)
            #print()
            print(isWordOnGrid(word.strip()))

if __name__ == '__main__':
    main()
