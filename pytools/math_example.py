import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check if the discriminant is negative (no real roots)
    if discriminant < 0:
        return None  # No real roots
    
    # Calculate the two roots
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    return root1, root2

# Example usage
a = 5
b = 63
c = 1
roots = solve_quadratic(a, b, c)
if roots:
    print("Root 1:", roots[0])
    print("Root 2:", roots[1])
else:
    print("No real roots")
