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

        # Methods to open and close different nodes
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
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

        def update_neighbors(self, grid):
            pass
        
        # Make a method name less than (lt for short) to compare two spots together and handle the logic
        def __lt__(self, other):
            return False


# Heuristic function
def heuristic(point1, point2):
    # Figure out the distance between points 1 and 2 by using Manhattan distance
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

# Grid function
def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        # Create nested lists of Node objects inside
        grid.append([])
        for j in range(rows):
            # Create node object and append it to the grid
            node = Node(i, j, gap, rows)
            grid[i].append(node)

    return grid

# Draw grid lines
def draw_grid(win, rows, width):
    gap = width // rows
    # Horizontal lines
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
    # Vertical lines
    for j in range(rows):
        pygame.draw.line(win, GREY, (j * gap, 0), (i * gap, width))

# Create main draw function
def draw(window, grid, rows, width):
    window.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(window)
    
    draw_grid(window, rows, width)
    pygame.display.update()


