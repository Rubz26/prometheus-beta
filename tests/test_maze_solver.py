import pytest
from src.maze_solver import MazeSolver

class TestMazeSolver:
    def setup_method(self):
        self.solver = MazeSolver()
    
    def test_simple_path(self):
        maze = [
            ['S', '0', '0', '0'],
            ['1', '1', '0', '1'],
            ['0', '0', '0', 'E']
        ]
        path = self.solver.find_shortest_path(maze)
        assert path is not None
        assert path[0] == (0, 0)  # Start at S
        assert path[-1] == (2, 3)  # End at E
    
    def test_direct_path(self):
        maze = [
            ['S', '0', 'E']
        ]
        path = self.solver.find_shortest_path(maze)
        assert path == [(0, 0), (0, 1), (0, 2)]
    
    def test_blocked_path(self):
        maze = [
            ['S', '1', 'E']
        ]
        path = self.solver.find_shortest_path(maze)
        assert path is None
    
    def test_complex_maze(self):
        maze = [
            ['S', '0', '0', '0', '0'],
            ['1', '1', '1', '0', '1'],
            ['0', '0', '0', '0', '0'],
            ['0', '1', '1', '1', '0'],
            ['0', '0', '0', '0', 'E']
        ]
        path = self.solver.find_shortest_path(maze)
        assert path is not None
        assert path[0] == (0, 0)  # Start at S
        assert path[-1] == (4, 4)  # End at E
    
    def test_no_path(self):
        maze = [
            ['S', '1', '1'],
            ['1', '1', '1'],
            ['1', '1', 'E']
        ]
        path = self.solver.find_shortest_path(maze)
        assert path is None
    
    def test_empty_maze(self):
        with pytest.raises(ValueError, match="Maze cannot be empty"):
            self.solver.find_shortest_path([])
    
    def test_maze_without_start_or_exit(self):
        maze = [
            ['0', '0', '0'],
            ['0', '0', '0']
        ]
        with pytest.raises(ValueError, match="Maze must contain both start"):
            self.solver.find_shortest_path(maze)