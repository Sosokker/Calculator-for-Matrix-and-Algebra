class Matrix:
    """
    We will write matrix in form of nd-array 

    Example:
    - [[1, 2], [3, 4]] is a 2x2 Matrix (row x column)
    - [[1, 2]] is 1x2 Matrix
    """
    
    def __init__(self, array: list):
        self.array = array
        self.row = len(array)
        self.column = len(array[0])
        
    def __add__(self, other):
        """
        Add matrix up and those matrix need same dimesional.
        >>> m1 = Matrix([[1, 2], [3, 4]])
        >>> m2 = Matrix([[1, 2], [3, 4]])
        >>> m3 = m1 + m2
        >>> m3.array
        [[2, 4], [6, 8]]
        """

        if (self.row != other.row) and (self.column != other.column):
            raise ValueError("Need matrix with same dimesional when add matrix up.")
        for row_index in range(self.row):
            for column_index in range(self.column):
                self.array[row_index][column_index] += other.array[row_index][column_index]
        return self

    def __sub__(self, other):
        """
        Substract matrix up and those matrix need same dimesional.
        >>> m1 = Matrix([[1, 2], [3, 4]])
        >>> m2 = Matrix([[1, 2], [3, 4]])
        >>> m3 = m1 - m2
        >>> m3.array
        [[0, 0], [0, 0]]
        """

        if (self.row != other.row) and (self.column != other.column):
            raise ValueError("Need matrix with same dimesional when add matrix up.")
        for row_index in range(self.row):
            for column_index in range(self.column):
                self.array[row_index][column_index] -= other.array[row_index][column_index]
        return self

    def __mul__(self, other: "int | float"):
        """
        Multiply matrix up and those matrix need same dimesional.
        >>> m1 = Matrix([[1, 2], [3, 4]])
        >>> m2 = Matrix([[1, 2], [3, 4]])
        >>> m3 = m1 * m2
        >>> m3.array
        [[7, 10], [15, 22]]
        >>> m1 = Matrix([[1, 2], [3, 4]])
        >>> m2 = 2
        >>> m4 = m1 * m2
        >>> m4.array
        [[2, 4], [6, 8]]
        """
        if isinstance(other, int) or isinstance(other, float):
            for row in range(self.row):
                for col in range(self.column):
                    self.array[row][col] = self.array[row][col] * other
            return self
        else:
            if  self.column == other.row:
                new_matrix = Matrix([[0 for i in range(other.column)] for k in range(self.row)])
                for row_index in range(self.row): 
                    for col_index in range(self.column):
                        for k in range(other.row):
                            new_matrix.array[row_index][col_index] += self.array[row_index][k] * other.array[k][col_index]
                return new_matrix
            else:
                raise ValueError("Can't multiply these matrix")

    def copy_matrix(self):
        """
        >>> m = Matrix([[1,2]])
        >>> m2 = m.copy_matrix()
        >>> m2 is m
        False
        """
        arr = self.array
        new_matrix = Matrix(arr)
        return new_matrix

    def new_matrix(a,i):#FUNCTION TO FIND THE NEW MATRIX
        arr = a.copy_matrix() 
        if len(arr) == 2:
            
            return arr
        else:
            arr.pop(0)
            for j in arr:
                j.pop(i)
                
            return arr

    def determinant(self):
        """
        Using Cofactor Expanion.
        |M| = sum[M(1,i)*Cofactor(M(1,i)) from i = 1 to n]

        Find determinant of Square Matrix
        >>> m1 = Matrix([[1,2,3],[1,2,3],[1,2,3]])
        >>> m1.determinant()
        0
        >>> m2 = Matrix([[13212,1,3,8321],[27,2,4,6],[321,5,2,-14],[312,21,211,3]])
        >>> m2.determinant()
        858575226
        """
        if self.row != self.column:
            raise ValueError(f"Can't Find determinant of {self.row} x {self.column} Matrix")

        if len(self.array) == 2 and len(self.array[0]) == 2:
            return self.array[0][0] * self.array[1][1] - self.array[1][0] * self.array[0][1]

        det = 0
        for col in range(len(self.array)):
            temp = self.copy_matrix()
            minor = lambda i, j : [row[:j] + row[j+1:] for row in (temp.array[:i]+temp.array[i+1:])]
            temp.array = minor(0,col)
            det += ((-1)**col)*self.array[0][col]*temp.determinant()
        return det

    def tranpose(self):
        """
        Substract matrix up and those matrix need same dimesional.
        >>> m1 = Matrix([[1, 2, 3], [3, 4, 5]])
        >>> m1 = m1.tranpose()
        >>> m1.array
        [[1, 3], [2, 4], [3, 5]]
        """
        new_matrix = Matrix([[0 for i in range(self.row)] for k in range(self.column)])
        for row_index in range(self.row):
            for col_index in range(self.column):
                new_matrix.array[col_index][row_index] += self.array[row_index][col_index]
        return new_matrix

    def inverse(self):
        """
        Find Inverse Matrix.
        >>> m1 = Matrix([[4, 3],[3, 2]])
        >>> m1.inverse().array
        [[-2.0, 3.0], [3.0, -4.0]]
        >>> m1 = Matrix([[3, 0, 2],[2, 0, -2],[0, 1, 1]])
        >>> m1.inverse().array
        [[0.2, 0.2, 0.0],[-0.2, 0.3, 1.0],[0.2, -0.3, 0.0]]
        """
        n = len(self.array)
        A = [row[:] + [int(i == j) for j in range(n)] for i, row in enumerate(self.array)]
        for i in range(n):
            pivot = max(range(i, n), key=lambda j: abs(A[j][i]))
            A[i], A[pivot] = A[pivot], A[i]
            pivot_val = A[i][i]
            for j in range(i, 2 * n):
                A[i][j] /= pivot_val
            for j in range(n):
                if i != j:
                    cur_val = A[j][i]
                    for k in range(i, 2 * n):
                        A[j][k] -= cur_val * A[i][k]

        return [[round(val, 5) for val in row[n:]] for row in A]

    def __str__(self):
       return f'Matrix({self.array})'

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # Use the following line INSTEAD if you want to print all tests anyway.
    # doctest.testmod(verbose = True)


    # def inverse_matrix(A):
    # # Create the identity matrix
    # I = [[0] * len(A) for i in range(len(A))]
    # for i in range(len(I)):
    #     I[i][i] = 1
    # # Create the augmented matrix
    # M = [A[i] + I[i] for i in range(len(A))]
    # # Perform row operations until the matrix is in reduced row echelon form
    # for i in range(len(A)):
    #     # Find the row with the largest pivot
    #     pivot = max(range(i, len(A)), key=lambda k: abs(M[k][i]))
    #     # Swap the pivot row with the current row
    #     M[i], M[pivot] = M[pivot], M[i]
    #     # Divide the current row by the pivot element
    #     M[i] = [M[i][j] / M[i][i] for j in range(len(A) * 2)]
    #     # Subtract the current row from all other rows to eliminate the pivot column
    #     for j in range(len(A)):
    #         if i != j:
    #             M[j] = [M[j][k] - M[i][k] * M[j][i] for k in range(len(A) * 2)]
    # # The inverse matrix is the right half of the reduced row echelon form
    # return [[M[i][j] for j in range(len(A), len(A) * 2)] for i in range(len(A))]