import pygame

pygame.init()
screen = pygame.display.set_mode((900, 700))

background2 = pygame.image.load("assets/bad_ending.jpeg")
background2 = pygame.transform.scale(background2, (900, 700))

font4 = pygame.font.Font(None, 100)
text4 = font4.render("GAME OVER", True, (255, 255, 255))

font5 = pygame.font.Font(None, 30)
text5 = font5.render("Hopefully the next traveller fares better.", True, (255, 255, 255))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else: 
            screen.blit(background2, (0, 0))
            screen.blit(text4, (248, 480))
            screen.blit(text5, (265, 555))
        pygame.display.flip()
            
pygame.quit()