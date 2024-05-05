import pygame
from src.ghost import Ghost
from src.dog import Dog
from src.door import Door
from src.maze import Maze

pygame.init()

screen_width = 1100
screen_height = 850
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)

maze = [
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

pause_start = 0

my_maze = Maze(maze)

exit = Door(1015, 689, my_maze)
player = Dog(my_maze.cell_size, my_maze.cell_size, my_maze)
ghosts = [
    Ghost(535, 550, my_maze),
    Ghost(200, 400, my_maze),
    Ghost(775, 320, my_maze)
]

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

font4 = pygame.font.Font(None, 150)
text4 = font4.render("GAME OVER", True, (255, 255, 255))

font5 = pygame.font.Font(None, 40)
text5 = font5.render("Hopefully the next traveller fares better.", True, (255, 255, 255))

font6 = pygame.font.Font(None, 100)
text6 = font6.render("You Escaped", True, (255, 255, 255))

font7 = pygame.font.Font(None, 30)
text7 = font7.render("Somehow, you lived to see another day", True, (255, 255, 255))



class Controller:
    def __init__(self):
        self.screen = pygame.display.set_mode((1100, 900))
        self.start_button = pygame.Rect(450, 650, 200, 50)
        
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
            self.screen.blit(text2, (325, 75))
            self.screen.blit(text3, (405, 190))
            pygame.display.flip()
            
    def gameloop(self):
        run = True
        
        pause = False
        
        moving_left = False
        moving_right = False
        moving_down = False
        moving_up = False

        while run:
            #frame right
            clock.tick(13)
                    
            screen.fill("dark gray")
            my_maze.draw_maze(maze)
                    
            #event handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                #keyboard commands
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        moving_left = True
                    if event.key == pygame.K_RIGHT:
                        moving_right = True
                    if event.key == pygame.K_DOWN:
                        moving_down = True
                    if event.key == pygame.K_UP:
                        moving_up = True
                        
            #button release
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        moving_left = False
                    if event.key == pygame.K_RIGHT:
                        moving_right = False
                    if event.key == pygame.K_DOWN:
                        moving_down = False
                    if event.key == pygame.K_UP:
                        moving_up = False
                                
            # Update the game state
            print(player.rect.x, player.rect.y)
            if moving_right and not my_maze.is_wall(player.rect.x + 55, player.rect.y):
                player.update('right')
            elif moving_left and not my_maze.is_wall(player.rect.x - 55, player.rect.y):
                player.update('left')
            if moving_up and not my_maze.is_wall(player.rect.x, player.rect.y - 55):
                player.update('up')
            elif moving_down and not my_maze.is_wall(player.rect.x, player.rect.y + 55):
                player.update('down')
                
                
                
            
            exit.draw(screen)
            player.draw(screen)
            for ghost in ghosts:
                ghost.move()
                ghost.draw(screen)
                        
                if player.rect.colliderect(ghost.rect):
                    run = False
                    self.state = "gameover"
                    self.gameoverloop()

                if player.rect.colliderect(exit.rect):
                    run = False
                    self.state = "won"
                    self.wonloop()
                            
            pygame.display.flip()
                            
        pygame.quit()
                    

    def gameoverloop(self):
        gameover_running = True
        while gameover_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            self.screen.blit(background2, (0, 0))
            self.screen.blit(text4, (235, 480))
            self.screen.blit(text5, (290, 600))
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