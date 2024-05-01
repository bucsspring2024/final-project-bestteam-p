import pygame
import math

class Dog:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/dog.png") 
        self.image = pygame.transform.scale(self.image, (120, 120))  # Resize the image to 40x40 pixels
        self.rect = self.image.get_rect() 
        self.rect.center = (x, y)
        
    def move(self, dx, dy):
        #control diagonal speed
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2) / 2)
            dy = dy * (math.sqrt(2) / 2)
        self.rect.x += dx
        self.rect.y += dy
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)  # Draw the image onto the surface