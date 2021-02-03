# Trey Fischbach 02/03/2021
# This program is a sequal to the basic spacecraft movement
# Utilizes text and movement bounds

# We import pygame for use
import pygame

# Initialize pygame
pygame.init()

# Set with and height values in pixels
displayWidth = 500
displayHeight = 500

# The number of crashes that have occured
crashNumber = 0

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
black = (0,0,0)
white = (255,255,255)
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
        self.width = 85

        # "speed" is how much the x and y position change when the object is moving, in pixels
        self.speed = 5

        # The number of crashes that have occurs
        self.crash_number = 0

    # This function draws the object
    def draw(self):
        # Instead of drawing a rectangle, blits the spaceship image onto the board instead
        gameDisplay.blit(spaceship,(self.x,self.y))

        # Prints out the ship's x and y position if needed
        #print(self.x,self.y)

    # This function handles all inputs from the user and checks if they can be executed
    def giveInput(self, keys):
        conditionA = self.x >= -10
        conditionB = self.x + self.width < displayWidth
        conditionC = self.y > 0
        conditionD = self.y + self.height < displayHeight


        # If the user hits the left key and
        # If the x posistion of the ship is greater than -10, (negative ten because the ship file
        # extends past the point where the ship is actually drawn) (If the left side of the ship
        # has not yet passed the leftmost boundary of the game.
        if keys[pygame.K_LEFT] and conditionA:
            self.x += -(self.speed)

        # If the user hits the right key and
        # If the left side (x+width) is not greater than the display width (If the right side
        # of the ship has not yet passed the rightmost boundary of the game.
        if keys[pygame.K_RIGHT] and conditionB:
            self.x += (self.speed)

        # If the user hits the up key and
        # If the y position the spacecraft is greater than zero (If the top of the ship
        # has not yet passed the top of the screen).
        if keys[pygame.K_UP] and conditionC:
            self.y += -(self.speed)

        # If the user hits the down key and
        # If the bottomost part of the ship (y+height) is not yet past the bottom of the screen. 
        if keys[pygame.K_DOWN] and conditionD:
            self.y += (self.speed)


        # This tests if the user has crashed or not.
        # If so, the crash function is called.
        if (not conditionA or not conditionB or not conditionC or not conditionD):
            self.crash()

    # In the event of a crash, the ship is reset to the middle of the screen
    def crash(self):
        self.x = displayWidth/2
        self.y = displayHeight/2
        self.crash_number += 1
          
    

# This function ends the game
def endGame():
    pygame.quit()
    quit()

# This function draws everything in the game
def draw():
    # Fills the screen with a black background
    gameDisplay.fill(black)

    # Crash number message as a string to be draw on the game display
    crash_num_message = "Total crashes: " + str(bob.crash_number)

    # Draws the crash number
    drawText(crash_num_message, 85, 15, white)
    
    # Draws the bob object
    bob.draw()
    
    # Updates the screen once all the objects have been drawn
    pygame.display.update()

# Draws the words on the game display
def drawText(text, centerX, centerY, color):
    numberText = pygame.font.Font('freesansbold.ttf', 20)
    TextSurf, TextRect = text_objects(text, numberText, color)
    TextRect.center = (centerX, centerY)
    gameDisplay.blit(TextSurf, TextRect)
    
# Helps with drawing the words
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


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
        
        # We give bob the player input so it can move itself if needed
        bob.giveInput(keys)

        # This sets the frames per second of the game
        # 30 fps
        clock.tick(30)

        # This calls the draw function which draws the entire game
        draw()
        
# This calls the game loop function which runs the game
# Notice that this is called last, once everything is defined
game_loop()
