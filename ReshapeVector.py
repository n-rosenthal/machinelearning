import numpy as np;

def reshape_matrix(a: list[list[float|int]], new_shape: tuple[int, int]) -> list[list[float|int]]:
    """
    Reshape a 2D matrix to the specified new shape.

    Parameters:
    a (list of list of float|int): The input matrix to be reshaped.
    new_shape (tuple of int, int): The desired shape for the output matrix.

    Returns:
    list of list of float|int: The reshaped matrix.

    Raises:
    ValueError: If the total number of elements in the input matrix does not match
                the product of the dimensions in the new shape.
    """
    return np.reshape(a, new_shape).tolist();
