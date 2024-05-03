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
        self.pause_start_time = 0
        
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
            [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 2, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        def draw_maze(maze):    
            cell_size = 55
            wall_image = pygame.image.load("assets/Grey_Brick.jpeg")
            wall_image = pygame.transform.scale(wall_image, (cell_size, cell_size))
            exit = pygame.image.load("assets/door.png")
            exit = pygame.transform.scale(exit, (1.5 * cell_size, 1.5 * cell_size))
                        #takes in a variable maze
            for y, row in enumerate(maze):
                            for x, cell in enumerate(row):
                                if cell == 2:  # Door
                                    self.screen.blit(exit, (x * cell_size, y * cell_size, cell_size, cell_size))
                                elif cell == 1:  # Wall
                                    self.screen.blit(wall_image, (x * cell_size, y * cell_size, cell_size, cell_size))
                                elif cell == 0:  # Path
                                    pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))
       
       
        while game_running:
            clock = pygame.time.Clock()
            dog = Dog(55, 55)
            ghost_list = [Ghost(535, 550), Ghost(200, 400), Ghost(775, 320)]
            #frame rate
            clock.tick(13)
            dogImg = pygame.image.load("assets/dog.png")
            dogImg = pygame.transform.scale(dogImg, (55, 55))
            
            ghostImg = pygame.image.load("assets/ghost.png")
            self.screen.blit(dogImg, (55/55, 55//55))
            for ghost in ghost_list:
                self.screen.blit(ghostImg, (ghost.ghost_x//55, ghost.ghost_y//55))
            movement = ""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                #sets movement for dog direction
                #reset upon finishing dog,move()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        movement = "left"
                    if event.key == pygame.K_RIGHT:
                        movement = "right"
                    if event.key == pygame.K_DOWN:
                        movement = "down"
                    if event.key == pygame.K_UP:
                        movement = "up"
                elif event.type == pygame.KEYUP:
                    movement = ""
                
                if dog.move(movement):
                    pygame.transform.scale(dog.image, (55, 55))
                    dog.rect = dog.image.get_rect()
                    self.screen.blit(dog.image, dog.rect)
                    
                    
            else: 
                # If the game is paused, check if a second has passed
                if pygame.time.get_ticks() - self.pause_start_time >= 1500:
                    self.state = "won"
                    
                    
            pygame.display.flip()
            
        
    def gameoverloop(self):
        gameover_running = True
        while gameover_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            self.screen.blit(background2, (0, 0))
            self.screen.blit(text4, (248, 480))
            self.screen.blit(text5, (265, 555))
            pygame.display.flip()
   
    def wonloop(self):
        won_running = True
        
        while won_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            self.screen.blit(background3, (0, 0))
            self.screen.blit(text6, (235, 343))
            self.screen.blit(text7, (263, 430))
            pygame.display.flip()
            
                        
        