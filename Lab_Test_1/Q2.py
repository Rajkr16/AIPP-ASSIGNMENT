class Rectangle:
    """
    A class to represent a rectangle.
    Attributes:
    ----------
    width : float
        The width of the rectangle (must be non-negative).
    height : float
        The height of the rectangle (must be non-negative).
    Methods:
    -------
    area() -> float:
        Calculates and returns the area of the rectangle.
    perimeter() -> float:
        Calculates and returns the perimeter of the rectangle.
    from_input() -> Rectangle:
        Class method that creates a Rectangle instance from user input.
    Raises:
    -------
    ValueError:
        If width or height is negative during initialization.
    """
    def __init__(self, width: float, height: float):
        # Validate that dimensions are non-negative
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative.")
        # Initialize instance attributes
        self.width = width
        self.height = height

    def area(self) -> float:
        # Calculate area using width * height formula
        return self.width * self.height

    def perimeter(self) -> float:
        # Calculate perimeter using 2 * (width + height) formula
        return 2 * (self.width + self.height)

    @classmethod
    def from_input(cls):
        # Prompt user for width and convert to float
        w = float(input("Enter width: ").strip())
        # Prompt user for height and convert to float
        h = float(input("Enter height: ").strip())
        # Create and return new Rectangle instance
        return cls(w, h)


def main():
    # Create rectangle from user input
    rect = Rectangle.from_input()
    # Display the calculated area
    print(f"Area: {rect.area()}")
    # Display the calculated perimeter
    print(f"Perimeter: {rect.perimeter()}")


# Execute main function only if script is run directly
if __name__ == "__main__":
    main()