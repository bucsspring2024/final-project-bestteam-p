import pygame
pygame.init()

class Door:
    def __init__(self, x, y, maze):
        self.image = pygame.image.load("assets/door.png")
        self.image = pygame.transform.scale(self.image, (1.5 * maze.cell_size, 1.5 * maze.cell_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.maze = maze
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)