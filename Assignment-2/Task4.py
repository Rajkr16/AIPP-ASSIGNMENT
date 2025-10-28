from typing import List


def sum_of_squares(numbers: List[int]) -> int:
    """Return the sum of squares for a list of integers."""
    total = 0
    for value in numbers:
        total += value * value
    return total


def sum_of_squares_from_input(prompt: str = "Enter integers separated by spaces: ") -> int:
    """Prompt the user for integers and return the sum of their squares.

    The function repeatedly prompts until valid space-separated integers are provided.
    It prints the computed result and also returns it.
    """
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("Please enter at least one integer.")
            continue
        parts = raw.split()
        try:
            values = [int(p) for p in parts]
        except ValueError:
            print("Invalid input. Please enter only integers separated by spaces.")
            continue
        result = sum_of_squares(values)
        print(f"Sum of squares: {result}")
        return result


if __name__ == "__main__":
    sum_of_squares_from_input()


