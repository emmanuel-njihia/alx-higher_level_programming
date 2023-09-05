#!/usr/bin/python3

"""This function defines a matrix multiplication ."""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices.
    Args:
        m_a: The first matrix.
        m_b: The second matrix.
    Raises:
        TypeError: If either m_a or m_b consist of non ints/floats.
        TypeError: If either m_a or m_b is empty list.
        TypeError: If either m_a or m_b has different-sizes of rows.
        ValueError: If m_a and m_b can't multiply.
    Returns:
         multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must should be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for r in range(len(m_b[0])):
        new_ro = []
        for c in range(len(m_b)):
            new_ro.append(m_b[c][r])
        inverted_b.append(new_ro)

    new_matrix = []
    for ro in m_a:
        new_ro = []
        for col in inverted_b:
            prod = 0
            for i in range(len(inverted_b[0])):
                prod += ro[i] * col[i]
            new_ro.append(prod)
        new_matrix.append(new_ro)

    return new_matrix
