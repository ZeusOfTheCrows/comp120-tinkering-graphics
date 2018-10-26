import random
import pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()

numberOfRoomImages = 5  # number of room images in the "Images" folder
image_path = []  # loads
for i in range(0, numberOfRoomImages):
    image_path.append(str('Images/Room' + str(i) + '.png'))
roomImage = pygame.image.load(image_path[0])  # The first room image will
# always be the basic layout, after that it will be random

overlays = [pygame.image.load('Images/WaterOverlay.png'),
            pygame.image.load('Images/AirOverlay.png'),
            pygame.image.load('Images/EarthOverlay.png'),
            pygame.image.load('Images/FireOverlay.png')
            ]
screen = pygame.display.set_mode((roomImage.get_width(),
                                  roomImage.get_height()
                                  ))
screen.fill((33, 33, 39))
pygame.display.set_caption('Contract #1 Demonstration')


screen.blit(roomImage, (0, 0))


def apply_overlay(key_pressed):
    """

          Applies an elemental overlay to the floor image

          Press W to display the water overlay,
          A for air, E for earth, and F for fire.
          To display a new floor tile with a random overlay, press N.
          To display a new floor tile with no overlay, press N.
          Press Esc to exit.

              """

    if key_pressed == K_w:
        screen.blit(overlays[0], (0, 0))
    elif key_pressed == K_a:
        screen.blit(overlays[1], (0, 0))
    elif key_pressed == K_e:
        screen.blit(overlays[2], (0, 0))
    elif key_pressed == K_f:
        screen.blit(overlays[3], (0, 0))
    elif key_pressed == K_n:
        room_image = pygame.image.load(image_path[random.randint
                                       (0, numberOfRoomImages - 1)]
                                       )
        screen.blit(room_image, (0, 0))
    elif key_pressed == K_r:
        room_image = pygame.image.load(image_path[random.randint
                                       (0, numberOfRoomImages - 1)]
                                       )
        screen.blit(room_image, (0, 0))
        screen.blit(overlays[random.randint(0, len(overlays)-1)], (0, 0))


running = True
while running:

    # for loop is only to check user inputs
    for event in pygame.event.get():
        if \
            event.type == QUIT \
            or \
                (event.type == KEYUP and event.key == K_ESCAPE):
            running = False
        elif event.type == KEYUP:
            # If any key is pressed, launches overlay function
            # Which key was pressed is handled by the function itself
            apply_overlay(event.key)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
