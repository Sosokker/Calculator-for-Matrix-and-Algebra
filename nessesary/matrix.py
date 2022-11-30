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

    def __mul__(self, other):
        """
        Multiply matrix up and those matrix need same dimesional.
        >>> m1 = Matrix([[1, 2], [3, 4]])
        >>> m2 = Matrix([[1, 2], [3, 4]])
        >>> m3 = m1 * m2
        >>> m3.array
        [[7, 10], [15, 22]]
        """
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

    def determinant(self):
        """
        Find determinant of Square Matrix
        >>> m1 = Matrix([[1,2,3],[1,2,3],[1,2,3]])
        >>> d = m1.determinant()
        >>> d
        0
        """
        if self.row != self.column:
            raise ValueError(f"Can't Find determinant of {self.row} x {self.column} Matrix")

        if self.row == 2 and self.column == 2:
            return self.array[0][0] * self.array[1][1] - self.array[1][0] * self.array[0][1]

        # value = 0
        # index_cut_column = [range(self.row)]

        # for column_to_cut in index_cut_column:
        #     temp_matrix = self.copy_matrix()
        #     temp_matrix.array = temp_matrix.array[1:]
        #     row_count = len(temp_matrix.array)

        #     for row_index in range(row_count):
        #         temp_matrix.array[row_index] = temp_matrix.array[row_index][0:column_to_cut] + temp_matrix.array[row_index][column_to_cut+1:]

        #     coeff_sign = (-1) ** (column_to_cut % 2)
        #     sub_determinant = temp_matrix.determinant()
        #     value = coeff_sign * self.array[0][column_to_cut] * sub_determinant
        value = 0
        for x in range(0, self.row):

            i = 0
            j = x
            
            sum_mul = 1
            for y in range(0, self.row):
                sum_mul *= self.array[i][j]
                i += 1
                j += 1
                if (j >= self.row):
                    j = 0

            value += sum_mul

        sum_sub = 0
        for x in range(0, self.row):
            
            i = 0
            j = self.row - 1 - x
            
            sum_mul = 1
            for y in range(0, self.row):
                sum_mul *= self.array[i][j]
                i += 1
                j -= 1
                if (j < 0):
                    j = self.row - 1
            sum_sub -= sum_mul

        determinant = value + sum_sub
        return determinant

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
        pass

    def __str__(self):
       return f'Matrix({self.array})'

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # Use the following line INSTEAD if you want to print all tests anyway.
    # doctest.testmod(verbose = True)


m1 = Matrix([[1,1,1],[2,2,2],[3,3,3]])
d = m1.determinant()
print(d)