import numpy as np;
import math;
import sympy as sp;
import matplotlib.pyplot as plt;

from typing import List, Tuple, Optional, Final, Union;

class Vector:
    def __init__(self, *args, **kwargs):
        if len(args) > 0:
            self.value = np.array(args);
        else:
            self.value = np.array(kwargs['value']);

        self.shape = self.value.shape;
        self.size = self.value.size;
        self.dimensions = self.shape[0];
    
    @property
    def value(self):
        """
        The value of the vector as a numpy array.

        Returns:
        numpy array: The value of the vector.
        """
        return self._value;
    
    @value.setter
    def value(self, value):
        """
        Sets the value of the vector.

        Args:
            value (numpy array): The new value of the vector.

        Returns:
            None
        """
        self._value = value;
        self.shape = self.value.shape;
        self.size = self.value.size;
        self.dimensions = self.shape[0];
        
    def __repr__(self):
        return f"Vector({self.value})";
    
    def __str__(self):
        return f"Vector({self.value})";
    
    def __add__(self, other):
        """
        Adds two vectors together.

        Args:
            other (Vector): The other vector to add.

        Returns:
            Vector: The sum of the two vectors.
        """
        if self.dimensions != other.dimensions:
            raise ValueError("Vectors must have the same dimensions.");
        elif self.shape != other.shape:
            raise ValueError("Vectors must have the same shape.");
        elif self.size != other.size:
            raise ValueError("Vectors must have the same size.");
        return Vector(self.value + other.value);

    def __sub__(self, other):
        """
        Subtracts two vectors.
    
def matrixmul(a: list[list[float]], b: list[list[float]]):
    if len(a[0]) != len(b):
        return -1;
    print(len(a[0]), len(b));
    result : list[list[float]] = [];
    for i in range(len(a)):
        result.append([]);
        for j in range(len(b[0])):
            result[i].append(0);
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j];
    return result if len(result) >= 1 else -1;

if __name__ == '__main__':
    print(matrixmul([[0,0],[2,4],[1,2]],[[0,0,1],[2,4,1],[1,2,3]]))