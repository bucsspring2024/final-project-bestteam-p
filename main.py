import pygame
from src.mouse import Mouse
#  from src.maze import Maze


pygame. init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)

def draw_maze(arg = None):
    num1 = (screen_height // 32)
    num2 = (screen_width // 32)
    for i in range(len(arg)):
        for j in range(len(arg[i])):
            if arg[i][j] == 1:
                pygame.draw.line(screen, "blue", (j * num2 + (0.5 * num2), i * num1), 
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)
            if arg[i][j] == 2:
                pygame.draw.line(screen, "blue", (j * num2, i * num1 + (0.5 * num1)), 
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            

maze = [
    [2, 2, 2, 2, 2],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [2, 2, 2, 2, 2]
]
    



#define movement variables
moving_left = False
moving_right = False
moving_down = False
moving_up = False


#create player
player = Mouse(100, 100)

#main game loop
run = True
while run:
    #frame right
    clock.tick(60)
    
    screen.fill("black")
    draw_maze(maze)
    
     # Draw the maze
    
    #calculate player movement
    dx = 0
    dy = 0
    if moving_left == True:
        dx = -3
    if moving_right == True:
        dx = 3
    if moving_down == True:
        dy = 3
    if moving_up == True:
        dy = -3
    
    #move player
    player.move(dx, dy)
    
    
    #draw player
    player.draw(screen)
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #keyboard commands
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_DOWN:
                moving_down = True
            if event.key == pygame.K_UP:
                moving_up = True
        
        #button release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_DOWN:
                moving_down = False
            if event.key == pygame.K_UP:
                moving_up = False
            
    pygame.display.flip()
            
pygame.quit()






# def main():
#     pygame.init()
#     #Create an instance on your controller object
#     #Call your mainloop
    
#     ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# # https://codefather.tech/blog/if-name-main-python/
# if __name__ == '__main__':
#     main()
