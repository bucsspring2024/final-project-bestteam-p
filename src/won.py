import pygame

pygame.init()
screen = pygame.display.set_mode((900, 700))

background2 = pygame.image.load("assets/death.jpeg")
background2 = pygame.transform.scale(background2, (800, 600))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else: 
            screen.blit(background2, (0, 0))