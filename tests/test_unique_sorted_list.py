import pytest
from src.unique_sorted_list import get_unique_sorted_integers

def test_basic_functionality():
    """Test the function with a standard list of integers."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    assert get_unique_sorted_integers(input_list) == [1, 2, 3, 4, 5, 6, 9]

def test_empty_list():
    """Test with an empty list."""
    assert get_unique_sorted_integers([]) == []

def test_already_sorted_list():
    """Test with an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert get_unique_sorted_integers(input_list) == [1, 2, 3, 4, 5]

def test_negative_integers():
    """Test with negative integers."""
    input_list = [-3, -1, -4, -1, -5, 0, 0]
    assert get_unique_sorted_integers(input_list) == [-5, -4, -3, -1, 0]

def test_single_element():
    """Test with a single element list."""
    input_list = [42]
    assert get_unique_sorted_integers(input_list) == [42]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        get_unique_sorted_integers("not a list")

def test_invalid_element_type():
    """Test that a TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        get_unique_sorted_integers([1, 2, "3", 4])