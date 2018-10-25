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
numberOfRoomImages = 5
overlays = [pygame.image.load('Images/WaterOverlay.png'),
            pygame.image.load('Images/AirOverlay.png'),
            pygame.image.load('Images/EarthOverlay.png'),
            pygame.image.load('Images/FireOverlay.png')
            ]
screen = pygame.display.set_mode((roomImage.get_width(),
                                  roomImage.get_height()))
screen.fill((33, 33, 39))
pygame.display.set_caption('Contract #1 Demonstration')


screen.blit(roomImage, (0, 0))


def main_game_loop():
    """

          Main game loop

          Press W to display the water overlay,
          A for air, E for earth, and F for fire.
          To remove the overlay , press N. This also displays
          a new floor tile. Press Esc to exit.

              """

    running = True
    while running:

        for event in pygame.event.get():
            if \
                    event.type == QUIT \
                    or \
                    (event.type == KEYUP and event.key == K_ESCAPE):
                        running = False
            elif event.type == KEYUP and event.key == K_w:
                screen.blit(overlays[0], (0, 0))
            elif event.type == KEYUP and event.key == K_a:
                screen.blit(overlays[1], (0, 0))
            elif event.type == KEYUP and event.key == K_e:
                screen.blit(overlays[2], (0, 0))
            elif event.type == KEYUP and event.key == K_f:
                screen.blit(overlays[3], (0, 0))
            elif event.type == KEYUP and event.key == K_n:
                global roomImage
                roomImage = pygame.image.load(image_path[random.randint
                                            (0, numberOfRoomImages - 1)]
                                            )
                screen.blit(roomImage, (0, 0))

        pygame.display.update()
        clock.tick(60)


main_game_loop()

pygame.quit()
