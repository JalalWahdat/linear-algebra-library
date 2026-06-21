class Matrix:
    def __init__(self, mat_1, mat_2):
        self.matrix_1 = mat_1
        self.matrix_2 = mat_2
        self.steps = []

    def add(self):
        result = []

        for row in range(len(self.matrix_1)):
            row_result = []

            for col in range(len(self.matrix_1[row])):
                value = self.matrix_1[row][col] + self.matrix_2[row][col]
                row_result.append(value)

                self.steps.append({
                    "operation": f"A[{row}][{col}] + B[{row}][{col}]",
                    "result": value
                })
            result.append(row_result)
        return result
    def displaySteps(self):
        for step in range(len(self.steps)):
            print(f"Operation {step + 1}: {self.steps[step]["operation"]} Result: {self.steps[step]["result"]}") 
    
mat = Matrix([[1,2], [3,4]], [[5,6], [7,8]])
print(mat.add())
print(mat.displaySteps())