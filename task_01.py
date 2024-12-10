import re

def is_palindrome(string):
    if string is None:
        return False
    s = re.sub(r'[^a-zA-Z0-9]', '', str(string)).lower()
    return s == s[::-1]


print(is_palindrome("A man, a plan, a canal -- Panama")) # => True
print(is_palindrome("Madam, I'm Adam!")) # => True
print(is_palindrome(333)) # => True
print(is_palindrome(None)) # => False
print(is_palindrome("Abracadabra")) # => False

