# Vector Operations

def vector_add(v1, v2):
    return [a + b for a, b in zip(v1, v2)]

def vector_subtract(v1, v2):
    return [a - b for a, b in zip(v1, v2)]

def dot_product(v1, v2):
    return sum(a * b for a, b in zip(v1, v2))


# Matrix Operations

def matrix_add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def matrix_subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]

def scalar_multiply_matrix(matrix, scalar):
    return [[scalar * element for element in row]
            for row in matrix]


# Example Data

v1 = [1, 2, 3]
v2 = [4, 5, 6]

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

scalar = 3

# Vector Results
print("Vector Addition:", vector_add(v1, v2))
print("Vector Subtraction:", vector_subtract(v1, v2))
print("Dot Product:", dot_product(v1, v2))

# Matrix Results
print("\nMatrix Addition:")
for row in matrix_add(A, B):
    print(row)

print("\nMatrix Subtraction:")
for row in matrix_subtract(A, B):
    print(row)

print("\nScalar Multiplication of Matrix:")
for row in scalar_multiply_matrix(A, scalar):
    print(row)