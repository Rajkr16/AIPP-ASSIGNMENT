class Rectangle:
    """
    A class used to represent a Rectangle.

    Attributes
    ----------
    width : float
        The width of the rectangle (must be non-negative).
    height : float
        The height of the rectangle (must be non-negative).

    Methods
    -------
    area() -> float
        Returns the area of the rectangle (width * height).

    perimeter() -> float
        Returns the perimeter of the rectangle (2 * (width + height)).

    from_input() -> Rectangle
        Creates a Rectangle object by reading width and height from user input.
    """

    def __init__(self, width: float, height: float):
        """
        Initialize the Rectangle with width and height.

        Parameters
        ----------
        width : float
            Width of the rectangle, must be a non-negative number.
        height : float
            Height of the rectangle, must be a non-negative number.

        Raises
        ------
        ValueError
            If width or height is negative.
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative.")
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Calculate the area of the rectangle.

        Returns
        -------
        float
            The computed area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self) -> float:
        """
        Calculate the perimeter of the rectangle.

        Returns
        -------
        float
            The computed perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

    @classmethod
    def from_input(cls):
        """
        Create a Rectangle instance based on user-provided input.

        Returns
        -------
        Rectangle
            A Rectangle object constructed from input values.
        """
        w = float(input("Enter width: ").strip())
        h = float(input("Enter height: ").strip())
        return cls(w, h)


def main():
    """
    Main function to run the Rectangle program.

    Reads width and height from the user, creates a Rectangle object,
    and prints its area and perimeter.
    """
    rect = Rectangle.from_input()
    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")


if __name__ == "__main__":
    main()
