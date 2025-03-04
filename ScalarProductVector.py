from typing import List;

def scalar_multiply(matrix: List[List[int|float]], scalar: int|float) -> List[List[int|float]]:
    return [[e * scalar for e in row] for row in matrix];