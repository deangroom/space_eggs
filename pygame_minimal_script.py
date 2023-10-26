import pygame
import sys

# Initialise Pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic goes here

    # Drawing and rendering
    screen.fill((0, 0, 0))  # Clear the screen with a black background

    # Drawing code goes here

    pygame.display.update()  # Update the display

# Clean up and quit Pygame
pygame.quit()
sys.exit()
