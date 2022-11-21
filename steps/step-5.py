"""Edge collision with rects"""

import pygame
from pygame.locals import *

FPS = 60
WIDTH, HEIGHT = 600, 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DVD Screensaver")
clock = pygame.time.Clock()

dvd = pygame.image.load("dvd.png").convert_alpha()

x = 0
y = 0
x_vel = 5
y_vel = 2
# Generate a rect from the image (same size as image)
rect = dvd.get_rect()

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    x += x_vel
    y += y_vel
    rect.x = x # Update the x position of the rect to match the x variable
    rect.y = y # Update the y position of the rect to match the y variable
    # If the left of the rect is crossing the left border of the window
    # or if the right of the rect is crossing the right border of the window
    if rect.left < 0 or rect.right > WIDTH:
        x_vel = -x_vel # Reverse the x velocity
    # If the top of the rect is crossing the top border of the window
    # or if the bottom of the rect is crossing the bottom border of the window
    if rect.top < 0 or rect.bottom > HEIGHT:
        y_vel = -y_vel # Reverse the y velocity

    screen.fill((0, 0, 0))
    screen.blit(dvd, (x, y))

    pygame.display.update()

pygame.quit()
