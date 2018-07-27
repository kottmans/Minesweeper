import pygame
from random import randint

"""
---------------------------- DEFINE CONSTANTS -----------------------------
"""
# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# This sets the GRID_WIDTH and GRID_HEIGHT of the grid (i.e. # of cells)
GRID_WIDTH = 20
GRID_HEIGHT = 20

# This sets the MARGIN between each cell
MARGIN = 2

# This sets the WIDTH and HEIGHT of each grid cell
CELL_WIDTH = 30
CELL_HEIGHT = 30

SCREEN_SIZE_X = (MARGIN * GRID_WIDTH+1) + (CELL_WIDTH * GRID_WIDTH)
SCREEN_SIZE_Y = (MARGIN * GRID_HEIGHT+1) + (CELL_HEIGHT * GRID_HEIGHT)
SCREEN_SIZE = (SCREEN_SIZE_X, SCREEN_SIZE_Y)

# Sets Clock Speed
FPS = 60

# Sets the total number of mines placed on the grid
TOTAL_MINES = 60

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
    screen = pygame.display.set_mode(SCREEN_SIZE)

    pygame.display.set_caption("Minesweeper")


    # Create the 2D Grid Arrays
    grid = generateGridArray()          # Keeps track of logical value of cells
    visibleGrid = generateGridArray()   # Keeps track if cell is visible by user
    setMines(grid)
    setNumbers(grid)


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

                # If the cell clicked is currently "unvisited"
                if visibleGrid[row][column] == 0:
                    visibleGrid[row][column] = 1 # reveal clicked tile
                    
                    # if the cell is also blank
                    if isBlank(grid, row, column):
                        revealTiles(grid, visibleGrid, row, column)


        draw(screen, grid, visibleGrid)
        clock.tick(FPS)
     
    # Close the window and quit
    pygame.quit()

#--------------------------------------------------------------------------
# Function: generateGridArray()
# Purpose: Generates a 2D array the size of the game board and assigns
#          a default value 0 to each cell
#--------------------------------------------------------------------------
def generateGridArray():
    grid = []

    # for each row, create a list that will represent an entire row
    for row in range(GRID_HEIGHT):
        grid.append([])

        # Add the number zero to each cell in the current row
        for column in range(GRID_WIDTH):
            grid[row].append(0)

    return grid

#--------------------------------------------------------------------------
# Function: getGridCoords()
# Purpose: Gets the screen coordinates of a mouse click and converts it to
#          coordinates on the game grid
#--------------------------------------------------------------------------
def getGridCoords():
    pos = pygame.mouse.get_pos()

    column = pos[0] // (CELL_WIDTH + MARGIN)
    row = pos[1] // (CELL_HEIGHT + MARGIN)

    return row, column

#--------------------------------------------------------------------------
# Function: draw(screen, grid)
# Purpose: draws the game board
#--------------------------------------------------------------------------
def draw(screen, grid, visibleGrid):
    # --- Screen-clearing code goes here
    # Don't put other drawing commands above this, or they will be erased
    screen.fill(BLACK)
    
    # Draw the game grid
    for row in range(GRID_HEIGHT):
        for column in range(GRID_WIDTH):
            color = WHITE
            if visibleGrid[row][column] == 0:
                img = pygame.image.load("tiles/unvisited.png")
            elif visibleGrid[row][column] == 1:
                if grid[row][column] == "Mine":
                    img = pygame.image.load("tiles/mine.png")
                elif grid[row][column] == 0:
                    img = pygame.image.load("tiles/visited.png")
                elif grid[row][column] == 1:
                    img = pygame.image.load("tiles/1.png")
                elif grid[row][column] == 2:
                    img = pygame.image.load("tiles/2.png")
                elif grid[row][column] == 3:
                    img = pygame.image.load("tiles/3.png")
                elif grid[row][column] == 4:
                    img = pygame.image.load("tiles/4.png")
                elif grid[row][column] == 5:
                    img = pygame.image.load("tiles/5.png")
                elif grid[row][column] == 6:
                    img = pygame.image.load("tiles/6.png")
                elif grid[row][column] == 7:
                    img = pygame.image.load("tiles/7.png")
                elif grid[row][column] == 8:
                    img = pygame.image.load("tiles/8.png")
            else:
                img = pygame.image.load("tiles/flag.png")

            pygame.draw.rect(screen,
                             color,
                             [MARGIN + (column * CELL_WIDTH) + (column * MARGIN),       
                                             MARGIN + (row * CELL_HEIGHT) + (row * MARGIN),      
                                             CELL_WIDTH,                                     
                                             CELL_HEIGHT])
            
            # Insert tile into game
            img = pygame.transform.scale(img,(CELL_WIDTH, CELL_HEIGHT))
            screen.blit(img,(MARGIN + (column * CELL_WIDTH) + (column * MARGIN)
                             ,MARGIN + (row * CELL_HEIGHT) + (row * MARGIN)))
            
            
    
    # --- Update the screen
    pygame.display.flip()

#--------------------------------------------------------------------------
# Function: setMines(grid)
# Purpose: Will randomly place mines onto the grid
#          *** Assumes an empty grid as input ***
#--------------------------------------------------------------------------
def setMines(grid):

    numMines = 0
    while numMines < TOTAL_MINES:
        rand_row = randint(0, GRID_HEIGHT-1)
        rand_column = randint(0, GRID_WIDTH-1)

        if grid[rand_row][rand_column] != "Mine":
            grid[rand_row][rand_column] = "Mine"
            numMines += 1

#--------------------------------------------------------------------------
# Function: setNumbers(grid)
# Purpose: Will assign numbers to cells based on distance from mines
#          *** Assumes a grid "with mines" as input ***
#--------------------------------------------------------------------------
def setNumbers(grid):
    
    # go through each cell in the grid
    for row in range(GRID_HEIGHT):
        for column in range(GRID_WIDTH):

            # If the current cell is not a mine
            if not isMine(grid, row, column):
                mineCount = 0

                # find the neighboring cells
                neighborList = getNeighbors(grid, row, column)

                # find number of mines in those cells
                for neighbor in neighborList:
                    if isMine(grid,neighbor[0],neighbor[1]):
                        mineCount += 1
                
                grid[row][column] = mineCount
    return

#--------------------------------------------------------------------------
# Function: isBlank(grid, row, column)
# Purpose: Determines if the given cell is blank
#--------------------------------------------------------------------------
def isBlank(grid, row, column):
    return grid[row][column] == 0

#--------------------------------------------------------------------------
# Function: isMine(grid, row, column)
# Purpose: Determines if the given cell is a mine
#--------------------------------------------------------------------------
def isMine(grid, row, column):
    return grid[row][column] == "Mine"

#--------------------------------------------------------------------------
# Function: isNumber(grid, row, column)
# Purpose: Determines if the given cell is a number
#--------------------------------------------------------------------------
def isNumber(grid, row, column):
    cellValue = grid[row][column]
    if cellValue == "Mine" or cellValue == 0:
        return False
    else:
        return True

#--------------------------------------------------------------------------
# Function: getNeighbors(grid, row, column)
# Purpose: Finds and returns a list of neighboring cells for a given cell
#--------------------------------------------------------------------------
def getNeighbors(grid, row, column):

    neighborList = []

    if row != 0: # if it's not in the top row
        neighborList.append([row-1, column]) # add the cell above
        if column != 0:
            neighborList.append([row-1, column-1]) # add upper-left cell
        if column != GRID_WIDTH-1:
            neighborList.append([row-1, column+1]) # add upper-right cell
        
    if row != GRID_HEIGHT-1: # if it's not in the bottom row
        neighborList.append([row+1, column]) # add the cell below
        if column != 0:
            neighborList.append([row+1, column-1]) # add lower-left cell
        if column != GRID_WIDTH-1:
            neighborList.append([row+1, column+1]) # add lower-right cell

    if column != 0:
        neighborList.append([row, column-1]) # Add cell to left
    if column != GRID_WIDTH-1:
        neighborList.append([row, column+1]) # Add cell to right

    return neighborList

#--------------------------------------------------------------------------
# Function: revealTiles(grid, visibleGrid, row, column)
# Purpose: Takes coordinates of a visited blank cell and reveals its
#          neighboring cells. If any of the neighboring cells are also
#          blank, it will recursively call this function again. 
#--------------------------------------------------------------------------
def revealTiles(grid, visibleGrid, row, column):
    
    neighborList = getNeighbors(grid, row, column)

    for neighbor in neighborList:
        neighbor_row = neighbor[0]
        neighbor_column = neighbor[1]
        
        # if neighbor is a number
        if isNumber(grid, neighbor_row, neighbor_column):
            if visibleGrid[neighbor_row][neighbor_column] == 0: # if not visible
                visibleGrid[neighbor_row][neighbor_column] = 1 # reveal the current tile

        # if neighbor is a blank, recursively call revealTiles()
        elif isBlank(grid, neighbor_row, neighbor_column):
            if visibleGrid[neighbor_row][neighbor_column] == 0: # if not visible
                visibleGrid[neighbor_row][neighbor_column] = 1 # reveal the current tile
                revealTiles(grid, visibleGrid, neighbor_row, neighbor_column)
            
        # if neighbor is a mine, do nothing
    
"""
---------------------------------------------------------------------------
"""
main()
