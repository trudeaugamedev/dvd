"""Adding randomness to the game"""

import pygame
from random import randint # Import the randint (generates a random integer between two numbers) function from the random module
from pygame.locals import *

FPS = 60
WIDTH, HEIGHT = 600, 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DVD Screensaver")
clock = pygame.time.Clock()

dvd = pygame.image.load("dvd.png").convert_alpha()

# Random spawn position
x = randint(0, WIDTH - dvd.get_width())
y = randint(0, HEIGHT - dvd.get_height())
# Random starting velocity from 1 to 6
x_vel = randint(1, 6)
y_vel = randint(1, 6)
rect = dvd.get_rect()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    x += x_vel
    y += y_vel
    rect.x = x
    rect.y = y
    if rect.left < 0 or rect.right > WIDTH:
        x_vel *= -1
    if rect.top < 0 or rect.bottom > HEIGHT:
        y_vel *= -1

    screen.fill((0, 0, 0))
    screen.blit(dvd, (x, y))

    pygame.display.update()

pygame.quit()
