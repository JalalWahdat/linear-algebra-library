# Final version with visual math steps
def vector_magnitude(v):
    # Calculate the squares, their sum, and the square root
    squares = [x**2 for x in v]
    sum_of_squares = sum(squares)
    result = sum_of_squares ** 0.5
    
    # Format the visual math steps
    step_squares = " + ".join([f"{x}²" for x in v])
    step_values = " + ".join([str(s) for s in squares])
    
    print("\nVECTOR MAGNITUDE (NORM)")
    print(f"||v|| = √({step_squares})")
    print(f"      = √({step_values})")
    print(f"      = √({sum_of_squares})")
    print(f"      = {result}")
    return result


def vector_normalize(v):
    # We reuse the magnitude function to get the divisor
    mag = vector_magnitude(v)
    
    # Prevent division by zero if it is a zero vector
    if mag == 0:
        raise ValueError("Cannot normalize a zero vector.")
        
    result = [x / mag for x in v]
    step = ", ".join([f"({x}/{mag})" for x in v])
    
    print("\nVECTOR NORMALIZATION (UNIT VECTOR)")
    print(f"û = v / ||v||")
    print(f"  = [{', '.join(map(str, v))}] / {mag}")
    print(f"  = [{step}]")
    print(f"  = {result}")
    return result

# ==========================================
# TEST EXECUTION
# ==========================================
v = [3, 4]
vector_normalize(v)
