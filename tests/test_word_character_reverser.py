import pytest
from src.word_character_reverser import reverse_words_and_characters

def test_normal_sentence():
    """Test a normal sentence with multiple words."""
    assert reverse_words_and_characters("Hello World") == "dlroW olleH"

def test_multiple_words():
    """Test a sentence with more than two words."""
    assert reverse_words_and_characters("Python is awesome") == "emosewa si nohtyP"

def test_empty_string():
    """Test an empty string input."""
    assert reverse_words_and_characters("") == ""

def test_single_word():
    """Test a single word input."""
    assert reverse_words_and_characters("hello") == "olleh"

def test_sentence_with_punctuation():
    """Test a sentence with punctuation."""
    assert reverse_words_and_characters("Hello, World!") == "!dlroW ,olleH"

def test_sentence_with_mixed_case():
    """Test a sentence with mixed case letters."""
    assert reverse_words_and_characters("Python Programming") == "gnimmargorP nohtyP"

def test_sentence_with_repeated_words():
    """Test a sentence with repeated words."""
    assert reverse_words_and_characters("hello hello world") == "dlrow olleh olleh"