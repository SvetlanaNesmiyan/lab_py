import numpy as np

def shift_matrix(matrix1, shift_amount, mode='right'):
    matrix = np.array(matrix1)
    rows, cols = matrix.shape

    if mode == 'right':
        shift_amount = shift_amount % cols
        return np.array([np.concatenate((row[-shift_amount:], row[:-shift_amount])) for row in matrix])
    elif mode == 'down':
        shift_amount = shift_amount % rows
        return np.vstack([matrix[-shift_amount:], matrix[:-shift_amount]])
    else:
        raise ValueError("Incorrect mode! Use 'right' or 'down'.")