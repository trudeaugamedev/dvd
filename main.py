"""
Full code with comments.
Window with bouncing dvd
"""

import pygame                                       # Get pygame into the project
from random import randint                          # Grab the randint function from the random module
from pygame.locals import *                         # Get the pygame constants into the project

FPS = 60                                            # Set a variable storing the MAXIMUM FPS
WIDTH, HEIGHT = 600, 400                            # Set two variables storing the width and height of the window

pygame.init()                                       # Initialize pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))   # Create and store the screen, with the size of WIDTH and HEIGHT
pygame.display.set_caption("DVD Screensaver")       # Set window title
clock = pygame.time.Clock()                         # Create and store the clock

dvd = pygame.image.load("dvd.png").convert_alpha()  # Load and store the image, convert it for faster rendering

x = randint(0, WIDTH - dvd.get_width())             # Random x spawn position between 0 and the right side of the screen
y = randint(0, HEIGHT - dvd.get_height())           # Random y spawn position between 0 and the bottom of the screen
x_vel = randint(1, 6)                               # Random x velocity between 1 and 6 (inclusive)
y_vel = randint(1, 6)                               # Random y velocity between 1 and 6 (inclusive)
rect = dvd.get_rect()                               # Generate a rect from the image (same size as image)

running = True                                      # Create a variable that determins if the game is running or not
while running:                                      # Main game loop, everything during the game happens in here
    clock.tick(FPS)                                 # Tick the clock, make the game run at a MAXIMUM of 60 FPS

    for event in pygame.event.get():                # Loop through every event that is currently happening in pygame
        if event.type == QUIT:                      # If the event is the user clicking the window close button
            running = False                         # Set the running variable to False, which stops the main loop

    x += x_vel                                      # Add the x velocity to the position, moving the image
    y += y_vel                                      # Add the y velocity to the position, moving the image
    rect.x = x                                      # Set the x position of the rect to match the x variable
    rect.y = y                                      # Set the y position of the rect to match the y variable
    if rect.left < 0 or rect.right > WIDTH:         # If the left or right side of the rect is outside the window
        x_vel = -x_vel                              # Reverse the x velocity
    if rect.top < 0 or rect.bottom > HEIGHT:        # If the top or bottom side of the rect is outside the window
        y_vel = -y_vel                              # Reverse the y velocity

    screen.fill((0, 0, 0))                          # Fill the screen with black (0, 0, 0)
    screen.blit(dvd, (x, y))                        # Draw the image at position (x, y)

    pygame.display.update()                         # Update the window, so that everything is actually displayed

pygame.quit()                                       # Close the game when the main loop exits
