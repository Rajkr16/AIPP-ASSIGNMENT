import math
import sys
def _get_positive_float(prompt):
    while True:
        try:
            val = input(prompt).strip()
            if val.lower() in ("q", "quit", "exit"):
                raise KeyboardInterrupt
            num = float(val)
            if num <= 0:
                print("Please enter a positive number.")
                continue
            return num
        except ValueError:
            print("Invalid number. Try again.")
        except KeyboardInterrupt:
            raise


def area_circle(radius):
    return math.pi * radius * radius


def area_rectangle(length, width):
    return length * width


def area_square(side):
    return side * side


def area_triangle(base, height):
    return 0.5 * base * height


def area_trapezoid(a, b, height):
    return 0.5 * (a + b) * height


def area_ellipse(a, b):
    return math.pi * a * b


SHAPES = {
    "1": ("Circle", ("radius",), lambda p: area_circle(p[0])),
    "2": ("Rectangle", ("length", "width"), lambda p: area_rectangle(p[0], p[1])),
    "3": ("Square", ("side",), lambda p: area_square(p[0])),
    "4": ("Triangle", ("base", "height"), lambda p: area_triangle(p[0], p[1])),
    "5": ("Trapezoid", ("a (base1)", "b (base2)", "height"), lambda p: area_trapezoid(p[0], p[1], p[2])),
    "6": ("Ellipse", ("a (semi-major)", "b (semi-minor)"), lambda p: area_ellipse(p[0], p[1])),
}


def user_input_area():
    """
    Interactive loop: user selects a shape and provides dimensions, area is printed.
    Enter 'q' or 'quit' at any prompt to exit.
    """
    try:
        while True:
            print("\nSelect a shape to compute area (enter number). Type 'q' to quit:")
            for key, (name, _, _) in SHAPES.items():
                print(f"  {key}. {name}")
            choice = input("Choice: ").strip().lower()
            if choice in ("q", "quit", "exit"):
                print("Exiting.")
                return
            if choice not in SHAPES:
                print("Invalid choice. Try again.")
                continue

            name, params, calc = SHAPES[choice]
            values = []
            try:
                for p in params:
                    values.append(_get_positive_float(f"Enter {p}: "))
            except KeyboardInterrupt:
                print("\nExiting.")
                return

            result = calc(values)
            print(f"Area of {name}: {result:.6f}")
    except (EOFError, KeyboardInterrupt):
        print("\nExiting.")


if __name__ == "__main__":
    user_input_area()
0