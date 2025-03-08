def remove_duplicate_words(sentence):
    """
    Remove duplicate words from a string while maintaining original order.

    Args:
        sentence (str): Input string containing words to be processed.

    Returns:
        str: A string with duplicate words removed, preserving the first occurrence.

    Raises:
        TypeError: If input is not a string.

    Examples:
        >>> remove_duplicate_words("hello world hello python world")
        'hello world python'
        >>> remove_duplicate_words("the quick brown fox jumps the quick fox")
        'the quick brown fox jumps'
    """
    # Validate input type
    if not isinstance(sentence, str):
        raise TypeError("Input must be a string")

    # Handle empty string case
    if not sentence:
        return ""

    # Split the sentence into words
    words = sentence.split()
    
    # Use a set to track seen words while preserving order
    seen_words = set()
    unique_words = []
    
    for word in words:
        # Only add word if it hasn't been seen before
        if word not in seen_words:
            unique_words.append(word)
            seen_words.add(word)
    
    # Join the unique words back into a string
    return " ".join(unique_words)