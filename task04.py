def factorial_recursive(n):
    """
    Calculate factorial using recursive approach
    Args:
        n: positive integer
    Returns:
        factorial of n
    """
    # Base case: if n is 0 or 1, return 1
    if n <= 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    """
    Calculate factorial using iterative approach
    Args:
        n: positive integer
    Returns:
        factorial of n
    """
    # Initialize result as 1
    result = 1
    # Multiply numbers from 1 to n
    for i in range(1, n + 1):
        result *= i
    return result

# Get user input
try:
    num = int(input("Enter a positive integer: "))
    if num < 0:
        print("Please enter a positive number")
    else:
        # Calculate and display results using both methods
        print(f"Recursive factorial of {num} is: {factorial_recursive(num)}")
        print(f"Iterative factorial of {num} is: {factorial_iterative(num)}")
except ValueError:
    print("Please enter a valid integer")