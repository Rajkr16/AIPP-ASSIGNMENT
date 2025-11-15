import unittest
import string


def is_sentence_palindrome(sentence: str) -> bool:
    """
    Returns (is_palindrome, cleaned_sentence) where cleaned_sentence removes
    spaces and punctuation and lowercases all letters.
    """
    if not isinstance(sentence, str):
        return False, ""

    allowed = set(string.ascii_letters + string.digits)
    normalized = "".join(ch.lower() for ch in sentence if ch in allowed)
    return normalized == normalized[::-1], normalized


class TestIsSentencePalindrome(unittest.TestCase):
    # Positive examples
    def test_classic_examples(self):
        res, cleaned = is_sentence_palindrome("A man a plan a canal Panama")
        self.assertTrue(res); self.assertEqual(cleaned, "amanaplanacanalpanama")
        res, cleaned = is_sentence_palindrome("No lemon, no melon!")
        self.assertTrue(res); self.assertEqual(cleaned, "nolemonnomelon")
        res, cleaned = is_sentence_palindrome("Was it a car or a cat I saw?")
        self.assertTrue(res); self.assertEqual(cleaned, "wasitacaroracatisaw")
        res, cleaned = is_sentence_palindrome("Able was I, ere I saw Elba")
        self.assertTrue(res); self.assertEqual(cleaned, "ablewasiereisawelba")

    def test_with_mixed_case_and_punctuation(self):
        res, cleaned = is_sentence_palindrome("Madam, I'm Adam.")
        self.assertTrue(res); self.assertEqual(cleaned, "madamimadam")
        res, cleaned = is_sentence_palindrome("Never odd or even")
        self.assertTrue(res); self.assertEqual(cleaned, "neveroddoreven")
        res, cleaned = is_sentence_palindrome("Eva, can I see bees in a cave?")
        self.assertTrue(res); self.assertEqual(cleaned, "evacaniseebeesinacave")

    # Negative examples
    def test_non_palindromes(self):
        res, cleaned = is_sentence_palindrome("Hello, world!")
        self.assertFalse(res); self.assertEqual(cleaned, "helloworld")
        res, cleaned = is_sentence_palindrome("This is not a palindrome")
        self.assertFalse(res); self.assertEqual(cleaned, "thisisnotapalindrome")
        res, cleaned = is_sentence_palindrome("Palindrome")
        self.assertFalse(res); self.assertEqual(cleaned, "palindrome")

    # Edge cases
    def test_edge_cases(self):
        res, cleaned = is_sentence_palindrome("")
        self.assertTrue(res); self.assertEqual(cleaned, "")
        res, cleaned = is_sentence_palindrome(" ,,,   !!! ")
        self.assertTrue(res); self.assertEqual(cleaned, "")
        res, cleaned = is_sentence_palindrome("abc cba")
        self.assertTrue(res); self.assertEqual(cleaned, "abccba")
        res, cleaned = is_sentence_palindrome("abcba!")
        self.assertTrue(res); self.assertEqual(cleaned, "abcba")
        res, cleaned = is_sentence_palindrome(12321)  # type: ignore[arg-type]
        self.assertFalse(res); self.assertEqual(cleaned, "")


if __name__ == "__main__":
    unittest.main()


