#A simple file for debugging
class Game:

    def __init__(self) -> None:
        self.grid = []
        self.nextGrid = []

    
    
    # Method for grabbing neighbors values
    # Returns an self.grid of all the values of neighbors
    def grabNeighbors(self, i, j):
        test_array = []

        # Add neighbors if it's at top left
        if i == 0 and j == 0:
            test_array.append(self.grid[i+1][j])
            test_array.append(self.grid[i][j+1])
            test_array.append(self.grid[i+1][j+1])
            return test_array
        
        # Add neighbors if it's at top left
        elif i == 0 and j == len(self.grid[0])-1:
            test_array.append(self.grid[i+1][j])
            test_array.append(self.grid[i][j-1])
            test_array.append(self.grid[i+1][j-1])
            return test_array
        
        # Add neighbors if it's at bottom right
        elif i == len(self.grid)-1 and j == 0:
            test_array.append(self.grid[i-1][j])
            test_array.append(self.grid[i][j+1])
            test_array.append(self.grid[i-1][j+1])
            return test_array
        
        # Add neighbors if it's at bottom left
        elif i == len(self.grid)-1 and j == len(self.grid[0])-1:
            test_array.append(self.grid[i-1][j])
            test_array.append(self.grid[i][j-1])
            test_array.append(self.grid[i-1][j-1])
            return test_array
        
        
        # Add neighbors if it's at the top
        elif i == 0:
            test_array.append(self.grid[i+1][j])
            test_array.append(self.grid[i][j+1])
            test_array.append(self.grid[i][j-1])
            test_array.append(self.grid[i+1][j-1])
            test_array.append(self.grid[i+1][j+1])
            return test_array
        
        # Add neighbors if it's at the bottom
        elif i == len(self.grid)-1:
            test_array.append(self.grid[i-1][j])
            test_array.append(self.grid[i][j+1])
            test_array.append(self.grid[i][j-1])
            test_array.append(self.grid[i-1][j-1])
            test_array.append(self.grid[i-1][j+1])
            return test_array
        
        # Add neighbors if it's at the front
        elif j == 0:
            test_array.append(self.grid[i+1][j])
            test_array.append(self.grid[i-1][j])
            test_array.append(self.grid[i][j+1])
            test_array.append(self.grid[i-1][j+1])
            test_array.append(self.grid[i+1][j+1])
            return test_array
        
        # Add neighbors if it's at the back
        elif j == len(self.grid[i])-1:
            test_array.append(self.grid[i+1][j])
            test_array.append(self.grid[i-1][j])
            test_array.append(self.grid[i][j-1])
            test_array.append(self.grid[i-1][j-1])
            test_array.append(self.grid[i+1][j-1])
            return test_array
        
        # Add neighbors if it's not at front, back, top, or bottom
        else:
            test_array.append(self.grid[i+1][j-1])
            test_array.append(self.grid[i+1][j])
            test_array.append(self.grid[i+1][j+1])
            test_array.append(self.grid[i][j+1])
            test_array.append(self.grid[i-1][j+1])
            test_array.append(self.grid[i-1][j])
            test_array.append(self.grid[i-1][j-1])
            test_array.append(self.grid[i][j-1])
            return test_array

    # Method for playing the game
    # Changes grid[i][j] depending of the rules
    ''' 
    Rules:

    Cell dies if it has less than 2 neighbors
    Cell with 2 or 3 neighbors lives for the next turn
    Cell with 3 or more neighbors dies
    A dead cell comes back to life if it has exactly 3 neighbors

    Life and Death are represented by 0 [Death] and 1 [Life]

    '''
    def playCell(self, i, j, next_grid):
        neighbors = self.grabNeighbors(i, j)
        cell = self.grid[i][j]
        alive_neighbors = neighbors.count(1)
        
        # If cell is alive
        if cell == 1:
            # If cell neighbors < 3 it dies
            if alive_neighbors < 2:
                next_grid[i][j] = 0
                
            # elif cell neighbors = 2 or cell neighbors = 3 it lives
            elif alive_neighbors in [2, 3]:
                next_grid[i][j] = 1
                
            # elif cell neighbors > 3 it dies
            elif alive_neighbors > 3:
                next_grid[i][j] = 0
                
        
        # Else Cell is dead
        else:
            # If cell neighbors = 3 it life
            if neighbors.count(1) == 3:
                next_grid[i][j] = 1

    

    # A method for running playCell on self.grid
    # Changes self.grid to the next frame
    def play(self):
        next_grid = [[self.grid[i][j] for j in range(len(self.grid[0]))] for i in range(len(self.grid))]

        # Iterate through each cell and apply playCell
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.playCell(i, j, next_grid)

        # Update the original grid with the next state
        self.grid = next_grid



    def debugCell(self, i, j):
        neighbors = self.grabNeighbors(i, j)
        cell = self.grid[i][j]
        alive_neighbors = neighbors.count(1)
        print(f"Cell Value {cell} Neighbors {neighbors} Neighbors value count {neighbors.count(1)}")

        # If cell is alive
        if cell == 1:
            # If cell neighbors < 3 it dies
            if neighbors.count(1) < 2:
                print("died")
                
            # elif cell neighbors = 2 or cell neighbors = 3 it lives
            elif neighbors.count(1) == 2 or neighbors.count(1) == 3:
                print("lives")
                
            # elif cell neighbors > 3 it dies
            elif neighbors.count(1) > 3:
                print("dies")
                
        
        # Else Cell is dead
        else:
            # If cell neighbors = 3 it life
            if neighbors.count(1) == 3:
                print('revived')



    # An mutator method for changing self.grid
    def getNewGrid(self, grid):
        self.grid = grid
    
    # An accessor method for self.grid
    def getGrid(self):
        return self.grid
    
    # Printing the grid
    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, row)) for row in self.grid])