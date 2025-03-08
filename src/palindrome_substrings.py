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
    for i in range(len(s)):
        # Odd length palindromes
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1
        
        # Even length palindromes
        left, right = i, i+1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1
    
    return list(palindromes)