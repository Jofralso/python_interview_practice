# 1. Reverse a string
def reverse_string(s):
    return s[::-1]

# 2. Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# 3. Count the number of vowels in a string
def count_vowels(s):
    return sum(1 for char in s if char.lower() in 'aeiou')

# 4. Replace all spaces in a string with underscores
def replace_spaces(s):
    return s.replace(' ', '_')

# 5. Remove all vowels from a string
def remove_vowels(s):
    return ''.join(char for char in s if char.lower() not in 'aeiou')

# 6. Find the longest word in a string
def longest_word(s):
    words = s.split()
    return max(words, key=len)

# 7. Count the number of words in a string
def count_words(s):
    return len(s.split())

# 8. Capitalize the first letter of each word in a string
def capitalize_words(s):
    return s.title()

# 9. Check if a string contains only digits
def is_digit(s):
    return s.isdigit()

# 10. Find all substrings of a string
def substrings(s):
    return [s[i:j+1] for i in range(len(s)) for j in range(i, len(s))]

# 11. Find the first non-repeated character in a string
def first_non_repeated_char(s):
    from collections import Counter
    counts = Counter(s)
    for char in s:
        if counts[char] == 1:
            return char
    return None

# 12. Count the occurrences of each character in a string
def char_occurrences(s):
    from collections import Counter
    return dict(Counter(s))

# 13. Remove duplicate characters from a string
def remove_duplicates(s):
    return ''.join(sorted(set(s), key=s.index))

# 14. Check if two strings are anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# 15. Convert a string to title case
def to_title_case(s):
    return s.title()

# 16. Check if a string is a valid email address
import re
def is_valid_email(s):
    return bool(re.match(r"[^@]+@[^@]+\.[^@]+", s))

# 17. Find the most common character in a string
def most_common_char(s):
    from collections import Counter
    return Counter(s).most_common(1)[0][0]

# 18. Check if a string contains any special characters
def contains_special_chars(s):
    return any(not char.isalnum() for char in s)

# 19. Convert a string to a list of words
def string_to_word_list(s):
    return s.split()

# 20. Join a list of words into a single string
def join_words(word_list):
    return ' '.join(word_list)


# 21. Remove leading and trailing whitespace from a string
def strip_whitespace(s):
    return s.strip()

# 22. Check if a string starts with a specific substring
def starts_with(s, prefix):
    return s.startswith(prefix)

# 23. Check if a string ends with a specific substring
def ends_with(s, suffix):
    return s.endswith(suffix)

# 24. Find the index of the first occurrence of a substring
def find_first_occurrence(s, substring):
    return s.find(substring)

# 25. Find the index of the last occurrence of a substring
def find_last_occurrence(s, substring):
    return s.rfind(substring)

# 26. Split a string into a list of words
def split_into_words(s):
    return s.split()

# 27. Join a list of words into a single string with a specific delimiter
def join_with_delimiter(word_list, delimiter):
    return delimiter.join(word_list)

# 28. Repeat a string n times
def repeat_string(s, n):
    return s * n

# 29. Replace all occurrences of a substring with another substring
def replace_substring(s, old, new):
    return s.replace(old, new)

# 30. Remove all non-alphanumeric characters from a string
def remove_non_alphanumeric(s):
    return ''.join(char for char in s if char.isalnum())

# 31. Check if a string contains any digits
def contains_digits(s):
    return any(char.isdigit() for char in s)

# 32. Count the number of digits in a string
def count_digits(s):
    return sum(1 for char in s if char.isdigit())

# 33. Find the longest palindrome in a string
def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return ""
    longest = s[0]
    for i in range(n):
        for j in range(i, n):
            substr = s[i:j+1]
            if substr == substr[::-1] and len(substr) > len(longest):
                longest = substr
    return longest

# 34. Check if a string is a valid IP address
def is_valid_ip(s):
    import re
    return bool(re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", s))

# 35. Convert a string to lowercase
def to_lowercase(s):
    return s.lower()

# 36. Convert a string to uppercase
def to_uppercase(s):
    return s.upper()

# 37. Swap the case of each character in a string
def swap_case(s):
    return s.swapcase()

# 38. Count the number of uppercase characters in a string
def count_uppercase(s):
    return sum(1 for char in s if char.isupper())

# 39. Count the number of lowercase characters in a string
def count_lowercase(s):
    return sum(1 for char in s if char.islower())

# 40. Check if a string is a valid hexadecimal number
def is_valid_hex(s):
    return bool(re.match(r"^[0-9a-fA-F]+$", s))

# 41. Find the length of the shortest word in a string
def shortest_word_length(s):
    words = s.split()
    return len(min(words, key=len))

# 42. Reverse the order of words in a string
def reverse_words(s):
    return ' '.join(s.split()[::-1])

# 43. Check if a string is a valid URL
def is_valid_url(s):
    import re
    return bool(re.match(r"^(https?|ftp)://[^\s/$.?#].[^\s]*$", s))

# 44. Find the second most common character in a string
def second_most_common_char(s):
    from collections import Counter
    counts = Counter(s).most_common(2)
    return counts[1][0] if len(counts) > 1 else None

# 45. Convert a string to a binary representation
def to_binary(s):
    return ' '.join(format(ord(char), 'b') for char in s)

# 46. Find the longest common prefix among a list of strings
def longest_common_prefix(strings):
    if not strings:
        return ""
    prefix = strings[0]
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

# 47. Check if a string is a valid date (YYYY-MM-DD)
def is_valid_date(s):
    import re
    return bool(re.match(r"^\d{4}-\d{2}-\d{2}$", s))

# 48. Count the number of punctuation characters in a string
def count_punctuation(s):
    import string
    return sum(1 for char in s if char in string.punctuation)

# 49. Check if a string contains balanced parentheses
def is_balanced_parentheses(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

# 50. Convert a string to camelCase
def to_camel_case(s):
    words = s.split()
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])