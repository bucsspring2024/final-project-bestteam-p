import pygame
pygame.init()

class Ghost:
    def __init__(self, x_coord, y_coord):
        self.image = pygame.image.load("assets/ghost.png")
        self.direction = 'up'
        self.ghost_x = x_coord
        self.ghost_y = y_coord
        
    def move(self):
        if self.direction == 'up':
            self.rect.y -= 40
            if self.rect.y <= 110 :  # If the ghost has reached the top of the screen
                self.direction = 'down'  # Change direction to down
        else:  # If direction is down
            self.rect.y += 40
            if self.rect.y >= 660:  # If the ghost has reached the bottom of the screen
                self.direction = 'up'  # Change direction to up
                
    def check_position(self):
        #used by CONTROLLER to update dog pos
        #return x and y coord of pixels
        return[self.ghost_x, self.ghost_y]