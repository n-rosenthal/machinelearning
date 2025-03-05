"""Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode. The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.
Example:
Input:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode = 'column'

Output:

[4.0, 5.0, 6.0]

Reasoning:

Calculating the mean of each column results in [(1+4+7)/3, (2+5+8)/3, (3+6+9)/3]."""

from typing import List;

def line_mean(matrix: List[List[float]], mode: str) -> List[float]:
    match mode:
        case 'row':
            return [sum(row) / len(row) for row in matrix];
        case 'column':
            return [sum(col[i] for col in matrix) / len(matrix) for i in range(len(matrix[0]))];
        case _:
            return [];
    return [];

