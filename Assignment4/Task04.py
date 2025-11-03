def count_vowels(s: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in the given string (case-insensitive)."""
    vowels = set("aeiou")
    return sum(1 for ch in s.lower() if ch in vowels)

if __name__ == "__main__":
    text = input("Enter a string: ")
    print("number of vowel-",count_vowels(text))


