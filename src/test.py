import pygame

pygame.init()
screen = pygame.display.set_mode((900, 700))

background1 = pygame.image.load("assets/dungeon.jpeg")
background1 = pygame.transform.scale(background1, (900, 700))

start_button = pygame.Rect(325, 560, 200, 50)
font = pygame.font.Font(None, 36)
text = font.render("Start", True, (0, 0, 0))

font2 = pygame.font.Font(None, 150)
text2 = font2.render("Escape", True, (255, 255, 255))

font3 = pygame.font.Font(None, 47)
text3 = font3.render("The Dungeon", True, (255, 255, 255))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        else:
            screen.blit(background1, (0, 0))
            pygame.draw.rect(screen, (115, 147, 179), start_button)
            screen.blit(text, (start_button.x + 66, start_button.y + 12))
            screen.blit(text2, (415, 220))
            screen.blit(text3, (430, 330))

        # Update the display
        pygame.display.flip()

pygame.quit()