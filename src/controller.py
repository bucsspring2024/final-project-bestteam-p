import pygame
from src import Mouse

class Controller:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.background = pygame.image.load('path_to_your_image.png')  # Load the image
        self.background = pygame.transform.scale(self.background, (800, 600))  # Scale the image to fit the screen
        
    def mainloop(self):
        self.state = "menu"
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            if self.state == "menu":
                self.menuloop()
            elif self.state == "game":
                self.gameloop()
            elif self.state == "gameover":
                self.gameoverloop()
            else:
                break
            
    def menuloop(self):
        menu_running = True
        start_button = pygame.Rect(100, 100, 200, 50)
        font = pygame.font.Font(None, 36)
        text = font.render("Start", True, (255, 255, 255))
        text_rect = text.get_rect(center=start_button.center)
        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        self.state = "game"
                        menu_running = False
            self.screen.blit(self.background, (0, 0))
            pygame.draw.rect(self.screen, (255, 0, 0), start_button)
            pygame.display.flip()
            
    def gameloop(self):
        
    def gameoverloop(self):
        while True:
            if 