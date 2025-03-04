def kernel(v, u) -> float:
    """
    Linear kernel function.

    This function takes two vectors v and u and returns the dot product of the two vectors.

    Parameters
    ----------
    v : List[float]
        The first vector.
    u : List[float]
        The second vector.

    Returns
    -------
    float
        The dot product of the two vectors.
    """
    return sum(v[i] * u[i] for i in range(len(v)));