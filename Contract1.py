import random
import pygame
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()

image_path = []  # loads
for i in range(0, 15):
    image_path.append(str('Images/Room' + str(i) + '.png'))

roomImage = pygame.image.load(image_path[0])  # The first room image will
# always be the basic layout, after that it will be random
numberOfRoomImages = 5  # number of room images in the "Images" folder
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
          To display a new floor tile, press N.
          This also removed the overlay. Press Esc to exit.

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
        global roomImage  # This may not need to be global - please advise
        roomImage = pygame.image.load(image_path[random.randint
                                      (0, numberOfRoomImages - 1)]
                                      )
        screen.blit(roomImage, (0, 0))


running = True
while running:
    for event in pygame.event.get():
        if \
            event.type == QUIT \
            or \
                (event.type == KEYUP and event.key == K_ESCAPE):
            running = False
        elif event.type == KEYUP:  # if any key is pressed, launches function
            apply_overlay(event.key)                        # (inefficient)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
