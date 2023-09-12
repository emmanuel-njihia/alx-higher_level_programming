#!/usr/bin/python3
""" Pascal's Triangle function."""


def pascal_triangle(n):
    """Pascal's Triangle of size n.
    Return:
    a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        t = triangles[-1]
        tmp = [1]
        for i in range(len(t) - 1):
            tmp.append(t[i] + t[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
