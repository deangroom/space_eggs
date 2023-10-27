import pygame
import sys

'''

'''

# Initialise pygame
pygame.init()

#set clock 
clock = pygame.time.Clock()

#get size of background image
bg = pygame.image.load("images/castle_8bit.png")
bg_size = bg.get_size()
bg_width = bg_size[0]
bg_height = bg_size[1]

#set screensize to background image size
screen = pygame.display.set_mode((bg_width, bg_height))


#set caption
pygame.display.set_caption("Zena")

#create idle animation
idle = []
for i in range(1, 7):
    filename = f"images/idle/Warrior_Idle_{i}.png"
    try:
        img = pygame.image.load(filename)
        #scale image
        img = pygame.transform.scale(img, (int(img.get_width() * 2), int(img.get_height() * 2)))
        idle.append(img)
        print(f"Loaded image {filename}")
    except pygame.error:
        print(f"Could not load image {filename}")


#set animation loop speed
animation_speed = 0.15

#main loop
current_frame = 0
while True:

    #draw background
    screen.blit(bg, (0, 0))

    #draw idle animation using animation speed
    current_frame += animation_speed
    if current_frame >= len(idle):
        current_frame = 0
    screen.blit(idle[int(current_frame)], (100, 95))


    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #set framerate
    clock.tick(60)
    
    #update display
    pygame.display.update()