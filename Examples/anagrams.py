def anagrams(s1: str, s2: str) -> bool:
    return sorted(s1) == sorted(s2)


print(anagrams("hello", "olleh"))
print(anagrams("hello", "world"))
