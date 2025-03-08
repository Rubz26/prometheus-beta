import pytest
from src.palindrome_counter import count_palindromic_substrings

def test_empty_string():
    """Test that an empty string returns 0 palindromic substrings"""
    assert count_palindromic_substrings("") == 0

def test_single_character():
    """Test that a single character is a palindrome"""
    assert count_palindromic_substrings("a") == 1

def test_two_different_characters():
    """Test a string with two different characters"""
    assert count_palindromic_substrings("ab") == 2

def test_two_same_characters():
    """Test a string with two same characters"""
    assert count_palindromic_substrings("aa") == 3

def test_three_characters_all_same():
    """Test a string with three same characters"""
    assert count_palindromic_substrings("aaa") == 6

def test_mixed_palindromes():
    """Test a string with mixed palindromes"""
    assert count_palindromic_substrings("abc") == 3

def test_longer_palindromic_string():
    """Test a longer string with multiple palindromes"""
    assert count_palindromic_substrings("racecar") == 10

def test_complex_palindrome():
    """Test a complex string with various palindromic substrings"""
    assert count_palindromic_substrings("aabaa") == 9