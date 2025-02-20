def is_prime(num):
    """
    Check if a number is prime.
    
    Args:
        num (int): Number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_sum_pairs(n):
    """
    Find unique prime numbers that can be obtained by summing pairs of numbers 
    from the range [1, n].
    
    Args:
        n (int): Upper bound of the range to consider.
    
    Returns:
        list: Sorted list of unique prime numbers formed by summing pairs.
    """
    if n < 2:
        return []
    
    # Set to store unique prime sums
    prime_sums = set()
    
    # Check all possible pairs
    for i in range(1, n):
        for j in range(i, n + 1):
            current_sum = i + j
            if current_sum > n and is_prime(current_sum):
                prime_sums.add(current_sum)
    
    # Return sorted list of unique prime sums
    return sorted(list(prime_sums))