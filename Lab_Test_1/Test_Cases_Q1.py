# Test cases (listed before function as requested), with justifications:
# 1. n = -10 (negative composite-like) -> not prime; negatives are not prime.
# 2. n = -1 (negative) -> not prime; boundary just below 0.
# 3. n = 0 -> not prime; zero is not prime by definition.
# 4. n = 1 -> not prime; 1 is a classic edge case.
# 5. n = 2 -> prime; smallest prime and only even prime.
# 6. n = 3 -> prime; smallest odd prime.
# 7. n = 4 -> composite; first non-prime >2, even.
# 8. n = 5 -> prime; small odd prime.
# 9. n = 9 -> composite; perfect square of a prime (3*3), tests sqrt boundary.
# 10. n = 25 -> composite; larger perfect square (5*5), tests iteration to sqrt.
# 11. n = 29 -> prime; just above a square (5^2), ensures loop stops correctly.
# 12. n = 97 -> prime; higher prime, checks broader range.
# 13. n = 100 -> composite; larger even number.
# 14. n = 121 -> composite; 11*11, square of a larger prime.
# 15. n = 143 -> composite; semiprime (11*13) non-square, non-trivial factors.
# 16. n = 9973 -> prime; larger prime for performance and correctness.
# 17. n = 9991 -> composite; = 97 * 103 (product of two primes near sqrt range).

def is_prime(n: int) -> bool:
    """Return True if n is a prime number, else False."""
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # Check odd divisors up to sqrt(n)
    limit = int(n ** 0.5)
    for d in range(3, limit + 1, 2):
        if n % d == 0:
            return False
    return True

# Assertions for all test cases:
assert is_prime(-10) is False
assert is_prime(-1) is False
assert is_prime(0) is False
assert is_prime(1) is False
assert is_prime(2) is True
assert is_prime(3) is True
assert is_prime(4) is False
assert is_prime(5) is True
assert is_prime(9) is False
assert is_prime(25) is False
assert is_prime(29) is True
assert is_prime(97) is True
assert is_prime(100) is False
assert is_prime(121) is False
assert is_prime(143) is False
assert is_prime(9973) is True
assert is_prime(9991) is False

# Optional quick sanity prints (can be removed):
if __name__ == "__main__":
    for v in [-10,-1,0,1,2,3,4,5,9,25,29,97,100,121,143,9973,9991]:
        print(v, is_prime(v))