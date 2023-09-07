#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices m_a and m_b.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        list of lists: The result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists, empty, or contains non-integer/float elements.
        ValueError: If m_a and m_b can't be multiplied because of their dimensions.

    Example:
    >>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    [[7, 10], [15, 22]]
    """
    # Your matrix multiplication logic here

if __name__ == '__main__':
    import doctest
    doctest.testmod()
