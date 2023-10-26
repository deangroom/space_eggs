# Structuring your game code


This minimal script provides a solid foundation for building your game. You can expand upon it by adding more game logic, additional event handling, and further drawing elements. It follows best practices for organizing your game code and ensures that the game loop runs smoothly.


## These sections should be noted by using comments in the code to

- Import Required Modules: Import the necessary modules, such as pygame and sys, at the beginning of your script.

- Initialise Pygame: Use ```pygame.init()``` to initialise Pygame. This should be called at the start of your script.

- Define Constants: Define constants for the screen dimensions. This makes it easy to change the screen size later and keeps the code clean.

- Create the Game Window: Use pygame.```display.set_mode()``` to create the game window with the specified width and height. You can set a caption for the window using ```pygame.display.set_caption()```.

- The Game Loop: The core of any game is the game loop. It repeatedly checks for user input, updates the game logic, and renders the game.

- Event Handling: In the game loop, use a for loop to handle events. Check for the QUIT event to handle window closure. This allows the user to exit the game cleanly.

- Game Logic: The section for game logic, such as updating player positions, checking for collisions, and tracking scores, should go in the designated area. This is where your game-specific code resides.

- Clearing the Screen: Use ```screen.fill()``` to clear the screen with a specified color (in RGB format). This should be done at the beginning of each frame to prevent objects from leaving trails.

- Drawing Code: The section for drawing objects, characters, and other elements goes here. This is where you use Pygame functions to draw sprites, images, and text on the screen.

- Updating the Display: After drawing everything, call ```pygame.display.update()``` to update the display and show the changes on the screen.

- Exiting the Game: Once the game loop is done (e.g., when the player quits the game), make sure to clean up any resources and exit Pygame gracefully using ```pygame.quit()``` and ```sys.exit()```.

## Activity
1. Change the screen size to be 640 x 480
2. Find out why is 640 x 480 and 800 x 600 are 'standard size'
3. Change the screen file to 'white' using RGB values
4. Change the window caption to your name