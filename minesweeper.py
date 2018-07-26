import pygame

"""
---------------------------- DEFINE CONSTANTS -----------------------------
"""
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the MARGIN between each cell
MARGIN = 2

# Sets Clock Speed
FPS = 60

"""
#--------------------------------------------------------------------------
"""

#--------------------------------------------------------------------------
# Function: main()
# Purpose: Initialize pygame & game window; Runs main game event loop
#--------------------------------------------------------------------------
def main():
    """
    SET UP THE GAME & WINDOW
    """
    pygame.init()
     
    # Set the width and height of the screen [width, height]
    size = (442, 442)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Minesweeper")


    # Create the 2D Grid Array
    grid = generateGridArray()


    """
    MAIN PROGRAM LOOP
    """
    # Loop until the user clicks the close button.
    done = False
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
     
    # -------- Main Program Loop -----------
    while not done:
        
        # --- Main event loop
        for event in pygame.event.get(): # Everytime user does something
            
            # If the user clicks close
            if event.type == pygame.QUIT:
                done = True

            # If the user clicks the mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get positional coordinates and convert
                row, column = getGridCoords()
                print(row, column)
                grid[row][column] = 1

        # --- Game logic should go here

        # --- Drawing code should go here
        draw(screen, grid)
     
        # --- Limit to 60 frames per second
        clock.tick(FPS)
     
    # Close the window and quit.
    pygame.quit()

#--------------------------------------------------------------------------
# Function: generateGridArray()
# Purpose: Generates a 2D array the size of the game board and assigns
#          the default value 0 to each cell
#--------------------------------------------------------------------------
def generateGridArray():
    grid = []

    # for each row, create a list that will represent an entire row
    for row in range(20):
        grid.append([])

        # Add the number zero to each cell in the current row
        for column in range(20):
            grid[row].append(0)

    return grid

#--------------------------------------------------------------------------
# Function: getGridCoords()
# Purpose: Gets the screen coordinates of a mouse click and converts it to
#          coordinates on the game grid
#--------------------------------------------------------------------------
def getGridCoords():
    pos = pygame.mouse.get_pos()

    column = pos[0] // (WIDTH + MARGIN)
    row = pos[1] // (HEIGHT + MARGIN)

    return row, column

#--------------------------------------------------------------------------
# Function: draw(screen, grid)
# Purpose: draws the game board
#--------------------------------------------------------------------------
def draw(screen, grid):
    # --- Screen-clearing code goes here
    # Don't put other drawing commands above this, or they will be erased
    screen.fill(BLACK)
    
    # Draw the game grid
    for row in range(20):
        for column in range(20):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                             color,
                             [MARGIN + (column * WIDTH) + (column * MARGIN),                # x
                                             MARGIN + (row * HEIGHT) + (row * MARGIN),      # y
                                             WIDTH,                                         # width
                                             HEIGHT])                                       # height
    
    # --- Update the screen with what we've drawn.
    pygame.display.flip()

"""
---------------------------------------------------------------------------
"""
main()
