import pygame
from src.maze import Maze

pygame.init()

class Dog:
    def __init__(self, x_coord, y_coord):
        self.image = pygame.image.load("assets/dog.png")
        self.dog_x = x_coord
        self.dog_y = y_coord
        self.board = Maze()
      
    def move(self, direction):
        #takes direction from controller
        #needs is_wall from maze to determine if loc = 1
        if direction == 'right' and not self.board.is_wall((self.dog_x + 55)//55, (self.dog_y)//55):
            self.dog_x += 55
            
        elif direction == 'left' and not self.board.is_wall((self.dog_x - 55)//55, (self.dog_y)//55):
            self.dog_x -= 55
            
        elif direction == 'up' and not self.board.is_wall((self.dog_x)//55, (self.dog_y - 55)//55):
            self.dog_y -= 55
            
        elif direction == 'down' and not self.board.is_wall((self.dog_x)//55, (self.dog_y + 55)//55):
            self.dog_y += 55
            
        if self.board.is_door(self.dog_x//55, self.dog_y//55):
            return False
        else:   
            return True
        
        
    def check_position(self):
        #used by CONTROLLER to update dog pos
        #return x and y coord of pixels
        return[self.dog_x, self.dog_y]