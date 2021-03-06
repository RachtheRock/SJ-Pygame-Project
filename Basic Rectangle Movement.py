# Trey Fischbach 01/30/2021
# This program highlights the very basics of pygame. A rectange is drawn and can be moved around via the arrow keys.

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

# Some colors that are defined in RBG
black = (0, 0, 0)
red = (255,0,0)

# A class through which our object is drawn and modified
class Rectangle(object):

    # The initilization function, as of now only sets the x coordinates and y coordinates
    def __init__(self,x,y):
        
        # X position in pixels
        self.x = x

        # Y position in pixels
        self.y = y

        # "speed" is how much the x and y position change when the object is moving, in pixels
        self.speed = 5

    # This function draws the object
    def draw(self):
        # Right now the object is just a rectangle
        # Draws a rectange at the its coordinates with width 100 and 100 
        pygame.draw.rect(gameDisplay, red, (self.x, self.y, 100, 100))

    # This function handles all inputs from the user
    def giveInput(self, keys):

        # If the user hits the left key
        if keys[pygame.K_LEFT]:
            self.x += -(self.speed)

        # If the user hits the right key
        if keys[pygame.K_RIGHT]:
            self.x += (self.speed)

        # If the user hits the up key
        if keys[pygame.K_UP]:
            self.y += -(self.speed)

        # If the user hits the down key
        if keys[pygame.K_DOWN]:
            self.y += (self.speed)

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
    # Updates the screen
    pygame.display.update()

# Creates a rectangle object named bob that we can move around
bob = Rectangle(100,100)

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
        
        # We give bob the player input so it can move itself if needed
        bob.giveInput(keys)

        # This sets the frames per second of the game
        # 30 fps
        clock.tick(20)

        # This calls the draw function which draws the entire game
        draw()
        
# This calls the game loop function which runs the game
# Notice that this is called last, once everything is defined
game_loop()
