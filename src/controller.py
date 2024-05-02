import pygame

class Controller:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        
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
            
    