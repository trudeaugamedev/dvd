"""Fill the background, and hide the background of the image"""

import pygame
from pygame.locals import *

FPS = 60
WIDTH, HEIGHT = 600, 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DVD Screensaver")
clock = pygame.time.Clock()

# Convert the image, faster, so it's good practice to do so all the time
dvd = pygame.image.load("dvd.png").convert_alpha()

x = 0
y = 0
x_vel = 5
y_vel = 2

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    x += x_vel
    y += y_vel

    # Fill the screen with black so that the image doesn't just keep getting drawn on top of each other
    screen.fill((0, 0, 0))

    screen.blit(dvd, (x, y))

    pygame.display.update()

pygame.quit()
