import pygame
import sys
from pygame import mixer

shipx = 400 - 16
shipy = 400
enemyx = 400 - 16
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

# Create a dictionary to track the state of keys
keys = {
    pygame.K_z: False,
    pygame.K_x: False
}

# Create variables to control ship movement
ship_speed = 5


# create an enemy
enemy = pygame.image.load("images/enemy.png")
enemy = pygame.transform.scale(enemy, (32, 32))
enemyx = 400 - 16


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key in keys:
                keys[event.key] = True

        # Check for key releases
        if event.type == pygame.KEYUP:
            if event.key in keys:
                keys[event.key] = False

    # Check the state of keys and move the ship accordingly
    if keys[pygame.K_z]:
        shipx -= ship_speed
    if keys[pygame.K_x]:
        shipx += ship_speed

    # Update background position
    background_y += 1
    if background_y > background_size[1]:
        background_y = 0

    # Set background
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background_size[1]))

    # Set sprites
    screen.blit(enemy, (enemyx, 40))
    screen.blit(playerShip, (shipx, shipy))

    # Update display
    pygame.display.update()

    # Set clock
    clock.tick(60)
