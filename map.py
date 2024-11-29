import pygame
from settings import *
from GameEngine import *

class Map:
    # 1 means black space 0 means white space
    def __init__(self) -> None:

        self.grid = []
        self.load_grid_file()

    # Loading from file
    def load_grid_file(self):
        
        with open("map.txt", 'r') as file:
            for line in file:
                row = list(map(int, line.split()))
                self.grid.append(row)
        '''
        with open("Random\Conways Game of Life\map.txt", 'r') as file:
            for line in file:
                row = list(map(int, line.split()))
                self.grid.append(row)
        '''

    # Method for rendering map into pygame
    # Returns nothing
    def render(self, screen):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                # pixel coordinates
                tile_x = j * TILESIZE
                tile_y = i * TILESIZE

                if self.grid[i][j] == 0:
                    pygame.draw.rect(screen, (255, 255, 255), (tile_x, tile_y, TILESIZE, TILESIZE))
                elif self.grid[i][j] == 1:
                    pygame.draw.rect(screen, (0, 0, 0), (tile_x, tile_y, TILESIZE, TILESIZE))


    # Used to export map to file
    # Returns a file called map.txt
    def exportMap(self):
        with open("map.txt", "w") as file:
            for i in range(len(self.grid)):
                # file.write("[")
                for j in range(len(self.grid[0])):
                    file.write(f"{self.grid[i][j]} ")
                # file.write("],")
                file.write("\n")
    
    # Grab new array from GameEngine
    def grabNewGrid(self, array):
        self.grid = array
    
    def getGrid(self):
        return self.grid