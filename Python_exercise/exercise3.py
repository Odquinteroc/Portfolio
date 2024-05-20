'''
"Given a string of any length, return 50% or half of the given string.
Notes/Constraints:
• Should a given string have an odd number of letters, round down to the nearest number.
'''

def half_string(text: str )-> str:
    
    new_text = str[:len(text)//2]
    return new_text

print(half_string('texto'))
