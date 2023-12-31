import pygame
import sys
import random
from pygame import mixer

shipx = 400 - 16
shipy = 400
pygame.init()
mixer.init()

# Set clock
clock = pygame.time.Clock()

# Set display
screen = pygame.display.set_mode((800, 600))

# Set sprites
playerShip = pygame.image.load("images/ship.png")
playerShip = pygame.transform.scale(playerShip, (32, 32))

enemy = pygame.image.load("images/enemy.png")
enemy = pygame.transform.scale(enemy, (32, 32))

bullet_img = pygame.image.load("images/bullet.png")
bullet_img = pygame.transform.scale(bullet_img, (16, 16))

# Set background
background = pygame.image.load("images/background.png")
background_size = background.get_size()
background_y = 0

# Play music in the background
mixer.music.load("sounds/music.mp3")
mixer.music.play(-1)

# Create a dictionary to track the state of keys
keys = {
    pygame.K_LEFT: False,
    pygame.K_RIGHT: False
}

# Create variables to control ship movement
ship_speed = 0.0
acceleration = 0.2
glide_time = 30  # Approximately 0.5 seconds (adjust as needed)

# Create variables to control bullets
bullets = []  # List to store bullets

# Create a bullet cooldown timer
bullet_cooldown = 0

# Create variables for enemies
enemies = []
enemy_speed = 3  # Adjust the speed of the enemies
enemy_spawn_delay = 120  # Adjust the delay between enemy spawns

# Create a function to spawn enemies
def spawn_enemy():
    enemy = pygame.image.load("images/enemy.png")
    enemy = pygame.transform.scale(enemy, (32, 32))
    enemyx = random.randint(0, 800 - 32)  # Randomly position the enemy along the x-axis
    enemies.append([enemyx, 0, enemy])

# Create a function to fire bullets
def fire(fx, fy):
    global bullet_cooldown
    if bullet_cooldown <= 0:
        bullet_sound = mixer.Sound("sounds/fire.mp3")
        bullet_sound.play()
        bullets.append([fx, fy])
        bullet_cooldown = 30  # Set the bullet cooldown (adjust as needed)

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

    # Apply acceleration to the ship
    if keys[pygame.K_LEFT]:
        ship_speed -= acceleration
    if keys[pygame.K_RIGHT]:
        ship_speed += acceleration

    # Apply deceleration after releasing keys
    if not keys[pygame.K_LEFT] and ship_speed < 0:
        ship_speed += acceleration
    if not keys[pygame.K_RIGHT] and ship_speed > 0:
        ship_speed -= acceleration

    # Ensure the ship doesn't move too fast
    ship_speed = min(max(ship_speed, -5.0), 5.0)

    # Update the ship's position
    shipx += int(ship_speed)

    # Update background position
    background_y += 1
    if background_y > background_size[1]:
        background_y = 0

    # Set background
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background_size[1]))

    # Update and draw bullets
    for bullet in bullets:
        screen.blit(bullet_img, (bullet[0], bullet[1]))
        bullet[1] -= 5  # Adjust the speed of the bullets

    # Remove bullets that have gone off the screen
    bullets = [bullet for bullet in bullets if bullet[1] > 0]

    # Update and draw enemies
    for enemy in enemies:
        screen.blit(enemy[2], (enemy[0], enemy[1]))
        enemy[1] += enemy_speed

    # Remove enemies that have gone off the screen
    enemies = [enemy for enemy in enemies if enemy[1] < 600]

    # Spawn new enemies at random intervals
    if enemy_spawn_delay <= 0:
        spawn_enemy()
        enemy_spawn_delay = 60  # Reset the spawn delay
    else:
        enemy_spawn_delay -= 1

    # Set the ship image on the screen
    screen.blit(playerShip, (shipx, shipy))

    # Update display
    pygame.display.update()

    # Set clock
    clock.tick(60)
