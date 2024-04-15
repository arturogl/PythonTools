def render_pyramid(levels):
    for i in range(levels):
        # Print leading spaces
        print(" " * (levels - i - 1), end="")
        
        # Print asterisks for the current level
        print("*" * (2 * i + 1))

# Test the function with N = 5 levels
render_pyramid(5)
