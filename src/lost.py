import pygame

pygame.init()
screen = pygame.display.set_mode((900, 700))

background2 = pygame.image.load("assets/other.jpeg")
background2 = pygame.transform.scale(background2, (800, 600))

font4 = pygame.font.Font(None, 36)
text4 = font4.render("GAME OVER", True, (255, 255, 255))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else: 
            screen.blit(background2, (0, 0))
            screen.blit(text4, (335, 500))
        pygame.display.flip()
            
pygame.quit()