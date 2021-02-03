# Trey Fischbach 02/3/2021
# This program is a different way of moving the spacecraft in the "Basic Spacecraft
# Movement" file. Here we use the mouse.

# We import pygame for use
import pygame

# Initialize pygame
pygame.init()

# Set with and height values in pixels
displayWidth = 500
displayHeight = 500

# We create a game display object. 
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))

# The game caption
pygame.display.set_caption("A Game")

# Create a clock to keep time in game, and control fps of game
clock = pygame.time.Clock()

# This imports the file that contains the spaceship png
# The object is assigned to the name "spaceship"
# The image you select can be anything you want, just be sure to match the file name with
# the string you put in the parameters
spaceship = pygame.image.load('spaceship.png')

# Some colors that are defined in RBG
black = (0, 0, 0)
red = (255,0,0)

# A class through which our object is drawn and modified
class Ship(object):


    # The initilization function, as of now only sets the x coordinates and y coordinates
    def __init__(self,x,y):
        
        # X position in pixels
        self.x = x

        # Y position in pixels
        self.y = y

        # The height in pixels of the spacecraft
        self.height = 70
        
        # The width in pixels of the spacecraft
        self.width = 95

        # "speed" is how much the x and y position change when the object is moving, in pixels
        self.speed = 5
        

    # This function draws the object using the position of the mouse
    def draw(self):
        
        # Gets the position of the user's mouse
        mouseCoordinates = pygame.mouse.get_pos()
        
        # Instead of drawing a rectangle, blits the spaceship image onto the board instead
        # Draws the spacecraft where the mouse is

        # Calculates where the spacecraft should be drawn given the mouse position
        xPos = mouseCoordinates[0]-(self.width/2)
        yPos = mouseCoordinates[1]-(self.height/2)
        gameDisplay.blit(spaceship,(xPos,yPos))



# This function ends the game
def endGame():
    pygame.quit()
    quit()

# This function draws everything in the game
def draw():
    # Fills the screen with a black background
    gameDisplay.fill(black)
    
    # Draws the bob object
    bob.draw()
    
    # Updates the screen once all the objects have been drawn
    pygame.display.update()

# Creates a rectangle object named bob that we can move around
bob = Ship(100,100)

# This is the main game loop which runs until the user quits the game
def game_loop():
    # This boolean variable keeps track of whether the game is running
    running = True

    # While the game is runnnig
    while running:

        # Get all the events (ie user inputs) that are currently happening
        for event in pygame.event.get():

            # If the user tries to close the game tap
            if event.type == pygame.QUIT:
                # The loop ends
                running = False
                # Calls the endGame function which terminates pygame and the program
                endGame()

        # This returns a list of all the keys on the keyboard.
        # The keys that are currently being pressed are set to True
        keys = pygame.key.get_pressed()
        

        # This sets the frames per second of the game
        # 30 fps
        clock.tick(30)

        # This calls the draw function which draws the entire game
        draw()
        
# This calls the game loop function which runs the game
# Notice that this is called last, once everything is defined
game_loop()
