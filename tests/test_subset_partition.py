import pytest
from src.subset_partition import count_equal_sum_partitions

def test_basic_partition():
    """Test a simple case with multiple equal sum partitions."""
    numbers = [1, 2, 3, 4, 5, 7]
    assert count_equal_sum_partitions(numbers) == 1

def test_no_partition():
    """Test a case where no equal sum partition exists."""
    numbers = [1, 2, 3, 4, 5]
    assert count_equal_sum_partitions(numbers) == 0

def test_single_partition():
    """Test a case with a specific equal sum partition."""
    numbers = [1, 1, 2, 2]
    assert count_equal_sum_partitions(numbers) == 1

def test_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        count_equal_sum_partitions([])

def test_large_numbers():
    """Test a case with larger numbers."""
    numbers = [10, 20, 30, 40, 50, 60]
    assert count_equal_sum_partitions(numbers) > 0

def test_complex_partition():
    """Test a more complex partitioning scenario."""
    numbers = [3, 1, 1, 2, 2, 1]
    assert count_equal_sum_partitions(numbers) > 0

def test_difficult_partition():
    """Test a challenging partitioning scenario."""
    numbers = [1, 2, 3, 4, 5, 5]
    assert count_equal_sum_partitions(numbers) > 0