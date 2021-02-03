# Trey Fischbach 02/03/2021
# This program shows how to draw various shapes and text in pygame.

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
pygame.display.set_caption("Shapes and Text")

# Create a clock to keep time in game, and control fps of game
clock = pygame.time.Clock()

# Some colors that are defined in RBG
black = (0, 0, 0)
red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
green = (0,255,0)


# This function ends the game
def endGame():
    pygame.quit()
    quit()

# This function draws all the shapes
def draw():
    # Fills the screen with a white background
    gameDisplay.fill(white)

    # Draws a rectangle:
    # (the game display, color, (x coordinate of top left, y coordinate of top left, width, height))
    pygame.draw.rect(gameDisplay, red, ((10,10,100,100)))

    # Draws a polygon:
    # (the game display, color, ((x coordinate of point1,y coordinate of point1),(x2,y2),(x3,y3) for as many points as desired)
    # Note, draws the shape in the order of the points that you give it
    pygame.draw.polygon(gameDisplay, blue, ((200,75),(200,175),(350,75),(300,25)))

    # Draws a line without specifying the width
    # (the game display, color, start position, end position, (optional width))
    pygame.draw.line(gameDisplay, black, (375,100), (475,125))

    # Draws a line with specifying the width
    pygame.draw.line(gameDisplay, black, (375,75), (475,100), 5)

    # Draws a circle (the game display, color, center, radius)
    pygame.draw.circle(gameDisplay, green, (150,200), 50)

    # Writes hello
    drawText("Hello", 250, 250, black)

    # Writes goodbye
    drawText("Goodbye", 100, 400, black)
                       
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


        # This sets the frames per second of the game
        # 30 fps
        clock.tick(30)

        # This calls the draw function which draws the entire game
        draw()
        
# This calls the game loop function which runs the game
# Notice that this is called last, once everything is defined
game_loop()
