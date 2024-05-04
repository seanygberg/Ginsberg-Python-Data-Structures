def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1_str = str(num1)
    num2_str = str(num2)

    num1_freq = {}
    for digit in num1_str:
        num1_freq[digit] = num1_freq.get(digit,0) + 1
    
    num2_freq = {}
    for digit in num2_str:
        num2_freq[digit] = num2_freq.get(digit,0) + 1

    return num1_freq == num2_freq