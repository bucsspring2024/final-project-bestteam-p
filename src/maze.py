import pygame

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
