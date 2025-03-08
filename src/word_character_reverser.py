def reverse_words_and_characters(input_string):
    """
    Reverse the order of words in a string and the characters within each word.

    Args:
        input_string (str): The input string to be transformed.

    Returns:
        str: A string with words in reverse order and each word's characters reversed.

    Examples:
        >>> reverse_words_and_characters("Hello World")
        "dlroW olleH"
        >>> reverse_words_and_characters("Python is awesome")
        "emosewa si nohtyP"
        >>> reverse_words_and_characters("")
        ""
    """
    # Handle empty string case
    if not input_string:
        return ""
    
    # Split the string into words, reverse the order, 
    # and reverse characters of each word
    reversed_words = [word[::-1] for word in input_string.split()[::-1]]
    
    # Join the reversed words back into a string
    return " ".join(reversed_words)