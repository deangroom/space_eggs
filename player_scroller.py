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
pygame.display.set_caption("Player Scroller")

# Set the player position
player_x = screen_width/2
player_y = screen_height/2

# Load the idle animation frames for the player
player_idle = []
for i in range(1, 7):
    image = pygame.image.load("images/idle/Warrior_Idle_" + str(i) + ".png")
    scaled_image = pygame.transform.scale(image, (100, 100))
    player_idle.append(scaled_image)

# Load the running animation frames for the player
player_run = []
for i in range(1, 7):
    image = pygame.image.load("images/run/Warrior_Run_" + str(i) + ".png")
    scaled_image = pygame.transform.scale(image, (100, 100))
    player_run.append(scaled_image)

# Set the initial player animation frame
player_frame = 0

# Load the background image
bg = pygame.image.load("images/city.png")

# Get the size of the background image
bg_size = bg.get_size()
bg_width = bg_size[0]
bg_height = bg_size[1]

# Define the background position
bg_x = 0

# Define the background speed
bg_speed = 2

# Define a flag to indicate if the player has moved to start the game
game_started = False

# Define the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bg_x += bg_speed
        if bg_x > 0:
            bg_x = 0
        game_started = True
        player_frame += 1
        if player_frame >= len(player_run):
            player_frame = 0
    elif keys[pygame.K_RIGHT]:
        bg_x -= bg_speed
        if bg_x <= -bg_width + screen_width:
            bg_x = -bg_width + screen_width
        game_started = True
        player_frame += 1
        if player_frame >= len(player_run):
            player_frame = 0
    else:
        game_started = False
        player_frame += 1
        if player_frame >= len(player_idle):
            player_frame = 0

    # Blit the background onto the screen
    screen.blit(bg, (bg_x, 0))

    # Blit the player onto the screen
    if game_started:
        screen.blit(player_run[player_frame], (player_x, player_y))
    else:
        screen.blit(player_idle[player_frame], (player_x, player_y))

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(30)

# Quit Pygame
pygame.quit()