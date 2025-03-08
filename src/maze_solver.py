from typing import List, Tuple, Optional
from collections import deque

class MazeSolver:
    """
    A class to solve the shortest path problem in a 2D maze.
    
    The maze is represented as a 2D grid where:
    - 0 represents a passable path
    - 1 represents a wall/blocked cell
    - 'S' represents the start point
    - 'E' represents the exit point
    """
    
    def find_shortest_path(self, maze: List[List[str]]) -> Optional[List[Tuple[int, int]]]:
        """
        Find the shortest path from start to exit in the maze using Breadth-First Search.
        
        Args:
            maze (List[List[str]]): 2D grid representing the maze
        
        Returns:
            Optional[List[Tuple[int, int]]]: List of coordinates representing the shortest path,
                                             or None if no path exists
        
        Raises:
            ValueError: If maze is empty or does not contain start/exit points
        """
        if not maze or not maze[0]:
            raise ValueError("Maze cannot be empty")
        
        # Find start and exit points
        start, exit = self._find_start_and_exit(maze)
        
        # Validate start and exit points
        if start is None or exit is None:
            raise ValueError("Maze must contain both start ('S') and exit ('E') points")
        
        # Possible movement directions: up, right, down, left
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        rows, cols = len(maze), len(maze[0])
        visited = set()
        queue = deque([(start, [start])])
        
        while queue:
            (x, y), path = queue.popleft()
            
            # Check if reached exit
            if (x, y) == exit:
                return path
            
            # Mark current cell as visited
            visited.add((x, y))
            
            # Explore neighboring cells
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Check if new cell is valid
                if (0 <= nx < rows and 
                    0 <= ny < cols and 
                    maze[nx][ny] != '1' and 
                    (nx, ny) not in visited):
                    queue.append(((nx, ny), path + [(nx, ny)]))
        
        # No path found
        return None
    
    def _find_start_and_exit(self, maze: List[List[str]]) -> Tuple[Optional[Tuple[int, int]], Optional[Tuple[int, int]]]:
        """
        Find the start and exit points in the maze.
        
        Args:
            maze (List[List[str]]): 2D grid representing the maze
        
        Returns:
            Tuple of start and exit coordinates
        """
        start, exit = None, None
        
        for x in range(len(maze)):
            for y in range(len(maze[0])):
                if maze[x][y] == 'S':
                    start = (x, y)
                elif maze[x][y] == 'E':
                    exit = (x, y)
        
        return start, exit