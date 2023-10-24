import pygame
import sys
from pygame import mixer

shipx = 400 - 16
shipy = 400
enemyx = 400 - 16
maxammo = 20
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

enemy = pygame.image.load("images/enemy.png")
enemy = pygame.transform.scale(enemy, (32, 32))

bullet_img = pygame.image.load("images/bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (16, 16))

# Create a dictionary to track the state of keys
keys = {
    pygame.K_z: False,
    pygame.K_x: False
}

# Create variables to control ship movement
ship_speed = 10

# Create variables to control bullets
bullets = []  # List to store bullets

# Create a bullet cooldown timer
bullet_cooldown = 0

# Create a function to fire bullets
def fire(fx, fy):
    global bullet_cooldown
    if bullet_cooldown <= 0:
        bullet_sound = mixer.Sound("sounds/fire.mp3")
        bullet_sound.play()
        bullets.append([(fx+12), fy]) #offset for bullet's position as a graphic
        bullet_cooldown = 20  # Set the bullet cooldown (adjust as needed)

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

        # Check for space key press to fire bullets
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            fire(shipx, shipy)

    # Update the bullet cooldown timer
    if bullet_cooldown > 0:
        bullet_cooldown -= 1

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

    # Update and draw bullets
    for bullet in bullets:
        screen.blit(bullet_img, (bullet[0], bullet[1]))
        bullet[1] -= 5  # Adjust the speed of the bullets

    # Remove bullets that have gone off the screen
    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    # Update display
    pygame.display.update()

    # Set clock
    clock.tick(120)
