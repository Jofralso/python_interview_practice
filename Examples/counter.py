# Implement a function to count the number of occurrences 
# of each character in a string.
# 
from collections import Counter

def count_characters(s: str) -> dict:
    return dict(Counter(s))


print(count_characters("hello"))
print(count_characters("world"))


def char_count(s: str) -> dict:

    char_count_dict = {}
    for char in s:
        char_count_dict[char] = char_count_dict.get(char, 0) + 1
    return char_count_dict


print(char_count("hello"))
print(char_count("world"))
