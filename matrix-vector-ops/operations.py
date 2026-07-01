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
# MATRIX OPERATIONS WITH STEPS
# ==========================================

def matrix_add(A, B):
    # Zip rows, then zip elements inside those rows
    result = [[a + b for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]
    step = [[f"({a}+{b})" for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]
    
    print("\nMATRIX ADDITION")
    print("A + B")
    print(f"= {A} +\n  {B}")
    print(f"= {step}")
    print(f"= {result}")
    return result


def matrix_subtract(A, B):
    result = [[a - b for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]
    step = [[f"({a}-{b})" for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]
    
    print("\nMATRIX SUBTRACTION")
    print("A - B")
    print(f"= {A} -\n  {B}")
    print(f"= {step}")
    print(f"= {result}")
    return result


def scalar_multiply_matrix(matrix, scalar):
    result = [[scalar * val for val in row] for row in matrix]
    step = [[f"({scalar}×{val})" for val in row] for row in matrix]
    
    print("\nSCALAR MULTIPLICATION (MATRIX)")
    print(f"{scalar} * A")
    print(f"= {scalar} * {matrix}")
    print(f"= {step}")
    print(f"= {result}")
    return result


def hadamard_product(A, B):
    # Element-wise multiplication using the same zip structure as addition
    result = [[a * b for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]
    step = [[f"({a}×{b})" for a, b in zip(rowA, rowB)] for rowA, rowB in zip(A, B)]
    
    print("\nHADAMARD PRODUCT (ELEMENT-WISE MULTIPLICATION)")
    print("A ∘ B")
    print(f"= {A} ∘\n  {B}")
    print(f"= {step}")
    print(f"= {result}")
    return result


def matrix_transpose(matrix):
    # Uses zip(*matrix) to unpack rows and group elements by their column index
    result = [list(col) for col in zip(*matrix)]
    step = [[f"row_to_col({val})" for val in row] for row in matrix] # Maps how original elements shift
    
    print("\nMATRIX TRANSPOSE")
    print("Aᵀ")
    print(f"= {matrix}ᵀ")
    print(f"= Transposing rows to columns...")
    print(f"= {result}")
    return result


# ==========================================
# EXAMPLE EXECUTION
# ==========================================

v1 = [1, 2, 3]
v2 = [4, 5, 6]
k = 3

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Run Vector Tests
vector_add(v1, v2)
vector_subtract(v1, v2)
scalar_multiply(v1, k)
dot_product(v1, v2)

# Run Matrix Tests
matrix_add(A, B)
matrix_subtract(A, B)
scalar_multiply_matrix(A, k)
hadamard_product(A, B)
matrix_transpose(A)