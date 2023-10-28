import pygame
import sys

# Initialise pygame
pygame.init()

# Set the clock
clock = pygame.time.Clock()

# Set the screen size
screen_width = 320
screen_height = 180

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption
pygame.display.set_caption("Scrolling Background")

# Load the background image
bg = pygame.image.load("images/city.png")

# Load the ground overlay image
ground = pygame.image.load("images/ground.png")

# Get the size of the background image
bg_size = bg.get_size()
bg_width = bg_size[0]
bg_height = bg_size[1]

# Define the background position
bg_x = 0

# Define the ground position
ground_x = 0

# Define the ground speed
ground_speed = 0.5

# Define the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the background position
    bg_x -= 0.5

    # Update the ground position
    ground_x -= ground_speed

    # If the ground has scrolled off the screen, reset its position
    if ground_x <= -screen_width:
        ground_x = 0

    # Blit the background onto the screen
    screen.blit(bg, (bg_x, 0))

    # Blit the ground overlay onto the screen
    screen.blit(ground, (ground_x, screen_height - ground.get_height()))

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(30)

# Quit Pygame
pygame.quit()