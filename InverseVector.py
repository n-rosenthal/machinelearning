from typing import List;

def determinant_2(matrix: List[List[int|float]]) -> int|float:
    """The determinant of a 2x2 matrix is computed by the following formula:
    
    det(A) = a11 * a22 - a12 * a21
    
    Parameters
    ----------
    matrix : List[List[int|float]]
        The input matrix A.
    
    Returns
    -------
    int|float
        The determinant of A.
    """
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0];

def adjoint_2(matrix: List[List[int|float]]) -> List[List[int|float]]:
    """The adjoint of a 2x2 matrix is computed by the following formula:
    
    adj(A) = [[a22, -a12], [-a21, a11]]
    
    Parameters
    ----------
    matrix : List[List[int|float]]
        The input matrix A.
    
    Returns
    -------
    List[List[int|float]]
        The adjoint of A.
    """
    return [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]];

def inverse_2(matrix: List[List[int|float]]) -> List[List[int|float]]:
    """The inverse of a 2x2 matrix is computed by the following formula:
    
    (1/det(A)) * adj(A)
    
    provided that det(A) is not 0.
    
    Parameters
    ----------
    matrix : List[List[int|float]]
        The input matrix A.
    
    Returns
    -------
    List[List[int|float]]
        The inverse of A.
    """
    return (1 / determinant_2(matrix)) * adjoint_2(matrix);