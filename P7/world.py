# ===================================================================================
# file: world.py
# author: Oracle16
# date: 04/09/2025
# ===================================================================================

class World:
    # Constructor to create the world with given rows and columns
    def __init__(self, total_rows, total_columns):
        self.total_rows = total_rows
        self.total_columns = total_columns
        self.player_current_row = 0  # player starts at bottom-left corner (0,0)
        self.player_current_column = 0
        self.obstacle_positions = set()  # set to store obstacle positions

    # Returns the total number of rows in the world
    def numRows(self):
        return self.total_rows

    # Returns the total number of columns in the world
    def numColumns(self):
        return self.total_columns

    # Returns the current location of the player as a tuple (row, column)
    def playerLocation(self):
        return (self.player_current_row, self.player_current_column)

    # Moves player to a specific row and column if it's a valid position and not an obstacle
    def moveTo(self, new_row, new_column):
        # check if new position is inside the world and not an obstacle
        if (0 <= new_row < self.total_rows and
            0 <= new_column < self.total_columns and
            (new_row, new_column) not in self.obstacle_positions):
            self.player_current_row = new_row
            self.player_current_column = new_column
            return True  # move successful
        return False  # move unsuccessful

    # Moves player up one row if possible
    def moveUp(self):
        return self.moveTo(self.player_current_row + 1, self.player_current_column)

    # Moves player down one row if possible
    def moveDown(self):
        return self.moveTo(self.player_current_row - 1, self.player_current_column)

    # Moves player left one column if possible
    def moveLeft(self):
        return self.moveTo(self.player_current_row, self.player_current_column - 1)

    # Moves player right one column if possible
    def moveRight(self):
        return self.moveTo(self.player_current_row, self.player_current_column + 1)

    # Adds an obstacle at the specified row and column
    def addObstacle(self, obstacle_row, obstacle_column):
        # check if obstacle position is inside the world
        if (0 <= obstacle_row < self.total_rows and
            0 <= obstacle_column < self.total_columns):
            self.obstacle_positions.add((obstacle_row, obstacle_column))

    # Returns a list of all obstacle positions
    def getObstacles(self):
        return list(self.obstacle_positions)