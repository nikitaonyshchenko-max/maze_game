import numpy as np
import matplotlib.pyplot as plt
from collections import deque

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = maze.shape[0]
        self.cols = maze.shape[1]
        self.start = None
        self.end = None

    def set_start_end(self, start, end):
        self.start = start
        self.end = end

    def solve(self):
        # BFS initialization
        queue = deque([self.start])
        visited = np.zeros_like(self.maze, dtype=bool)
        visited[self.start] = True
        parent = {self.start: None}

        while queue:
            current = queue.popleft()

            # Check if we reached the end
            if current == self.end:
                return self.retrace_path(parent)

            # Explore neighbors
            for neighbor in self.get_neighbors(current):
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = current
                    queue.append(neighbor)
                    self.visualize()  # Visualize progress

        return None  # No path found

    def get_neighbors(self, pos):
        x, y = pos
        neighbors = []

        # Possible movements: up, down, left, right
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.maze[nx, ny] == 0:
                neighbors.append((nx, ny))
        return neighbors

    def retrace_path(self, parent):
        # Retrace the path from end to start
        path = []
        step = self.end
        while step is not None:
            path.append(step)
            step = parent[step]
        return path[::-1]  # Return reversed path

    def visualize(self):
        plt.imshow(self.maze, cmap='binary')  # Display the maze
        plt.pause(0.1)

# Example usage
if __name__ == '__main__':
    # Create a maze (0 = path, 1 = wall)
    maze = np.array([
        [0, 1, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 1, 0]
    ])
    solver = MazeSolver(maze)
    solver.set_start_end((0, 0), (4, 4))
    path = solver.solve()
    print('Path found:', path)  # Print the path found