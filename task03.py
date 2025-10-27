# Function to reverse a string
def reverse_string(s: str) -> str:
    """Auto-completed reverse function: returns the reversed string."""
    return s[::-1]

if __name__ == "__main__":
    # Get input from user
    user_input = input("Enter a string to reverse: ")
    # Print the reversed string
    print("Reversed string:", reverse_string(user_input))
    