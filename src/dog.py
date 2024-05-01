import pygame
from src.maze import Maze
screen_width = 1100
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

cell_size = cell_size = screen_width // len(maze[0])

Maze = Maze(maze)

class Dog:
    def __init__(self, x, y, maze):
        self.image = pygame.image.load("assets/dog.png") 
        self.image = pygame.transform.scale(self.image, (120, 120))  # Resize the image to 40x40 pixels
        self.rect = self.image.get_rect() 
        self.rect.center = (x, y)
        self.maze = maze
    
    def check_position(self, x, y):
        valid_turns = []

        # Convert the player's position to maze coordinates
        maze_x, maze_y = x // cell_size, y // cell_size
        
        if self.maze.is_move_valid(maze_x, maze_y, 'up'):
            valid_turns.append('up')
        if self.maze.is_move_valid(maze_x, maze_y, 'down'):
            valid_turns.append('down')
        if self.maze.is_move_valid(maze_x, maze_y, 'left'):
            valid_turns.append('left')
        if self.maze.is_move_valid(maze_x, maze_y, 'right'):
            valid_turns.append('right')

        # # Check the cells around the player's position
        # if maze[maze_y-1][maze_x] == 0:  # Check the cell above
        #     valid_turns.append('up')
        # if maze[maze_y+1][maze_x] == 0:  # Check the cell below
        #     valid_turns.append('down')
        # if maze[maze_y][maze_x-1] == 0:  # Check the cell to the left
        #     valid_turns.append('left')
        # if maze[maze_y][maze_x+1] == 0:  # Check the cell to the right
        #     valid_turns.append('right')

        return valid_turns  
    
    
    def move(self, dx, dy):
         # Calculate the new position
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy

        # Get the valid moves from the current position
        valid_turns = check_position(self.rect.x, self.rect.y)

        # Only apply the move if it's valid
        if dx > 0 and 'right' in valid_turns:
            self.rect.x = new_x
        elif dx < 0 and 'left' in valid_turns:
            self.rect.x = new_x
        if dy > 0 and 'down' in valid_turns:
            self.rect.y = new_y
        elif dy < 0 and 'up' in valid_turns:
            self.rect.y = new_y

        # #control diagonal speed
        # if dx != 0 and dy != 0:
        #     dx = dx * (math.sqrt(2) / 2)
        #     dy = dy * (math.sqrt(2) / 2)
        # self.rect.x += dx
        # self.rect.y += dy
        
    def draw(self, surface):
        surface.blit(self.image, self.rect)  # Draw the image onto the surface