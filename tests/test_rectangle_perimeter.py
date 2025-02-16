import pytest
from src.rectangle_perimeter import calculate_rectangle_perimeter

def test_rectangle_perimeter_positive_numbers():
    """Test perimeter calculation with positive integers and floats"""
    assert calculate_rectangle_perimeter(5, 3) == 16
    assert calculate_rectangle_perimeter(2.5, 4.5) == 14.0
    assert calculate_rectangle_perimeter(10, 7.5) == 35.0

def test_rectangle_perimeter_zero():
    """Test perimeter calculation when length or width is zero"""
    assert calculate_rectangle_perimeter(0, 5) == 10
    assert calculate_rectangle_perimeter(5, 0) == 10
    assert calculate_rectangle_perimeter(0, 0) == 0

def test_rectangle_perimeter_negative_numbers():
    """Test that negative numbers raise a ValueError"""
    with pytest.raises(ValueError, match="Length and width must be non-negative values"):
        calculate_rectangle_perimeter(-5, 3)
    with pytest.raises(ValueError, match="Length and width must be non-negative values"):
        calculate_rectangle_perimeter(5, -3)
    with pytest.raises(ValueError, match="Length and width must be non-negative values"):
        calculate_rectangle_perimeter(-5, -3)