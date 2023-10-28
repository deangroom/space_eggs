import pygame
import random
import sys

'''
This script loads a background image and scrolls it across the screen.
It also loads a ground overlay image and scrolls it across the screen.
It also loads a platform image and scrolls it across the screen.

The ground and platform images are scaled to the screen width and height.
The platform is positioned at a random height between 0 and the screen height - 100.

The platform is blitted to the screen using the blit() method.
The blit() method takes two arguments: the image to blit and the position to blit it to.
The position is a tuple containing the x and y coordinates of the top left corner of the image.

'''

# Initialise pygame
pygame.init()

# Set the clock
clock = pygame.time.Clock()

# Set the screen size
screen_width = 640
screen_height = 180

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the caption
pygame.display.set_caption("Scrolling Background")

# Load the background image
bg = pygame.image.load("images/city.png")

# Load the ground overlay image
ground = pygame.image.load("images/ground.png")

# Load the platform image
platform = pygame.image.load("images/platform.png")

#scale the platform image to 50 pixels wide and 10 pixels high
'''this is a great way of setting the size of things in pygame'''
platform = pygame.transform.scale(platform, (50, 10))


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

# Define the platform position
platform_x = screen_width
#set the height of the platform to a random number between 0 and the screen height-100
platform_y = random.randint(10, screen_height-100)

# Define the platform speed
platform_speed = 1

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

    # Update the platform position
    platform_x -= platform_speed

    # If the ground has scrolled off the screen, reset its position
    if ground_x <= -screen_width:
        ground_x = 0

    # If the platform has scrolled off the screen, reset its position
    if platform_x <= -platform.get_width():
        platform_x = screen_width

    # Blit the background onto the screen
    screen.blit(bg, (bg_x, 0))

    # Blit the ground overlay onto the screen
    screen.blit(ground, (ground_x, screen_height - ground.get_height()))
   
    # Blit the platform onto the screen
    screen.blit(platform, (platform_x, platform_y))
    print(platform_x, platform_y)
    
    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(30)

# Quit Pygame
pygame.quit()