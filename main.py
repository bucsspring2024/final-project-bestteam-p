import pygame
import math
# from src.dog import Dog
# from src.maze import Maze


pygame. init()

screen_width = 1100
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

font = pygame.font.SysFont(None, 30)

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
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

moving_left = False
moving_right = False
moving_down = False
moving_up = False

pause = False
pause_start = 0

class Maze:
    def __init__(self, maze):
        self.maze = maze
        self.cell_size = screen_width // len(maze[0])
        self.wall_image = pygame.image.load("assets/Grey_Brick.jpeg")
        self.wall_image = pygame.transform.scale(self.wall_image, (self.cell_size, self.cell_size))
    
    def draw_maze(maze):    
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == 1:  # Wall
                    screen.blit(wall_image, (x * cell_size, y * cell_size, cell_size, cell_size))
                elif cell == 0:  # Path
                    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))
                
   
    def is_wall(self, x, y):
        a = x // self.cell_size
        b = y // self.cell_size
        #print(x, y, a, b)
        return self.maze[b][a] == 1
    

my_maze = Maze(maze)


class Door:
    def __init__(self, x, y, maze):
        self.image = pygame.image.load("assets/door.png")
        self.image = pygame.transform.scale(self.image, (1.5 * maze.cell_size, 1.5 * maze.cell_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.maze = maze
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    
    
class Dog:
    def __init__(self, x, y, maze):
        print(x, y)
        self.image = pygame.image.load("assets/dog.png") 
        self.image = pygame.transform.scale(self.image, (maze.cell_size, maze.cell_size))  # Resize the image to 40x40 pixels
        self.rect = self.image.get_rect() 
        self.rect.x = x
        self.rect.y = y
        self.maze = maze
        print(x,y, self.rect.x, self.rect.y)
        
            
    def update(self, direction):
        # if self.maze.is_wall == 1:
        if direction == 'right': 
            self.rect.x += 55
        elif direction == 'left':
            self.rect.x -= 55
        elif direction == 'up':
            self.rect.y -= 55
        elif direction == 'down':
            self.rect.y += 55
        print(self.rect.x, self.rect.y)
    
    def diagonal(self, dx, dy):
        #control diagonal speed
        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2) / 2)
            dy = dy * (math.sqrt(2) / 2)
        self.rect.x += dx
        self.rect.y += dy
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def move(self, dx, dy):
        if self.maze.check_position(self.rect.x + dx, self.rect.y + dy):
            self.rect.x += dx
            self.rect.y += dy


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
            self.rect.y -= 30
            if self.rect.y <= 110 :  # If the ghost has reached the top of the screen
                self.direction = 'down'  # Change direction to down
        else:  # If direction is down
            self.rect.y += 30
            if self.rect.y >= 660:  # If the ghost has reached the bottom of the screen
                self.direction = 'up'  # Change direction to up


cell_size = screen_width // len(maze[0])

wall_image = pygame.image.load("assets/Grey_Brick.jpeg")
wall_image = pygame.transform.scale(wall_image, (cell_size, cell_size))
      
def draw_maze(maze):    
        for y, row in enumerate(maze):
            for x, cell in enumerate(row):
                if cell == 1:  # Wall
                    screen.blit(wall_image, (x * cell_size, y * cell_size, cell_size, cell_size))
                elif cell == 0:  # Path
                    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size))
                
   
            
exit = Door(1015, 689, my_maze)
player = Dog(my_maze.cell_size, my_maze.cell_size, my_maze)
ghosts = [
    Ghost(535, 550, my_maze),
    Ghost(200, 400, my_maze),
    Ghost(775, 320, my_maze)
]



#main game loop
run = True
while run:
    #frame right
    clock.tick(13)
    
    screen.fill("dark gray")
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
        exit.draw(screen)
        player.draw(screen)
        for ghost in ghosts:
            ghost.move()
            ghost.draw(screen)
        
            if player.rect.colliderect(ghost.rect):
                pause = True
                pause_start_time = pygame.time.get_ticks()

        if player.rect.colliderect(exit.rect):
            pause = True
            pause_start_time = pygame.time.get_ticks()

    else: 
        # If the game is paused, check if a second has passed
        if pygame.time.get_ticks() - pause_start_time >= 1000:
            run = False
        
        
        
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
            
pygame.quit()






# def main():
#     pygame.init()
#     #Create an instance on your controller object
#     #Call your mainloop
    
#     ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# # https://codefather.tech/blog/if-name-main-python/
# if __name__ == '__main__':
#     main()
