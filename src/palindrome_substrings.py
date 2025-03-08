def find_palindrome_substrings(s):
    """
    Find all palindromic substrings in a given string.
    
    A palindromic substring is a substring that reads the same forwards and backwards.
    
    Args:
        s (str): The input string to search for palindromic substrings.
    
    Returns:
        list: A list of all unique palindromic substrings found in the input string.
    
    Examples:
        >>> find_palindrome_substrings("abc")
        ['a', 'b', 'c']
        >>> find_palindrome_substrings("aaa")
        ['a', 'aa', 'aaa']
    """
    # Handle edge cases
    if not s or not isinstance(s, str):
        return []
    
    # Set to store unique palindromic substrings
    palindromes = set()
    
    # Check all possible substrings
    for start in range(len(s)):
        for end in range(start, len(s)):
            substring = s[start:end+1]
            # Check if substring is a palindrome
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return list(sorted(palindromes, key=lambda x: (len(x), x)))