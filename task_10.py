from collections import Counter
import re

def count_words(string):
    words = re.findall(r'\b\w+\b', string.lower())
    return Counter(words)

print(count_words("A man, a plan, a canal -- Panama")) # {"a": 3, "man": 1, "plan": 1, "canal": 1, "panama": 1}
print(count_words("Doo bee doo bee doo")) # {"doo": 3, "bee": 2}
