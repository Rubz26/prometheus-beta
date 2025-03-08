from typing import List

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
    
    # Dynamic programming approach
    # Each state is (current_sum, current_index, count_1, count_2)
    dp = {}
    dp[(0, 0, 0, 0)] = 1

    for num in numbers:
        new_dp = dp.copy()
        for (sum_1, sum_2, count_1, count_2), ways in dp.items():
            # Try adding to first subset
            new_sum_1 = sum_1 + num
            if new_sum_1 <= target_sum:
                new_key = (new_sum_1, sum_2, count_1 + 1, count_2)
                new_dp[new_key] = new_dp.get(new_key, 0) + ways

            # Try adding to second subset
            new_sum_2 = sum_2 + num
            if new_sum_2 <= target_sum:
                new_key = (sum_1, new_sum_2, count_1, count_2 + 1)
                new_dp[new_key] = new_dp.get(new_key, 0) + ways

        dp = new_dp

    # Count valid partitions where both subset sums equal target_sum
    return sum(ways for (sum_1, sum_2, count_1, count_2), ways in dp.items() 
               if sum_1 == target_sum and sum_2 == target_sum and 
               (count_1 > 0 and count_2 > 0))