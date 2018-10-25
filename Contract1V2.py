import random
import pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()

image_path = []
for i in range(0, 15):
    image_path.append(str('Images/Floor' + str(i) + '.png'))

floorImage = pygame.image.load(image_path[0])
overlays = [pygame.image.load('Images/WaterOverlay.png'), pygame.image.load('Images/AirOverlay.png'),
            pygame.image.load('Images/EarthOverlay.png'), pygame.image.load('Images/FireOverlay.png')]
screen = pygame.display.set_mode((floorImage.get_width(), floorImage.get_height()))
screen.fill((33, 33, 39))
pygame.display.set_caption('Contract #1 Demonstration')


def replace_colour(colour_to_be_replaced, replacement_colour, image):
    for x in range(0, image.get_width()):
        for y in range(0, image.get_height()):
            if image.get_at((x, y)) == colour_to_be_replaced:
                image.set_at((x, y), replacement_colour)
    return image


screen.blit(floorImage, (0, 0))

running = True
while running:  # Main game loop

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            running = False
        elif event.type == KEYUP and event.key == K_w:  # Press w for water aligned room
            screen.blit(overlays[0], (0, 0))
        elif event.type == KEYUP and event.key == K_a:  # Press a for air aligned room
            screen.blit(overlays[1], (0, 0))
        elif event.type == KEYUP and event.key == K_e:  # Press e for earth aligned room
            screen.blit(overlays[2], (0, 0))
        elif event.type == KEYUP and event.key == K_f:  # Press f for fire aligned room
            screen.blit(overlays[3], (0, 0))
        elif event.type == KEYUP and event.key == K_n:  # Press n for new room
            floorImage = pygame.image.load(image_path[random.randint(0, 4)])
            # floorImage = pygame.image.load(image_path[0])
            screen.blit(floorImage, (0, 0))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
