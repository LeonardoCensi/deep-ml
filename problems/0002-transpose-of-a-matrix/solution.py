def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    transposta = []
    colunas = len(a[0])
    linhas = len(a)

    for j in range(colunas):
        coluna_nova = []
        for i in range(linhas):
            coluna_nova.append(a[i][j])
        transposta.append(coluna_nova)
    return transposta

    pass