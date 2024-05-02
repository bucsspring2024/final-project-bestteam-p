import pygame

pygame.init()
screen = pygame.display.set_mode((900, 700))

background3 = pygame.image.load("assets/bad_ending.jpeg")
background3 = pygame.transform.scale(background3, (900, 700))

font6 = pygame.font.Font(None, 100)
text6 = font6.render("You Escaped", True, (255, 255, 255))

font7 = pygame.font.Font(None, 30)
text7 = font7.render("Somehow, you lived to see another day", True, (255, 255, 255))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else: 
            screen.blit(background3, (0, 0))
            screen.blit(text6, (235, 500))
            screen.blit(text7, (263, 585))
        pygame.display.flip()
            
pygame.quit()