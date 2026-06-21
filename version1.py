class Matrix:
    def __init__(self, data):
        self.data = [list(map(float, row)) for row in data]
        self.rows = len(data)
        self.cols = len(data) if self.rows > 0 else 0

    def __repr__(self):
        # Format each number to 2 decimal places for clean step-by-step printing
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
        """Solves A * x = b, prints each step, and returns a 2-decimal rounded solution."""
        print("=== STEP 1: Form the Augmented Matrix [A | b] ===")
        aug = self.augment(b)
        print(aug)
        print("-" * 50)

        M = aug.data
        n = aug.rows

        print("=== STEP 2: Forward Elimination ===")
        for i in range(n):
            print(f"\n--- Processing Pivot Column {i+1} ---")
            
            # Partial Pivoting
            max_row = max(range(i, n), key=lambda r: abs(M[r][i]))
            if abs(M[max_row][i]) < 1e-9:
                raise ValueError("The matrix is singular or has no unique solution.")
            
            if max_row != i:
                print(f"Swap Row {i+1} with Row {max_row+1} (largest pivot value: {M[max_row][i]:.2f})")
                M[i], M[max_row] = M[max_row], M[i]
                print(aug)
            else:
                print(f"Row {i+1} already has the best pivot value: {M[i][i]:.2f}")

            # Eliminate entries below the current pivot
            for j in range(i + 1, n):
                factor = M[j][i] / M[i][i]
                print(f"Row {j+1} = Row {j+1} - ({factor:.4f} * Row {i+1})")
                for k in range(i, n + 1):
                    M[j][k] -= factor * M[i][k]
                print(aug)

        print("-" * 50)
        print("=== STEP 3: Back Substitution ===")
        x = [0.0] * n
        for i in range(n - 1, -1, -1):
            sum_terms = sum(M[i][j] * x[j] for j in range(i + 1, n))
            raw_value = (M[i][n] - sum_terms) / M[i][i]
            
            # Round the finalized variable assignment to 2 decimal places
            x[i] = round(raw_value, 2)
            
            print(f"Calculating Variable x_{i+1}:")
            print(f"  Equation: {M[i][i]:.2f} * x_{i+1} + (sum of knowns: {sum_terms:.2f}) = {M[i][n]:.2f}")
            print(f"  Result: x_{i+1} = {x[i]}")
            
        print("=" * 50)
        return x

# --- Running a Live Test ---
if __name__ == "__main__":
    # Solve:
    # 2x + 1y = 5
    # 1x - 3y = -1
    A = Matrix([[1,3],
                [2, 4]])
    b = [7, 10]
    
    final_solution = A.solve_linear_system(b)
    print(f"\nFinal Solution Package Output: {final_solution}")
