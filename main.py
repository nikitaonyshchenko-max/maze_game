import pygame
import random
from collections import deque

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Cell class to represent each cell in the maze
class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.visited = False
        self.walls = [True, True, True, True]  # top, right, bottom, left

# Maze generation using Recursive Backtracking
def generate_maze():
    grid = [[Cell(row, col) for col in range(COLS)] for row in range(ROWS)]
    stack = []
    current_cell = grid[0][0]
    current_cell.visited = True
    total_cells = ROWS * COLS
    visited_cells = 1

    while visited_cells < total_cells:
        neighbors = []
        row, col = current_cell.row, current_cell.col

        if row > 0 and not grid[row - 1][col].visited:  # Up
            neighbors.append(grid[row - 1][col])
        if row < ROWS - 1 and not grid[row + 1][col].visited:  # Down
            neighbors.append(grid[row + 1][col])
        if col > 0 and not grid[row][col - 1].visited:  # Left
            neighbors.append(grid[row][col - 1])
        if col < COLS - 1 and not grid[row][col + 1].visited:  # Right
            neighbors.append(grid[row][col + 1])
        
        if neighbors:
            neighbor = random.choice(neighbors)
            if neighbor.row < current_cell.row:  # Up
                current_cell.walls[0] = False
                neighbor.walls[2] = False
            elif neighbor.row > current_cell.row:  # Down
                current_cell.walls[2] = False
                neighbor.walls[0] = False
            elif neighbor.col < current_cell.col:  # Left
                current_cell.walls[3] = False
                neighbor.walls[1] = False
            elif neighbor.col > current_cell.col:  # Right
                current_cell.walls[1] = False
                neighbor.walls[3] = False

            stack.append(current_cell)
            current_cell = neighbor
            current_cell.visited = True
            visited_cells += 1
        else:
            current_cell = stack.pop()

    return grid

# BFS algorithm to solve the maze
def bfs_solve(maze):
    start = (0, 0)
    end = (ROWS - 1, COLS - 1)
    queue = deque([start])
    visited = {start: None}
    
    while queue:
        current = queue.popleft()
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return path[::-1]  # Return reversed path

        row, col = current
        for direction, (dr, dc) in [(0, -1), (-1, 0), (0, 1), (1, 0)]:  # Up, Left, Down, Right
            neighbor = (row + dr, col + dc)
            if (0 <= neighbor[0] < ROWS and
                    0 <= neighbor[1] < COLS and
                    neighbor not in visited and
                    not maze[row][col].walls[direction]):
                queue.append(neighbor)
                visited[neighbor] = current

# Pygame visualization
def draw_maze(win, grid):
    for row in grid:
        for cell in row:
            x, y = cell.col * CELL_SIZE, cell.row * CELL_SIZE
            if cell.walls[0]:  # Top
                pygame.draw.line(win, BLACK, (x, y), (x + CELL_SIZE, y))
            if cell.walls[1]:  # Right
                pygame.draw.line(win, BLACK, (x + CELL_SIZE, y), (x + CELL_SIZE, y + CELL_SIZE))
            if cell.walls[2]:  # Bottom
                pygame.draw.line(win, BLACK, (x, y + CELL_SIZE), (x + CELL_SIZE, y + CELL_SIZE))
            if cell.walls[3]:  # Left
                pygame.draw.line(win, BLACK, (x, y), (x, y + CELL_SIZE))

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("2D Maze Game")

    grid = generate_maze()
    path = bfs_solve(grid)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        win.fill(WHITE)
        draw_maze(win, grid)
        for (row, col) in path:
            pygame.draw.rect(win, GREEN, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
