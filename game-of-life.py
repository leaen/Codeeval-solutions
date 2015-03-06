import sys

MAP_WIDTH = 5
MAP_HEIGHT = 5
ITERATIONS = 3

def neighbours(x, y):
    for dx, dy in [(-1,1),(0,1),(1,1),(-1,0),(1,0),(-1,-1),(0,-1),(1,-1)]:
        nx = x + dx
        ny = y + dy
        
        if nx >= 0 and nx < MAP_WIDTH and ny >= 0 and ny < MAP_HEIGHT:
            yield (nx, ny)
        else:
            continue
        
def print_grid(grid):
    for line in grid:
        print(''.join(line))

def import_grid(location):
    grid = []
    with open(location) as maze_file:
        for row in maze_file:
            grid.append(list(row.strip()))
    return grid

def step(grid):
    # Deep copy a new list for the next iterateion to avoid step errors
    next_grid = list(grid)
    
    # Iterate over the grid cell, by cell
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            n_cells = list(map(lambda coord: grid[coord[0]][coord[1]], neighbours(i, j))) 
            alive_neighbours = sum(map(lambda x: 1 if x == '*' else 0, n_cells))
            
            print('cell at ({},{}) has {} neighbours and is value {}'.format(i, j, alive_neighbours, cell))
            
            if cell == '.' and alive_neighbours == 3:
                # Cell is reborn
                next_grid[i][j] = '*'
            elif cell == '*':
                if alive_neighbours < 2:
                    # Cell dies
                    next_grid[i][j] = '.'
                elif alive_neighbours == 2 or alive_neighbours == 3:
                    # Cell survives
                    next_grid[i][j] = '*'
                elif alive_neighbours > 3:
                    # Cell dies
                    next_grid[i][j] = '.'
            
    return next_grid

def main():
    print(list(neighbours(0,2)))
    grid = []
    
    grid = import_grid(sys.argv[1])
    
    for iteration in range(ITERATIONS):
        print('ITERATION {}'.format(iteration))
        print('-'*50)
        print_grid(grid)
        grid = step(grid)

if __name__ == '__main__':
    main()
