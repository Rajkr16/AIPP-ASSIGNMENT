def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.

    The Fibonacci sequence is defined as follows:
    - fib(0) = 0 (base case)
    - fib(1) = 1 (base case)
    - fib(n) = fib(n-1) + fib(n-2) for n > 1

    Args:
        n (int): The position in the Fibonacci sequence to calculate.

    Returns:
        int: The nth Fibonacci number.
    
    The function works by calling itself with the two preceding numbers
    in the sequence until it reaches the base cases (0 or 1).
    """
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    # Base case: if n is 1, return 1
    elif n == 1:
        return 1
    else:
        # Recursive case: return the sum of the two preceding Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage:
# print(fibonacci(5))  # Output: 5