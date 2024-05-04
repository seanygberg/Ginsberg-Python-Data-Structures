def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = "aeiou"
    counter = {}
    for char in phrase:
        my_char = char.lower()
        if my_char in vowels:
            counter[my_char] = counter.get(my_char, 0) + 1
    return counter