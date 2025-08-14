# ===================================================================================
# file: oasis.py
# author: Oracle16
# date: 04/21/2025
# ===================================================================================

from world import World

class Oasis(World):
    def __init__(self, numRows, numCols):
        super().__init__(numRows, numCols)
        self._eggs = set()      # set of (row, col) tuples for eggs
        self._score = 0         # number of eggs collected

    def addEgg(self, row, col):
        """Add an egg at (row, col) if not already present."""
        self._eggs.add((row, col))

    def eggLocations(self):
        """Return a set of (row, col) tuples for eggs not yet collected."""
        return set(self._eggs)

    def getScore(self):
        """Return the number of eggs collected by the player."""
        return self._score

    def moveTo(self, newRow, newCol):
        """Move player, collect egg if present, and return if move was legal."""
        moved = super().moveTo(newRow, newCol)
        if moved:
            loc = self.playerLocation()
            if loc in self._eggs:
                self._eggs.remove(loc)
                self._score += 1
        return moved