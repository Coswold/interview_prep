#Q1.7

"""First implementation of the algorithm"""
def rotate_matrix(matrix):
    new_matrix = []
    j = 0
    while j < len(matrix[0]):
        i = 0
        new_row = []
        while i < len(matrix):
            new_row.append(matrix[i][j])
            i += 1
        new_matrix.append(new_row)
        j += 1
    return new_matrix

if __name__ == '__main__':
    matrix = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    print(rotate_matrix(matrix))
