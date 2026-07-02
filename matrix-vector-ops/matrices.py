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


def matrix_diagonal(matrix):
    # Extracts elements where row index equals column index (i == j)
    result = [matrix[i][i] for i in range(len(matrix))]
    step = [f"A[{i}][{i}]" for i in range(len(matrix))]
    
    print("\nDIAGONAL EXTRACTION")
    print("diag(A)")
    print(f"= Extracting main diagonal from {matrix}")
    print(f"= {step}")
    print(f"= {result}")
    return result


def matrix_trace(matrix):
    # Reuses the diagonal extraction logic, then sums the elements
    diag_elements = [matrix[i][i] for i in range(len(matrix))]
    result = sum(diag_elements)
    step = " + ".join(f"{val}" for val in diag_elements)
    
    print("\nMATRIX TRACE")
    print("tr(A)")
    print(f"= Sum of diagonal elements from {matrix}")
    print(f"= {step}")
    print(f"= {result}")
    return result


def matrix_multiply(A, B):
    # zip(*B) transposes B to cleanly pair its columns with A's rows
    result = [[sum(a * b for a, b in zip(rowA, colB)) for colB in zip(*B)] for rowA in A]
    
    # Formats the exact string math steps for each cell: (a1*b1 + a2*b2)
    step = [[ " + ".join(f"({a}×{b})" for a, b in zip(rowA, colB)) for colB in zip(*B)] for rowA in A]
    
    print("\nMATRIX MULTIPLICATION")
    print("A × B")
    print(f"= {A} ×\n  {B}")
    print(f"= {step}")
    print(f"= {result}")
    return result


# ==========================================
# EXAMPLE EXECUTION
# ==========================================

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
k = 3

# Run Matrix Tests
matrix_add(A, B)
matrix_subtract(A, B)
scalar_multiply_matrix(A, k)
hadamard_product(A, B)
matrix_transpose(A)
matrix_diagonal(A)
matrix_trace(A)
matrix_multiply(A, B)