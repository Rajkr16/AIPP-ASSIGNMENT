import re
import unittest


def is_valid_email(email: str) -> bool:
    """
    Validates an email string based on the given requirements:
    - Must contain exactly one '@' and at least one '.' in the domain part.
    - Must not start or end with special characters (must start and end with an alphanumeric).
    - Should not allow multiple '@' characters.
    """
    if not isinstance(email, str) or not email:
        return False

    # Quick checks for start/end characters and single '@'
    if not (email[0].isalnum() and email[-1].isalnum()):
        return False
    if email.count("@") != 1:
        return False

    local, domain = email.split("@", 1)

    # Domain must contain at least one dot
    if "." not in domain:
        return False

    # Define allowed characters for local and domain parts (common but simplified)
    allowed_local = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._%+\-]*$")
    allowed_domain = re.compile(r"^[A-Za-z0-9][A-Za-z0-9.\-]*[A-Za-z0-9]$")

    if not allowed_local.match(local):
        return False
    if not allowed_domain.match(domain):
        return False

    return True


class TestIsValidEmail(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(is_valid_email("user@example.com"))
        self.assertTrue(is_valid_email("u.ser-name+tag@sub.domain.com"))
        self.assertTrue(is_valid_email("User123@exa-mple.co"))

    def test_invalid_missing_at(self):
        self.assertFalse(is_valid_email("user.example.com"))
        self.assertFalse(is_valid_email("userexample.com"))

    def test_invalid_multiple_at(self):
        self.assertFalse(is_valid_email("user@@example.com"))
        self.assertFalse(is_valid_email("u@ser@ex.com"))

    def test_invalid_start_or_end_with_special(self):
        self.assertFalse(is_valid_email(".user@example.com"))
        self.assertFalse(is_valid_email("_user@example.com"))
        self.assertFalse(is_valid_email("-user@example.com"))
        self.assertFalse(is_valid_email("+user@example.com"))
        self.assertFalse(is_valid_email("user@example.com."))
        self.assertFalse(is_valid_email("user@example.com-"))
        self.assertFalse(is_valid_email("user@example.com_"))

    def test_invalid_no_dot_in_domain(self):
        self.assertFalse(is_valid_email("user@examplecom"))
        self.assertFalse(is_valid_email("user@localhost"))

    def test_edge_cases(self):
        self.assertFalse(is_valid_email(""))
        self.assertFalse(is_valid_email(" "))
        self.assertFalse(is_valid_email("@."))
        self.assertFalse(is_valid_email("a@b"))  # no dot in domain


if __name__ == "__main__":
    unittest.main()  # Run tests when executed directly


