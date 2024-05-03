import pygame
from src.dog import Dog
from src.ghost import Ghost


pygame.init()

background1 = pygame.image.load("assets/dungeon.jpeg")
background1 = pygame.transform.scale(background1, (1100, 900))

background2 = pygame.image.load("assets/bad_ending.jpeg")
background2 = pygame.transform.scale(background2, (1100, 900))

background3 = pygame.image.load("assets/woods.jpg")
background3 = pygame.transform.scale(background3, (1100, 900))

font = pygame.font.Font(None, 36)
text = font.render("Start", True, (0, 0, 0))

font2 = pygame.font.Font(None, 150)
text2 = font2.render("ESCAPE", True, (255, 255, 255))

font3 = pygame.font.Font(None, 37)
text3 = font3.render("Enter at your own risk.", True, (255, 255, 255))

font4 = pygame.font.Font(None, 100)
text4 = font4.render("GAME OVER", True, (255, 255, 255))

font5 = pygame.font.Font(None, 30)
text5 = font5.render("Hopefully the next traveller fares better.", True, (255, 255, 255))

font6 = pygame.font.Font(None, 100)
text6 = font6.render("You Escaped", True, (255, 255, 255))

font7 = pygame.font.Font(None, 30)
text7 = font7.render("Somehow, you lived to see another day", True, (255, 255, 255))


class Controller:
    def __init__(self):
        self.screen = pygame.display.set_mode((1100, 850))
        self.start_button = pygame.Rect(325, 570, 200, 50)
        self.pause = False
        
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

        dungeon = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
            [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        def draw_maze(maze):    
            cell_size = 55
            wall_image = pygame.image.load("assets/Grey_Brick.jpeg")
            wall_image = pygame.transform.scale(wall_image, (cell_size, cell_size))
                        #takes in a variable maze
            for y, row in enumerate(maze):
                            for x, cell in enumerate(row):
                                if cell == 1:  # Wall
                                    self.screen.blit(wall_image, (x * cell_size, y * cell_size, cell_size, cell_size))
                                elif cell == 0:  # Path
                                    pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))
        
        pygame.image.load("assets/door.png")
        pygame.transform.scale(self.image, (1.5 * 55, 1.5 * 55))
        self.rect = self.image.get_rect()
        self.screen.blit(self.image, self.rect)
        
        while game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            clock = pygame.time.Clock()
            dog = Dog(55, 55)
            ghost_list = [Ghost(535, 550),
            Ghost(200, 400),
            Ghost(775, 320)
            ]
                #frame rate
            clock.tick(13)
            
            if not self.pause:
                dog.draw(self.screen)
                for ghost in ghost_list:
                    ghost.move()
                    ghost.draw(self.screen)
            
                        
        