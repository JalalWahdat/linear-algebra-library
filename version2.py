class Matrix:
    def __init__(self, data):
        self.data = [list(map(float, row)) for row in data]
        self.rows = len(data)
        self.cols = len(data) if self.rows > 0 else 0

    def __repr__(self):
        lines = []
        for row in self.data:
            formatted_row = [f"{val:>.2f}" for val in row]
            lines.append("  [ " + ", ".join(formatted_row) + " ]")
        return "\n".join(lines)

    def augment(self, vector):
        """Appends a column vector to the matrix."""
        if len(vector) != self.rows:
            raise ValueError("Vector length must match the number of rows.")
        new_data = [self.data[i] + [float(vector[i])] for i in range(self.rows)]
        return Matrix(new_data)

    def solve_linear_system(self, b):
        """Transforms matrix to strict REF (pivots = 1) and solves via back-substitution."""
        print("=== STEP 1: Form the Augmented Matrix [A | b] ===")
        aug = self.augment(b)
        print(aug)
        print("-" * 60)

        M = aug.data
        n = aug.rows

        print("=== STEP 2: Convert to Strict Row Echelon Form (REF) ===")
        for i in range(n):
            print(f"\n--- Processing Row {i+1} ---")
            
            # 1. Partial Pivoting (Find largest absolute value in column below current row)
            max_row = max(range(i, n), key=lambda r: abs(M[r][i]))
            if abs(M[max_row][i]) < 1e-9:
                raise ValueError("The matrix is singular or has no unique solution.")
            
            if max_row != i:
                print(f"Swap Row {i+1} with Row {max_row+1} for numerical stability.")
                M[i], M[max_row] = M[max_row], M[i]
                print(aug)

            # 2. Force the Pivot to be exactly 1 (Scale the current row)
            pivot = M[i][i]
            if pivot != 1.0:
                print(f"Divide Row {i+1} by its pivot ({pivot:.2f}) to make the pivot 1:")
                M[i] = [val / pivot for val in M[i]]
                print(aug)

            # 3. Eliminate entries below the current pivot
            for j in range(i + 1, n):
                factor = M[j][i]
                if abs(factor) > 1e-9: # Only eliminate if it's not already 0
                    print(f"Eliminate lower entry in Row {j+1}: Row {j+1} = Row {j+1} - ({factor:.4f} * Row {i+1})")
                    for k in range(i, n + 1):
                        M[j][k] -= factor * M[i][k]
                    print(aug)

        print("-" * 60)
        print("=== STEP 3: Back Substitution (Solving for Variables) ===")
        x = [0.0] * n
        
        # Since all pivots on the diagonal are now 1, the division by M[i][i] is simplified
        for i in range(n - 1, -1, -1):
            sum_terms = sum(M[i][j] * x[j] for j in range(i + 1, n))
            raw_value = M[i][n] - sum_terms
            
            # Round the final variable answer to 2 decimal places
            x[i] = round(raw_value, 2)
            
            print(f"Calculating Variable x_{i+1}:")
            print(f"  Equation: 1.00 * x_{i+1} + {sum_terms:.2f} = {M[i][n]:.2f}")
            print(f"  Result: x_{i+1} = {x[i]}")
            
        print("=" * 60)
        return x

# --- Testing the Strict REF Solver ---
if __name__ == "__main__":
    # Solve:
    # 2x + 4y = 10
    # 1x - 3y = -5
    A = Matrix([[2,4],
                [1, 3]])
    b = [10, -5]
    
    final_solution = A.solve_linear_system(b)
    print(f"\nFinal Solution Package Output: {final_solution}")
