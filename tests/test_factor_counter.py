import pytest
from src.factor_counter import count_factors

def test_count_factors_basic():
    """Test basic factor counting for known values."""
    assert count_factors(1) == 1
    assert count_factors(4) == 3  # 1, 2, 4
    assert count_factors(12) == 6  # 1, 2, 3, 4, 6, 12

def test_count_factors_prime():
    """Test factor counting for prime numbers."""
    assert count_factors(7) == 2  # 1 and 7
    assert count_factors(11) == 2  # 1 and 11

def test_count_factors_large_number():
    """Test factor counting for larger numbers."""
    assert count_factors(100) == 9  # 1, 2, 4, 5, 10, 20, 25, 50, 100

def test_count_factors_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        count_factors("not an int")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        count_factors(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        count_factors(-5)