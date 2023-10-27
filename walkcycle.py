import pygame

# Initialise Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))

# set clock
clock = pygame.time.Clock()

# Load the sprite images
sprite_images = []
for i in range(1, 9):
    sprite_images.append(pygame.image.load(f"images/Run/Warrior_Run_{i}.png"))

# Define the sprite's position
sprite_x = 200
sprite_y = 300

# Define the sprite's velocity
sprite_vel_x = 0
sprite_vel_y = 0

# Define the sprite's acceleration
sprite_acc_x = 0
sprite_acc_y = 0.5

# Define the sprite's jump velocity
jump_vel = -10

# Define the sprite's movement speed
move_speed = 5

# Define the current frame of the sprite animation
current_frame = 0

# Define the animation speed
animation_speed = 10

# Define the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                sprite_vel_x = -move_speed
            elif event.key == pygame.K_RIGHT:
                sprite_vel_x = move_speed
            elif event.key == pygame.K_SPACE:
                sprite_vel_y = jump_vel

    # Update the sprite's position and velocity
    sprite_x += sprite_vel_x
    sprite_y += sprite_vel_y
    sprite_vel_x += sprite_acc_x
    sprite_vel_y += sprite_acc_y

    # Clamp the sprite's position to the screen bounds
    if sprite_x < 0:
        sprite_x = 0
    elif sprite_x > screen.get_width() - sprite_images[0].get_width():
        sprite_x = screen.get_width() - sprite_images[0].get_width()
    if sprite_y < 0:
        sprite_y = 0
    elif sprite_y > screen.get_height() - sprite_images[0].get_height():
        sprite_y = screen.get_height() - sprite_images[0].get_height()
        sprite_vel_y = 0

    #fill the screen with black
    screen.fill((0,0,0))
    
    # Draw the sprite
    screen.blit(sprite_images[current_frame // animation_speed], (sprite_x, sprite_y))


    # Update the current frame of the sprite animation
    current_frame = (current_frame + 1) % (animation_speed * len(sprite_images))

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(60)


# Quit Pygame
pygame.quit()