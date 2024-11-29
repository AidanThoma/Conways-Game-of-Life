import pygame
from settings import *
from map import *
import time

# Initilizing Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

clock = pygame.time.Clock()
map = Map()
GameEngine = Game()

running = True
while running:
    # Handle closing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Render Map
    map.render(screen)
    array = map.getGrid()
    GameEngine.getNewGrid(array)
    GameEngine.play()

    map.grabNewGrid(GameEngine.getGrid())


    time.sleep(0.2)
    

    pygame.display.flip()