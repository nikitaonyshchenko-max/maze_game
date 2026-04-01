# Maze Generator using Recursive Backtracking

"""
This script implements a maze generation algorithm using Recursive Backtracking.
It is based on exploring the graph of cells and backtracking when necessary. 
The key concepts of graph theory applied in this algorithm include:
- **Graph Representation**: The maze is represented as a grid (2D array), where each cell can be thought of as a vertex in a graph.
- **Edges**: Movement between cells represents edges in the graph.
- **Traversal**: The algorithm traverses the graph depth-first, creating paths by marking cells as visited.
"""

import random

# Define the size of the maze
width = 20  # Width of the maze
height = 10  # Height of the maze

# Directions for movement (up, down, left, right)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Create a maze grid initialized to walls
maze = [['#'] * (width * 2 + 1) for _ in range(height * 2 + 1)]

# Function to check if a cell is within the maze bounds
def within_bounds(x, y):
    return 0 <= x < width and 0 <= y < height

# Function to carve a path in the maze
def carve_path(x, y):
    # Mark the cell as part of the maze
    maze[y * 2 + 1][x * 2 + 1] = ' '
    random.shuffle(directions)  # Shuffle directions for random generation
    for dx, dy in directions:
        nx, ny = x + dx, y + dy  # Calculate new cell coordinates
        # Check if the next cell is within bounds and is a wall
        if within_bounds(nx, ny) and maze[ny * 2 + 1][nx * 2 + 1] == '#':
            # Carve a path between the current cell and the next cell
            maze[y * 2 + 1 + dy][x * 2 + 1 + dx] = ' '
            carve_path(nx, ny)  # Recur to continue carving

# Start the maze generation from the top-left cell
carve_path(0, 0)

# Print the generated maze
for row in maze:
    print(''.join(row))