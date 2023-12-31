#!/usr/bin/python3
"""
    pascal triangle
"""

def pascal_triangle(n):
    """
    This function creates a pascal triangle.
    
    Args:
        n (int): The number of rows.
        
    Returns:
        int: triangle.
    """

    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)

            else:
                prev_row = triangle[i - 1]
                value = prev_row[j] + prev_row[j-1]
                row.append(value)
        triangle.append(row)
    return triangle

