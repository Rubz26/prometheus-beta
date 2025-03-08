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

    # Use all possible subset sizes from 1 to len(numbers)//2
    for r in range(1, len(numbers) // 2 + 1):
        # Generate all combinations of size r
        for subset in combinations(numbers, r):
            # Compute subset sum
            subset_sum = sum(subset)
            
            # Check if this subset sum matches the target
            if subset_sum == target_sum:
                # Get the complement subset
                complement = [num for num in numbers if num not in subset]
                
                # Check if complement also sums to target
                if sum(complement) == target_sum:
                    # Ensure both subsets are non-empty
                    if len(subset) > 0 and len(complement) > 0:
                        count += 1

    return count