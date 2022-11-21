"""Base Code"""

import pygame
from pygame.locals import *

FPS = 60
WIDTH, HEIGHT = 600, 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DVD Screensaver")
# Create a clock
clock = pygame.time.Clock()

running = True
while running:
    # Make sure the game runs at at most 60 FPS, discuss reason why
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.update()

pygame.quit()
