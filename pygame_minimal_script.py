import pygame
import sys

# Initialise Pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

clock=pygame.time.Clock()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

# Game loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
          

  # Game logic goes here

  # Drawing and rendering
  screen.fill((0, 0, 0))  # Clear the screen with a black background

  # Drawing code goes here

  pygame.display.update()  # Update the display

  # Set Clock Tick
  clock.tick(60)
