import pygame
import math
from src.maze import Maze
screen_width = 1100
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

cell_size = cell_size = screen_width // len(maze[0])

Maze = Maze(maze)

class Dog:
    def __init__(self, x, y, maze):
        print(x, y)
        self.image = pygame.image.load("assets/dog.png") 
        self.image = pygame.transform.scale(self.image, (maze.cell_size, maze.cell_size))  # Resize the image to 40x40 pixels
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        self.maze = maze
        print(x,y, self.rect.x, self.rect.y)
        
            
    def update(self, direction):
        # if self.maze.is_wall == 1:
        if direction == 'right': 
            self.rect.x += 55
        elif direction == 'left':
            self.rect.x -= 55
        elif direction == 'up':
            self.rect.y -= 55
        elif direction == 'down':
            self.rect.y += 55
        print(self.rect.x, self.rect.y)
    
    def diagonal(self, dx, dy):
        #control diagonal speed
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2) / 2)
            dy = dy * (math.sqrt(2) / 2)
        self.rect.x += dx
        self.rect.y += dy
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self, dx, dy):
        if self.maze.check_position(self.rect.x + dx, self.rect.y + dy):
            self.rect.x += dx
            self.rect.y += dy