"""Load and draw/blit the first image"""

import pygame
from pygame.locals import *

FPS = 60
WIDTH, HEIGHT = 600, 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DVD Screensaver")
clock = pygame.time.Clock()

# Load in the image, and name it face
dvd = pygame.image.load("dvd.png")

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Draw the face at coordinates (0, 0), explain pygame coordinate system, encourage changing the coordinates
    screen.blit(dvd, (0, 0))

    pygame.display.update()

pygame.quit()
