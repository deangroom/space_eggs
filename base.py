import pygame
import sys
from pygame import mixer

shipx = 400-16
#place the ship in the middle of the screen which is literal and should be calculated
shipy = 400
# Initialize pygame
pygame.init()
mixer.init()


# Set clock
clock = pygame.time.Clock()

# Set display
screen = pygame.display.set_mode((800, 600))

# Set background
background = pygame.image.load("images/background.png")
background_size = background.get_size()
background_y = 0  # Initialize the position of the background

# Play music in the background
mixer.music.load("sounds/music.mp3")
mixer.music.play(-1)  # Play the loaded music indefinitely

# Set sprites
playerShip = pygame.image.load("images/ship.png")
playerShip = pygame.transform.scale(playerShip, (32, 32))

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update background position
    background_y += 1  # Adjust this value to control the speed of scrolling

    # If the background goes out of screen, reset its position
    if background_y > background_size[1]:
        background_y = 0

    # Set background
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background_size[1]))

    # Set sprites
    screen.blit(playerShip, (shipx, shipy))

    # Update display
    pygame.display.update()

    # Set clock
    clock.tick(60)