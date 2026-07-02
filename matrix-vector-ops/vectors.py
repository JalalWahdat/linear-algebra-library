# ==========================================
# VECTOR OPERATIONS WITH STEPS
# ==========================================

def vector_add(v1, v2):
    # Zip elements to calculate results and format the math steps simultaneously
    result = [a + b for a, b in zip(v1, v2)]
    step = ", ".join([f"({a}+{b})" for a, b in zip(v1, v2)])
    
    print("\nVECTOR ADDITION")
    print("V1 + V2")
    print(f"= {v1} + {v2}")
    print(f"= [{step}]")
    print(f"= {result}")
    return result


def vector_subtract(v1, v2):
    result = [a - b for a, b in zip(v1, v2)]
    step = ", ".join([f"({a}-{b})" for a, b in zip(v1, v2)])
    
    print("\nVECTOR SUBTRACTION")
    print("V1 - V2")
    print(f"= {v1} - {v2}")
    print(f"= [{step}]")
    print(f"= {result}")
    return result


def scalar_multiply(v, k):
    result = [k * x for x in v]
    step = ", ".join([f"({k}×{x})" for x in v])
    
    print("\nSCALAR MULTIPLICATION (VECTOR)")
    print(f"{k}V")
    print(f"= {k}{v}")
    print(f"= [{step}]")
    print(f"= {result}")
    return result


def dot_product(v1, v2):
    products = [a * b for a, b in zip(v1, v2)]
    step = " + ".join([f"({a}×{b})" for a, b in zip(v1, v2)])
    result = sum(products)
    
    print("\nDOT PRODUCT")
    print("V1 • V2")
    print(f"= [{', '.join(map(str, v1))}] • [{', '.join(map(str, v2))}]")
    print(f"= {step}")
    print(f"= {' + '.join(map(str, products))}")
    print(f"= {result}")
    return result


# ==========================================
# EXAMPLE EXECUTION
# ==========================================

v1 = [1, 2, 3]
v2 = [4, 5, 6]
k = 3

# Run Vector Tests
vector_add(v1, v2)
vector_subtract(v1, v2)
scalar_multiply(v1, k)
dot_product(v1, v2)