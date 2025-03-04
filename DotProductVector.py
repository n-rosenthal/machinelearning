from typing import List

def dot_product(a: List[List[int|float]], b: List[int|float]) -> List[List[int|float]]:
    if len(a) != len(b):
        return -1;
    A : List[List[int|float]] = a.copy();
    v : List[int|float] = b.copy();
    B : List[List[int|float]] = [];
    
    for i in range(len(A)):
        B.append([]);
        for j in range(1):
            B[i].append(0);
            for k in range(len(v)):
                B[i][j] += A[i][k] * v[k];
    return B;


if __name__ == "__main__":
    print(dot_product([[1, 2, 3], [2, 4, 5], [6, 8, 9]], [1, 2, 3]))