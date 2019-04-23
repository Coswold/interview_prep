# Q1.8

"""First implementation: O(n*m)"""
def zero_matrix(m):
    col = []
    row = []
    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            if m[i][j] == 0:
                row.append(i)
                col.append(j)
            j += 1
        i += 1

    i = 0
    while i < len(m):
        j = 0
        while j < len(m[i]):
            if j in col or i in row:
                m[i][j] = 0
            j += 1
        i += 1

    return m

if __name__ == '__main__':
    matrix = [
    [0, 2, 3],
    [1, 2, 3],
    [1, 2, 3]]
    print(zero_matrix(matrix))
