#!/usr/bin/python3
"""
This function divides all elements of matrix.
"""

def matrix_divided(matrix, div):
    """
    function which divides all  the elements of matrix.

    Args:
        matrix: A list of lists of integers n floats.
        div (int/float): the divisor.

    Raises:
        TypeError: If matrix has non numbers.
        TypeError: If matrix has rows of different sizes.
        TypeError: If div is non-int or non-float.
        ZeroDivisionError: If divisor is 0.

    Returns:
        A new matrix that represents the result.
    """

    # Check whether matrix is  empty, list that should have only integers or floats
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size or different
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check whether divisor is an integer or a float
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    # Check whether divisor is  zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with the results
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    # Return  new matrix
    return new_matrix
