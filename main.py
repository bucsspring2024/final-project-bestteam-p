import pygame
from src.mouse import Mouse


pygame. init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#create clock for frame rate
clock = pygame.time.Clock()

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
    
    #control frame rate
    clock.tick(60)
    
    screen.fill("green")
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
            
    pygame.display.update()
            
pygame.quit()






# def main():
#     pygame.init()
#     #Create an instance on your controller object
#     #Call your mainloop
    
#     ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# # https://codefather.tech/blog/if-name-main-python/
# if __name__ == '__main__':
#     main()
