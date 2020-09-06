import pygame
import math
from queue import PriorityQueue

# Set up window display
# Window width
WIDTH = 800
WINDOW = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A * Path Finding Visualizer")

# All the colors to be used in this project
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Build the visualization tool
class Node:
    # Keep track of each node in the grid
    # Each node will be represented with different colors
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self. x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

        def get_position(self):
            return self.row, self.col

        # Red nodes
        def is_closed(self):
            return self.color == RED

        def is_open(self):
            return self.color == GREEN

        def is_barrier(self):
            return self.color == BLACK

        def is_start(self):
            return self.color == ORANGE

        def is_end(self):
            return self.color == TURQUOISE

        def reset(self):
            self.color == WHITE

        def make_closed(self):
            self.color = RED

        def make_open(self):
            self.color = GREEN

        def make_barrier(self):
            self.color = BLACK

        def make_end(self):
            self.color = TURQUOISE

        def make_path(self):
            self.color = PURPLE

        # Draw the nodes onto the grid
        def draw(self, win):
            pygame.draw.rect(win, self.color, ())