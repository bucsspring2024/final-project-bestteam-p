import pygame
from src.controller import Controller
from src.maze import Maze, maze


def main():
    pygame.init()
    #Create an instance on your controller object
    my_controller = Controller()
    #Call your mainloop
    my_controller.mainloop()
    
#     ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# # https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()