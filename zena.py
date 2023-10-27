import pygame

# Initialize Pygame
pygame.init()

# Define the screen size
screen_width = 640
screen_height = 480

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the window title
pygame.display.set_caption("Zena")

# Define the sprite's movement speed
move_speed = 3
jump_speed = 8
gravity = 0.5

# Define the game loop
def game_loop():
    # Load the sprite images
    idle_images = [pygame.image.load("images/Idle/Warrior_Idle_1.png")]
    sprite_images = []
    for i in range(8):
        sprite_images.append(pygame.image.load(f"images/Run/Warrior_Run_{i}.png"))
    jump_images = []
    for i in range(6):
        jump_images.append(pygame.image.load(f"images/Jump/Warrior_Jump_{i % 3 + 1}.png"))

    # Scale the sprite images
    for i in range(len(idle_images)):
        idle_images[i] = pygame.transform.scale(idle_images[i], (idle_images[i].get_width() * 2, idle_images[i].get_height() * 2))
    for i in range(len(sprite_images)):
        sprite_images[i] = pygame.transform.scale(sprite_images[i], (sprite_images[i].get_width() * 2, sprite_images[i].get_height() * 2))
    for i in range(len(jump_images)):
        jump_images[i] = pygame.transform.scale(jump_images[i], (jump_images[i].get_width() * 2, jump_images[i].get_height() * 2))

    # Define the sprite's state and animation timer
    sprite_state = 0
    sprite_animation_timer = 0
    current_frame = 0

    # Define the sprite's position and velocity
    sprite_x = 0
    sprite_y = 300
    sprite_vel_x = 0
    sprite_vel_y = 0

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
                    sprite_state = 1
                elif event.key == pygame.K_RIGHT:
                    sprite_vel_x = move_speed
                    sprite_state = 1
                elif event.key == pygame.K_SPACE:
                    if sprite_vel_y == 0:
                        sprite_vel_y = -jump_speed
                        sprite_state = 2

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and sprite_vel_x < 0:
                    sprite_vel_x = 0
                    sprite_state = 0
                elif event.key == pygame.K_RIGHT and sprite_vel_x > 0:
                    sprite_vel_x = 0
                    sprite_state = 0

        # Update the sprite's position
        sprite_x += sprite_vel_x
        sprite_y += sprite_vel_y

        # Apply gravity to the sprite's velocity
        if sprite_vel_y != 0:
            sprite_vel_y += gravity

        # Set the sprite's state to idle if no keys are pressed
        if sprite_vel_x == 0 and sprite_vel_y == 0:
            sprite_state = 0

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
        elif sprite_state == 1:
            # Running animation
            sprite_animation_timer += 1
            if sprite_animation_timer >= animation_speed:
                sprite_animation_timer = 0
                current_frame += 1
                if current_frame >= len(sprite_images):
                    current_frame = 0
            sprite_image = sprite_images[current_frame]
        elif sprite_state == 2:
            # Jumping animation
            sprite_animation_timer += 1
            if sprite_animation_timer >= animation_speed:
                sprite_animation_timer = 0
                current_frame += 1
                if current_frame >= len(jump_images):
                    current_frame = len(jump_images) - 1
            sprite_image = jump_images[current_frame]

            # Check if the sprite has landed
            if sprite_y >= 300:
                sprite_y = 300
                sprite_vel_y = 0
                sprite_state = 0

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

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw the sprite
        screen.blit(sprite_image, (sprite_x, sprite_y))

        # Update the display
        pygame.display.update()

        # Tick the clock
        clock.tick(60)

    # Quit Pygame
    pygame.quit()

# Run the game loop
game_loop()