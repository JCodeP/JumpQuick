import pygame
import player


pygame.init()

mainScreen = pygame.display.set_mode((800, 600))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    mainScreen.fill((255, 255, 255))

    pygame.display.flip()
pygame.quit()