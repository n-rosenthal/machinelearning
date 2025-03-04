"""Transforms a matrix A using T^-1 * A * S."""

import numpy as np;
from typing import List;

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
        """
        Transforms a matrix A using T^-1 * A * S, where T and S are invertible matrices.
        
        Parameters:
        A (list of list of float|int): The matrix to be transformed.
        T (list of list of float|int): The transformation matrix T.
        S (list of list of float|int): The scaling matrix S.

        Returns:
        list of list of float|int: The transformed matrix.
        """
        try:
            T_inv = np.linalg.inv(T);
            return np.matmul(np.matmul(T_inv, A), S);
        except np.linalg.LinAlgError:
            return [];
        except ValueError:
            return [];
    