import pytest
from src.palindrome_substrings import find_palindrome_substrings

def test_empty_string():
    """Test that an empty string returns an empty list."""
    assert find_palindrome_substrings("") == []

def test_none_input():
    """Test that None input returns an empty list."""
    assert find_palindrome_substrings(None) == []

def test_single_character():
    """Test that single characters are recognized as palindromes."""
    result = find_palindrome_substrings("a")
    assert set(result) == {"a"}

def test_single_character_string():
    """Test a string with multiple single character palindromes."""
    result = find_palindrome_substrings("abc")
    assert set(result) == {"a", "b", "c"}

def test_repeated_characters():
    """Test string with repeated characters."""
    result = find_palindrome_substrings("aaa")
    assert set(result) == {"a", "aa", "aaa"}

def test_complex_palindromes():
    """Test a more complex string with multiple palindromes."""
    result = find_palindrome_substrings("racecar")
    expected = {"r", "a", "c", "e", "racecar", "aceca", "cec"}
    assert set(result) == expected

def test_no_palindromes():
    """Test a string with no palindromes longer than single characters."""
    result = find_palindrome_substrings("abcd")
    assert set(result) == {"a", "b", "c", "d"}

def test_palindrome_with_different_case():
    """Test that palindromes are case-sensitive."""
    result = find_palindrome_substrings("Aba")
    assert set(result) == {"A", "a", "b"}

def test_large_palindrome():
    """Test a long palindrome."""
    test_str = "a" * 100
    result = find_palindrome_substrings(test_str)
    assert len(result) > 1
    assert f"{'a' * 10}" in result  # Check that there are longer palindromes

def test_mixed_palindromes():
    """Test a string with mixed palindromes."""
    result = find_palindrome_substrings("abcba")
    expected = {"a", "b", "c", "abcba", "bcb"}
    assert set(result) == expected