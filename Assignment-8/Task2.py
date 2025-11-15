import unittest
from typing import Union


def assign_grade(score: Union[int, float]) -> str:
    """
    Assigns a letter grade based on numeric score.

    Rules:
    - 90-100: A
    - 80-89: B
    - 70-79: C
    - 60-69: D
    - <60: F

    Validation:
    - score must be int or float
    - score must be within [0, 100]

    Raises:
    - ValueError for invalid input type or out-of-range values
    """
    if not isinstance(score, (int, float)):
        raise ValueError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100 inclusive")

    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


class TestAssignGrade(unittest.TestCase):
    # Boundary tests
    def test_boundary_f(self):
        self.assertEqual(assign_grade(0), "F")
        self.assertEqual(assign_grade(59), "F")
        self.assertEqual(assign_grade(59.99), "F")

    def test_boundary_d(self):
        self.assertEqual(assign_grade(60), "D")
        self.assertEqual(assign_grade(69), "D")
        self.assertEqual(assign_grade(69.99), "D")

    def test_boundary_c(self):
        self.assertEqual(assign_grade(70), "C")
        self.assertEqual(assign_grade(79), "C")
        self.assertEqual(assign_grade(79.99), "C")

    def test_boundary_b(self):
        self.assertEqual(assign_grade(80), "B")
        self.assertEqual(assign_grade(89), "B")
        self.assertEqual(assign_grade(89.99), "B")

    def test_boundary_a(self):
        self.assertEqual(assign_grade(90), "A")
        self.assertEqual(assign_grade(100), "A")

    # Representative internal values
    def test_internal_values(self):
        self.assertEqual(assign_grade(75), "C")
        self.assertEqual(assign_grade(82.5), "B")
        self.assertEqual(assign_grade(95.2), "A")
        self.assertEqual(assign_grade(12.3), "F")
        self.assertEqual(assign_grade( sixty := 60.0 ), "D")

    # Invalid inputs
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            assign_grade(-5)
        with self.assertRaises(ValueError):
            assign_grade(105)
        with self.assertRaises(ValueError):
            assign_grade("eighty")  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            assign_grade(None)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()


