import pygame
import sys
from pygame import mixer

shipx = 400 - 16
shipy = 400
pygame.init()
mixer.init()

# Set clock
clock = pygame.time.Clock()

# Set display
screen = pygame.display.set_mode((800, 600))

# Set background
background = pygame.image.load("images/background.png")
background_size = background.get_size()
background_y = 0

# Play music in the background
mixer.music.load("sounds/music.mp3")
mixer.music.play(-1)

# Set sprites
playerShip = pygame.image.load("images/ship.png")
playerShip = pygame.transform.scale(playerShip, (32, 32))

# Create variables to control ship movement
ship_speed = 5

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for key presses (Z and X keys)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                shipx -= ship_speed
            elif event.key == pygame.K_x:
                shipx += ship_speed

    # Update background position
    background_y += 1
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
