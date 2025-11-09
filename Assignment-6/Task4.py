def sum_to_n_for(n):
    """
    Calculate sum of first n numbers using for loop.
    
    Args:
        n (int): The number of terms to sum
        
    Returns:
        int: Sum of first n numbers (1 + 2 + 3 + ... + n)
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def sum_to_n_while(n):
    """
    Calculate sum of first n numbers using while loop.
    
    Args:
        n (int): The number of terms to sum
        
    Returns:
        int: Sum of first n numbers (1 + 2 + 3 + ... + n)
    """
    total = 0
    i = 1
    while i <= n:
        total += i
        i += 1
    return total


def sum_to_n(n, loop_type='for'):
    """
    Calculate sum of first n numbers using specified loop type.
    
    Args:
        n (int): The number of terms to sum
        loop_type (str): 'for' or 'while' to specify loop type
        
    Returns:
        int: Sum of first n numbers (1 + 2 + 3 + ... + n)
    """
    if loop_type == 'for':
        return sum_to_n_for(n)
    elif loop_type == 'while':
        return sum_to_n_while(n)
    else:
        raise ValueError("loop_type must be 'for' or 'while'")


if __name__ == "__main__":
    # Get user input
    try:
        n = int(input("Enter a positive integer n: "))
        
        if n < 1:
            print("Please enter a positive integer!")
        else:
            # Calculate using for loop
            result_for = sum_to_n(n, 'for')
            print(f"\nSum of first {n} numbers (using for loop): {result_for}")
            
            # Calculate using while loop
            result_while = sum_to_n(n, 'while')
            print(f"Sum of first {n} numbers (using while loop): {result_while}")
            
            # Verify both methods give same result
            if result_for == result_while:
                print(f"\nBoth methods give the same result: {result_for}")
            
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

