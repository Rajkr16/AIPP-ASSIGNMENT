from scipy.optimize import linprog
import numpy as np

# Objective function coefficients (negative because linprog minimizes)
# We want to maximize profit: 6*A + 5*B
# So we minimize: -6*A - 5*B
c = [-6, -5]

# Inequality constraints (A_ub @ x <= b_ub)
# Milk constraint: 1*A + 1*B <= 5
# Choco constraint: 3*A + 2*B <= 12
A_ub = [
    [1, 1],   # Milk constraint
    [3, 2]    # Choco constraint
]
b_ub = [5, 12]

# Bounds for variables (non-negative)
x_bounds = [(0, None), (0, None)]

# Solve the linear programming problem
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=x_bounds, method='highs')

if result.success:
    units_A = result.x[0]
    units_B = result.x[1]
    max_profit = -result.fun
    
    print("Optimization Result:")
    print(f"Units of A to produce: {units_A:.2f}")
    print(f"Units of B to produce: {units_B:.2f}")
    print(f"Maximum Profit: Rs {max_profit:.2f}")
else:
    print("Optimization failed")