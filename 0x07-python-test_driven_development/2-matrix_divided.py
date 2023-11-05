#!/urs/bin/python3

    def matrix_divided(matrix, div):
        """Function divides  all the elements by a divisor.

        Args:
            matrix (list of list): Must be a list of list of integers or floats. div(int/float)
        Raises:
            TypeError: if the input is not a list of list of matrix contain row of the same size.
            TypeError: if any element of the matrix is not an integer or float.
            TypeError: if the matrix contains non-numbers
            ZeroDivisionError: If division is 0.
        Return:
            list of lists: New matrix representing the result of the division rounded to 2 decimal places.
            """
            if (not isinstance(matrix, list) or matrix == [] or
                    not all(isinstance(row, list) for row in matrix) or
                    not all((isinstance(ele, int) or isinstance(ele, float))
                        for ele in [num for row in matrix for num in row]))):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if not all(len(row) == len(matrix[0]) for row in matrix):
                raise TypeError("Each row of the matrix must have the same size")
            if not isinstance(div, int) and not isinstance(div, float):
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
            return ([round((num / div, 2), row)) for row in matrix])
