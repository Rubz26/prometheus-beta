import pytest
from src.prime_sum_pairs import find_prime_sum_pairs, is_prime

def test_is_prime():
    # Test prime numbers
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(17) == True
    
    # Test non-prime numbers
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(4) == False
    assert is_prime(15) == False

def test_find_prime_sum_pairs():
    # Test small input
    assert find_prime_sum_pairs(2) == []
    
    # Test larger inputs
    result_5 = find_prime_sum_pairs(5)
    assert result_5 == [5]  # Only prime sum possible is 2+3
    
    result_10 = find_prime_sum_pairs(10)
    assert set(result_10) == {5, 7, 11, 13}
    
    # Test edge cases
    assert find_prime_sum_pairs(1) == []
    assert find_prime_sum_pairs(0) == []

def test_find_prime_sum_pairs_uniqueness():
    # Ensure results are unique
    result = find_prime_sum_pairs(20)
    assert len(result) == len(set(result))
    
    # Verify all results are prime
    for num in result:
        assert is_prime(num) == True