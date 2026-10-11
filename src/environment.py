import numpy as np


class Environment:
    """
    Represents the 2D virtual world
    where our autonomous robot will navigate.
    """

    def __init__(self, width=30, height=20):

        self.width = width
        self.height = height

        # Create an empty map.
        # 0 = free space
        # 1 = obstacle
        self.grid = np.zeros(
            (height, width),
            dtype=int
        )

        self.create_obstacles()

    def create_obstacles(self):
        """
        Create obstacles inside the virtual world.
        """

        # Horizontal obstacle
        self.grid[5:8, 5:15] = 1

        # Vertical obstacle
        self.grid[10:17, 18:21] = 1

        # Another obstacle
        self.grid[13:16, 7:13] = 1

    def is_valid(self, position):
        """
        Check whether a position is inside the map
        and not occupied by an obstacle.
        """

        x, y = position

        # Check map boundaries
        if x < 0 or x >= self.width:
            return False

        if y < 0 or y >= self.height:
            return False

        # Check whether the location is an obstacle
        if self.grid[y, x] == 1:
            return False

        return True