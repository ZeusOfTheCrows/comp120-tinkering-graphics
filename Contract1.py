import pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((700, 533))
screen.fill((33, 33, 39))
pygame.display.set_caption('Contract #1 Demonstration')
image = pygame.image.load('Images/Image1.png')
colourToReplace = pygame.Color(255, 0, 135)


def replace_colour(colour_to_replace, new_colour):
    pygame.PixelArray.replace(colour_to_replace, new_colour)


'''
def replace_colour(colour_to_replace, new_colour):
    for x in range(700):
        for y in range(533):
            current_pixel_old = image.get_at((x, y))
            current_pixel_new = current_pixel_old
            # if current_pixel_old.r == colour_to_replace[0]:
            image.set_at((x, y), current_pixel_new)
            '''

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            running = False

    screen.blit(image, (0, 0))

    replace_colour(colourToReplace, pygame.Color(0, 0, 0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
