from src.maze import Maze
from src.dog import Dog
from src.door import Door
from src.ghost import Ghost

my_maze = Maze()
exit = Door(1015, 689, my_maze)
player = Dog(my_maze.cell_size, my_maze.cell_size, my_maze)
ghosts = [
    Ghost(535, 550, my_maze),
    Ghost(200, 400, my_maze),
    Ghost(775, 320, my_maze)
]

import pygame
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
        self.screen = pygame.display.set_mode((1100, 900))
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
            #frame right
            clock.tick(13)
    
            self.screen.fill("dark gray")
            draw_maze(maze)
            
            
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
                
            #draw player
            if not pause:
                exit.draw(self.screen)
                player.draw(self.screen)
                for ghost in ghosts:
                    ghost.move()
                    ghost.draw(self.screen)
                
                    if player.rect.colliderect(ghost.rect):
                        pause = True
                        pause_start_time = pygame.time.get_ticks()

                if player.rect.colliderect(exit.rect):
                    self.state = "won"

            else: 
                # If the game is paused, check if a second has passed
                if pygame.time.get_ticks() - pause_start_time >= 1500:
                    self.state = "gameover"
                
                
                
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