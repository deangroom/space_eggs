import pygame
import sys

# Initialise
pygame.init()

# clock
clock = pygame.time.Clock()

ex=400
ey=400

# display
screen = pygame.display.set_mode((800, 600))

# explosion animation 
explosion_images = []
for i in range(1, 6):
    explosion_images.append(pygame.image.load(f"images/sprite_{i}.png"))

# play the explosion animation
def play_explosion_animation(ex, ey):
   
    for explosion_frame in explosion_images:
        screen.blit(explosion_frame, (ex, ey))
       
        pygame.display.update()
        pygame.time.delay(500)  # Adjust the delay to control the animation speed

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    play_explosion_animation(ex, ey)
            
    # update display
    pygame.display.update()
    
    # set clock
    clock.tick(60)
