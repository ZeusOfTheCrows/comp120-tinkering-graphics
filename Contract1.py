import pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()

imageToRecolour = pygame.image.load('Images/Image1.png')
colourToBeReplaced = pygame.Color(128, 0, 128)
newColours = {'Blood': (102, 0, 0), 'Mud': (144, 108, 63)}
screen = pygame.display.set_mode((imageToRecolour.get_width(), imageToRecolour.get_height()))
screen.fill((33, 33, 39))
pygame.display.set_caption('Contract #1 Demonstration')


def replace_colour(colour_to_be_replaced, replacement_colour, image):
    for x in range(0, image.get_width()):
        for y in range(0, image.get_height()):
            if image.get_at((x, y)) == colour_to_be_replaced:
                image.set_at((x, y), replacement_colour)
    return image


running = True
while running:  # Main game loop
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            running = False
        elif event.type == KEYUP and event.key == K_b:  # Press b for blood coloured splash
            replace_colour(colourToBeReplaced, newColours['Blood'], imageToRecolour)
        elif event.type == KEYUP and event.key == K_m:  # Press m for mud coloured splash
            replace_colour(colourToBeReplaced, newColours['Mud'], imageToRecolour)

    screen.blit(imageToRecolour, (0, 0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
