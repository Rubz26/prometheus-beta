from typing import List
from itertools import combinations

def count_equal_sum_partitions(numbers: List[int]) -> int:
    """
    Calculate the number of ways a group of numbers can be partitioned 
    into two subsets with equal sums.

    Args:
        numbers (List[int]): A list of integers to partition.

    Returns:
        int: The number of ways the numbers can be partitioned into two subsets 
             with equal total sums.

    Raises:
        ValueError: If the input list is empty.
    """
    # Validate input
    if not numbers:
        raise ValueError("Input list cannot be empty")

    total_sum = sum(numbers)
    
    # If total sum is odd, no equal partition is possible
    if total_sum % 2 != 0:
        return 0

    target_sum = total_sum // 2
    count = 0

    def is_valid_partition(subset):
        """Check if the subset partitioning is valid."""
        if not subset:
            return False
        
        complement = [num for num in numbers if num not in subset]
        return (sum(subset) == target_sum and 
                sum(complement) == target_sum and 
                len(subset) > 0 and 
                len(complement) > 0)

    # Special case handling
    numbers_set = set(numbers)
    numbers_freq = {num: numbers.count(num) for num in numbers_set}

    # Try all possible combinations
    seen_partitions = set()
    for r in range(1, len(numbers) // 2 + 1):
        for subset in combinations(numbers, r):
            # Convert subset to a sorted tuple of unique values to avoid duplicates
            subset_key = tuple(sorted(set(subset)))
            
            # Check partition validity and avoid counting same partition multiple times
            if is_valid_partition(subset) and subset_key not in seen_partitions:
                count += 1
                seen_partitions.add(subset_key)

    return count