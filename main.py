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
    pygame.draw.rect(mainScreen, (128, 128, 128), (300, 400, 500, 200))
    # tbh write the whole game in main first, then put it into classes
    # TODO for next time:
    # create the lava, make the player jump and crouch, create the spikes, creat the spike functionality
    # implement death functionality

    pygame.display.flip()
pygame.quit()