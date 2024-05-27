'''Write a function that accept a string as a single argument and print out whether that string is a palindrome. (A palindrome is a string that reads the same forwards and backwards.) For example, "abcddcba" is a palindrome, "1221" is also a palindrome.'''

def palindrome(text: str)-> bool:
    if text == text[::-1]:
        return True
    return False

print(palindrome('345'))