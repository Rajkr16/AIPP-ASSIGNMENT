def f(x):
    return 2*x**3 + 4*x + 5

def derivative(x):
    # f'(x) = 6x^2 + 4
    return 6*(x**2) + 4

# Check if derivative can be zero (solve 6x^2 + 4 = 0)
a, b, c = 6, 0, 4  # for ax^2 + bx + c
discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("No real value of x where f'(x) = 0.")
    print("So f(x) is strictly increasing and has no finite minimum (in real numbers).")
else:
    # (This block won't run for this function, but shown for completeness)
    import math
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("Critical points:", x1, x2)
