import pygame

class Ghost:
    def __init__(self, x, y, maze):
        self.image = pygame.image.load("assets/ghost.png") 
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.maze = maze
        self.direction = 'up'
                
    def draw(self, surface):
        surface.blit(self.image, self.rect)
                
    def move(self):
        if self.direction == 'up':
            self.rect.y -= 40
            if self.rect.y <= 110 :  # If the ghost has reached the top of the screen
                self.direction = 'down'  # Change direction to down
        else:  # If direction is down
            self.rect.y += 40
            if self.rect.y >= 660:  # If the ghost has reached the bottom of the screen
                self.direction = 'up'  # Change direction to up
