def divide(a, b):
    """
    Divide a by b with error handling for division by zero.
    
    Args:
        a (float): The dividend
        b (float): The divisor
        
    Returns:
        float: The result of a / b
        
    Raises:
        ZeroDivisionError: If b is zero
    """
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
        return None  # Or you could raise the error, or return a special value


# Test the function with division by zero
print(divide(10, 0))

# Test with normal division
print(divide(10, 2))

# Test with another division
print(divide(15, 3))

