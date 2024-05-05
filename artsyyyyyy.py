import pygame

pygame.init()

screen_width = 1100
screen_height = 850
screen = pygame.display.set_mode((screen_width, screen_height))

background4 = pygame.image.load("assets/woods.jpg")
background4 = pygame.transform.scale(background4, (1100, 900))

font8 = pygame.font.Font(None, 150)
text8 = font8.render("You Escaped", True, (255, 255, 255))

font9 = pygame.font.Font(None, 40)
text9 = font9.render("Somehow, you lived to see another day", True, (255, 255, 255))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    else:
        screen.blit(background4, (0, 0))
        screen.blit(text8, (235, 390))
        screen.blit(text9, (290, 515))
        pygame.display.flip()