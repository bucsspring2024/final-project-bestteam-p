import pygame

background1 = pygame.image.load("assets/dungeon.jpeg")
background1 = pygame.transform.scale(background1, (900, 700))

font = pygame.font.Font(None, 36)
text = font.render("Start", True, (0, 0, 0))

font2 = pygame.font.Font(None, 150)
text2 = font2.render("ESCAPE", True, (255, 255, 255))

font3 = pygame.font.Font(None, 37)
text3 = font3.render("Enter at your own risk.", True, (255, 255, 255))


class Controller:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.start_button = pygame.Rect(325, 570, 200, 50)
        
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
        
        while menu_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button.collidepoint(event.pos):
                        self.state = "game"
                        menu_running = False
            self.screen.blit(background1, (0, 0))
            pygame.draw.rect(self.screen, (115, 147, 179), self.start_button)
            self.screen.blit(text, (self.start_button.x + 66, self.start_button.y + 12))
            self.screen.blit(text2, (215, 75))
            self.screen.blit(text3, (289, 182))
            pygame.display.flip()
        
    def gameloop(self):
        game_running = True
        
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            