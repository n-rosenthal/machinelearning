from typing import List
from numpy import linalg as la
import numpy as np

def eigenvalues(matrix: List[List[int|float]]) -> List[int|float]:
    return la.eig(matrix)[0];
