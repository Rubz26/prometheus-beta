import pytest
from src.mall_navigation import find_minimum_path

def test_simple_path():
    mall_graph = {
        'A': {'B': 5, 'C': 2},
        'B': {'A': 5, 'C': 1, 'D': 3},
        'C': {'A': 2, 'B': 1, 'D': 6},
        'D': {'B': 3, 'C': 6}
    }
    path, distance = find_minimum_path(mall_graph, 'A', 'D')
    assert path == ['A', 'C', 'B', 'D']
    assert distance == 6

def test_direct_path():
    mall_graph = {
        'A': {'B': 5, 'C': 2},
        'B': {'A': 5},
        'C': {'A': 2}
    }
    path, distance = find_minimum_path(mall_graph, 'A', 'B')
    assert path == ['A', 'B']
    assert distance == 5

def test_same_start_and_end():
    mall_graph = {
        'A': {'B': 5},
        'B': {'A': 5}
    }
    path, distance = find_minimum_path(mall_graph, 'A', 'A')
    assert path == ['A']
    assert distance == 0

def test_non_existent_start_store():
    mall_graph = {
        'A': {'B': 5},
        'B': {'A': 5}
    }
    with pytest.raises(ValueError, match="Start store 'C' not found"):
        find_minimum_path(mall_graph, 'C', 'A')

def test_non_existent_end_store():
    mall_graph = {
        'A': {'B': 5},
        'B': {'A': 5}
    }
    with pytest.raises(ValueError, match="End store 'C' not found"):
        find_minimum_path(mall_graph, 'A', 'C')

def test_disconnected_graph():
    mall_graph = {
        'A': {'B': 5},
        'B': {'A': 5},
        'C': {'D': 3},
        'D': {'C': 3}
    }
    with pytest.raises(ValueError, match="No path exists"):
        find_minimum_path(mall_graph, 'A', 'C')

def test_complex_path():
    mall_graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'D': 3},
        'C': {'A': 2, 'D': 5, 'E': 7},
        'D': {'B': 3, 'C': 5, 'E': 1},
        'E': {'C': 7, 'D': 1}
    }
    path, distance = find_minimum_path(mall_graph, 'A', 'E')
    assert path == ['A', 'C', 'D', 'E']
    assert distance == 8