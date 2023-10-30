# space_eggs
This is a set of building tutorials for a classic arcader space shooter
Each script adds to the last, it's a work in progress



## Base
This is a basic Pygame program that displays a scrolling background and a player ship sprite. The program starts by importing the necessary modules, initializing Pygame and the Pygame mixer module for playing music. It then sets the clock and display, and loads the background and player ship images.

The main game loop is a while loop that runs indefinitely until the user quits the program. Within the loop, the program handles events, updates the background position, blits the background and player ship onto the screen, and updates the display. The clock is used to limit the frame rate to 60 frames per second.

The background is scrolled vertically by updating the background_y variable, which controls the position of the background image. If the background goes out of the screen, its position is reset to 0. The background is then blitted onto the screen twice, once at its current position and once at its position minus its height, to create a seamless scrolling effect.

The player ship sprite is positioned in the middle of the screen by setting its shipx and shipy variables. The sprite is then blitted onto the screen at its position.

Finally, the display is updated to show the changes made in the loop. The clock is ticked to limit the frame rate to 60 frames per second.

Overall, this code provides a good starting point for a Pygame game with a scrolling background and a player sprite. However, it is a very basic program and lacks user input handling, collision detection, and other features that would make it a complete game.
