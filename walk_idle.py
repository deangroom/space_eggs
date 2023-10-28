import pygame

# Initialise Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((400, 300))

# set clock
clock = pygame.time.Clock()

# Load the sprite image
sprite_images = []
for i in range(1, 9):
    sprite_images.append(pygame.image.load(f"images/Run/Warrior_Run_{i}.png"))
    #scale the sprite image
    sprite_images[i - 1] = pygame.transform.scale(sprite_images[i - 1], (sprite_images[i - 1].get_width() * 2, sprite_images[i - 1].get_height() * 2))

# Load the idle sprite image
idle_images = []
for i in range(1, 7):
    idle_images.append(pygame.image.load(f"images/Idle/Warrior_Idle_{i}.png"))
    # Scale the idle sprite image
    idle_images[i - 1] = pygame.transform.scale(idle_images[i - 1], (idle_images[i - 1].get_width() * 2, idle_images[i - 1].get_height() * 2))


# Define the sprite's position
sprite_x = 200
sprite_y = 300

# Define the sprite's velocity
sprite_vel_x = 0
sprite_vel_y = 0

# Define the sprite's movement speed
move_speed = 1

# Define the current frame of the sprite animation
current_frame = 0

# Define the animation speed
animation_speed = 10

# Define the sprite state (0 for idle) and animation timer
sprite_state = 0
sprite_animation_timer = 0

# Define the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Update the sprite's animation
    if sprite_state == 0:
        # Idle animation
        sprite_animation_timer += 1
        if sprite_animation_timer >= animation_speed:
            sprite_animation_timer = 0
            current_frame += 1
            if current_frame >= len(idle_images):
                current_frame = 0
        sprite_image = idle_images[current_frame]

    # Draw the sprite
    screen.blit(sprite_image, (sprite_x, sprite_y))

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

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(60)