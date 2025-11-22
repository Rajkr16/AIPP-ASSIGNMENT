# Refactored version using dictionary-based dispatch

def calculate_rectangle_area(length, width):
    """Calculate area of a rectangle."""
    return length * width

def calculate_square_area(side):
    """Calculate area of a square."""
    return side * side

def calculate_circle_area(radius):
    """Calculate area of a circle."""
    return 3.14 * radius * radius

# Dictionary-based dispatch
AREA_CALCULATORS = {
    "rectangle": lambda x, y: calculate_rectangle_area(x, y),
    "square": lambda x, y: calculate_square_area(x),
    "circle": lambda x, y: calculate_circle_area(x)
}

def calculate_area(shape, x, y=0):
    """
    Calculate area based on shape type.
    
    Args:
        shape: Type of shape ('rectangle', 'square', 'circle')
        x: Primary dimension (length/side/radius)
        y: Secondary dimension (width for rectangle, unused for others)
    
    Returns:
        Area of the shape
    
    Raises:
        ValueError: If shape type is not supported
    """
    if shape not in AREA_CALCULATORS:
        raise ValueError(f"Unsupported shape: {shape}")
    
    return AREA_CALCULATORS[shape](x, y)


# Example usage
if __name__ == "__main__":
    print(f"Rectangle (5x3): {calculate_area('rectangle', 5, 3)}")
    print(f"Square (4x4): {calculate_area('square', 4)}")
    print(f"Circle (radius 7): {calculate_area('circle', 7)}")