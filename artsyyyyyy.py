import pygame

pygame.init()

screen_width = 1100
screen_height = 850
screen = pygame.display.set_mode((screen_width, screen_height))

background2 = pygame.image.load("assets/bad_ending.jpeg")
background2 = pygame.transform.scale(background2, (1100, 900))

font4 = pygame.font.Font(None, 150)
text4 = font4.render("GAME OVER", True, (255, 255, 255))

font5 = pygame.font.Font(None, 40)
text5 = font5.render("Hopefully the next traveller fares better.", True, (255, 255, 255))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    else:
        screen.blit(background2, (0, 0))
        screen.blit(text4, (235, 480))
        screen.blit(text5, (290, 600))
        pygame.display.flip()