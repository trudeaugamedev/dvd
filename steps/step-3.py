"""Move the image"""

import pygame
from pygame.locals import *

FPS = 60
WIDTH, HEIGHT = 600, 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DVD Screensaver")
clock = pygame.time.Clock()

dvd = pygame.image.load("dvd.png")

x = 0 # Declare a variable storing the x position
y = 0 # Declare a variable storing the y position
x_vel = 5 # Declare a variable storing the x speed/velocity (velocity -> vel)
y_vel = 2 # Declare a variable storing the y speed/velocity

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    x += x_vel # Move the x position by the x velocity every frame
    y += y_vel # Move the y position by the y velocity every frame

    # No screen.fill to show why screen.fill is necessary
    screen.blit(dvd, (x, y))

    pygame.display.update()

pygame.quit()
