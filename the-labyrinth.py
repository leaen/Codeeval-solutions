import sys
from heapq import *

class Node():
    def __init__(self, node_id, symbol, coord):
        self.node_id = node_id
        self.finalized = False
        self.previous = None
        self.distance = None
        self.coord = coord
        self.symbol = symbol

    def __str__(self):
        return self.symbol

    def isFinalized(self):
        return self.finalized

    def setFinalized(self, finalized):
        self.finalized = finalized
    
    def getDistance(self):
        return self.distance

    def setDistance(self, distance):
        self.distance = distance

    def getPrevious(self):
        return self.previous

    def setPrevious(self, previous):
        self.previous = previous

    def getID(self):
        return self.node_id
   
    def getCoord(self):
        return self.coord

class Maze():
    def __init__(self, grid):
        self.maze = grid
        self.width = len(grid[0])
        self.height = len(grid)
        self.solved = False
   
    def coordToID(self, x, y):
        return x + (y * self.width)

    def IDToCoord(self, ID):
        return [ID//self.width, ID%self.width]

    def setCell(self, sym, x, y):
        self.maze[x][y] = sym

    def solve(self):
        # Solve maze
        if self.solved:
            print('Already solved!')
            return

        # Find entry point
        entryCoord = ([i for i,e in enumerate(self.maze[0]) if e == ' '][0], 0)
        entryID = self.coordToID(*entryCoord) 

        # Find exit point
        exitCoord = ([i for i,e in enumerate(self.maze[self.height-1]) if e == ' '][0], self.height-1)
        exitID = self.coordToID(*exitCoord)

        # Add entry point to queue
        entryNode = Node(entryID, self.maze[entryCoord[0]][entryCoord[1]], entryCoord)
        self.setCell(entryNode, *entryCoord)
        queue = []
        heappush(queue, (0, entryNode))
        
        # Start search
        seenIDs = []
        while(queue):
            # Get next node from queue
            e = heappop(queue)
            priority, item = e[0], e[1]

            # Check for new node
            if item.getID() not in seenIDs:
                seenIDs.append(item.getID())

            # Find neighbouring nodes
            

            # Calculate distances
            # Add new nodes to queue
            # Have we found the exit point?

        # Found the exit point
        # Trace steps back by id
        # Mark each step with a '+'

    def __str__(self):
        return '\n'.join([''.join([str(x) for x in row]) for row in self.maze])

def main():
    gridInput = []
    with open(sys.argv[1]) as input_file:
        for line in input_file:
            gridInput.append(list(line.strip()))
    
    maze = Maze(gridInput)
    maze.solve()
    print(str(maze))

if __name__ == '__main__':
    main()
