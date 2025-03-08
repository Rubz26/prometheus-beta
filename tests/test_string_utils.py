import pytest
from src.string_utils import remove_duplicate_words

def test_remove_duplicate_words_basic():
    """Test basic functionality of removing duplicate words."""
    assert remove_duplicate_words("hello world hello python world") == "hello world python"

def test_remove_duplicate_words_no_duplicates():
    """Test with a string that has no duplicate words."""
    assert remove_duplicate_words("the quick brown fox") == "the quick brown fox"

def test_remove_duplicate_words_all_duplicates():
    """Test with a string where all words are duplicates."""
    assert remove_duplicate_words("hello hello hello") == "hello"

def test_remove_duplicate_words_empty_string():
    """Test with an empty string."""
    assert remove_duplicate_words("") == ""

def test_remove_duplicate_words_single_word():
    """Test with a single word."""
    assert remove_duplicate_words("hello") == "hello"

def test_remove_duplicate_words_type_error():
    """Test that a TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        remove_duplicate_words(123)
        remove_duplicate_words(None)
        remove_duplicate_words(["hello", "world"])