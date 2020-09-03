main_menu = """
1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit"""

transposition_menu = """
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line"""


class Matrix:
    def __init__(self, x, y):
        self.num_rows = x
        self.num_columns = y
        self.matrix = []
        self.dimensions = f'{str(self.num_rows)} {str(self.num_columns)}'

    def add_row(self, row):
        if len(row) == self.num_columns:
            self.matrix.append(row)
        else:
            print(f"Row incorrect length: {row}")

    def fill_matrix(self, n=''):
        print(f'Enter {n}matrix:')
        for i in range(self.num_rows):
            row = [float(num) if '.' in num else int(num) for num in list(input().split())]
            self.matrix.append(row)



def get_submatrix(matrix, i, j):
    submatrix = Matrix(matrix.num_rows -1, matrix.num_columns - 1)
    submatrix.matrix = [row[:] for row in matrix.matrix]
    submatrix.matrix.pop(i)
    for row in submatrix.matrix:
        row.pop(j)
    return submatrix


def get_determinant(m, total=0):
    if m.num_rows != m.num_columns:
        nope()
    else:
        if m.num_rows == 1:
            return m.matrix[0][0]

        if m.num_rows == 2:
            return m.matrix[0][0] * m.matrix[1][1] - m.matrix[0][1] * m.matrix[1][0]

        else:
            copy_matrix = Matrix(m.num_rows, m.num_columns)
            copy_matrix.matrix = [row[:] for row in m.matrix]

            i = 0
            for j in range(0, copy_matrix.num_columns):
                total += m.matrix[i][j] * (-1) ** (j % 2) * get_determinant(get_submatrix(copy_matrix, i, j))

        return total


def get_inverse(m):
    det = get_determinant(m)
    if det == 0:
        print("This matrix doesn't have an inverse.")
        main()
    else:
        adjunct_step_1 = Matrix(m.num_rows, m.num_columns)
        for i in range(m.num_rows):
            new_row = []
            for j in range(m.num_columns):
                x = (-1) ** (i + j) * get_determinant(get_submatrix(m, i, j))
                new_row.append(x)
            adjunct_step_1.add_row(new_row)

        adjunct = transpose_main_diagonal(adjunct_step_1)

        inverse = matrix_by_constant(adjunct, 1 / det)

        return inverse


def matrix_by_constant(m, const):
    multiplied_matrix = Matrix(m.num_rows, m.num_columns)
    for row in m.matrix:
        new_row = [0 if num * const == 0 else (round(num * const, 4)) for num in row]
        multiplied_matrix.add_row(new_row)
    return multiplied_matrix


def create_matrix(n=''):
    dimensions = input(f'Enter size of {n}matrix: ')
    matrix = Matrix(int(dimensions[0]), int(dimensions[2]))
    matrix.fill_matrix(n)
    return matrix


def matrix_by_matrix(m1, m2):
    if m1.num_columns == m2.num_rows:
        m3 = Matrix(m1.num_rows, m2.num_columns)
        for i in range(len(m1.matrix)):
            new_row = []
            for k in range(len(m2.matrix[0])):
                x = 0
                for j in range(len(m2.matrix)):
                    x += m1.matrix[i][j] * m2.matrix[j][k]
                new_row.append(round(x, 2))
            m3.add_row(new_row)
        return m3
    else:
        nope()


def transpose_main_diagonal(m):
    tm = Matrix(m.num_rows, m.num_columns)
    for i in range(m.num_rows):
        new_row = []
        for k in range(m.num_columns):
            new_row.append(m.matrix[k][i])
        tm.add_row(new_row)
    return tm


def transpose_side_diagonal(m):
    tm = Matrix(m.num_rows, m.num_columns)
    for i in range(1, m.num_rows + 1):
        new_row = []
        for k in range(m.num_columns - 1, -1, -1):
            new_row.append(m.matrix[k][-i])
        tm.add_row(new_row)
    return tm


def transpose_vertical(m):
    tm = Matrix(m.num_rows, m.num_columns)
    for row in m.matrix:
        new_row = []
        for i in range(len(row) - 1, -1, -1):
            new_row.append(row[i])
        tm.add_row(new_row)
    return tm


def transpose_horizontal(m):
    tm = Matrix(m.num_rows, m.num_columns)
    for i in range(m.num_rows - 1, -1, -1):
        tm.add_row(m.matrix[i])
    return tm


def add_two_matrices(m1, m2):
    if m1.dimensions == m2.dimensions:
        m3 = Matrix(m1.num_rows, m1.num_columns)
        for i in range(m1.num_rows):
            new_row = []
            for j in range(m1.num_columns):
                new_row.append(m1.matrix[i][j] + m2.matrix[i][j])
            m3.add_row(new_row)
        return m3
    else:
        nope()


def transpose():
    print(transposition_menu)
    transposition = input("Your choice: ")

    new_matrix = create_matrix()

    if transposition == '1':
        print_matrix(transpose_main_diagonal(new_matrix))

    elif transposition == '2':
        print_matrix(transpose_side_diagonal(new_matrix))

    elif transposition == '3':
        print_matrix(transpose_vertical(new_matrix))

    elif transposition == '4':
        print_matrix(transpose_horizontal(new_matrix))


def print_matrix(m):
    print("The result is:")

    printable_matrix = Matrix(m.num_rows, m.num_columns)
    for row in m.matrix:
        new_row =[str(num).rjust(8) for num in row]
        printable_matrix.add_row(new_row)

    for row in printable_matrix.matrix:
        print(*row)



def nope():
    print("The operation cannot be performed.")
    main()


def main():
    while True:
        print(main_menu)
        choice = input("Your choice: ")

        if choice == '1':
            first_matrix = create_matrix('first ')
            second_matrix = create_matrix('second ')
            print_matrix(add_two_matrices(first_matrix, second_matrix))

        elif choice == '2':
            new_matrix = create_matrix()
            const = int(input("Enter constant: "))
            print_matrix(matrix_by_constant(new_matrix, const))

        elif choice == '3':
            first_matrix = create_matrix('first ')
            second_matrix = create_matrix('second ')
            print_matrix(matrix_by_matrix(first_matrix, second_matrix))

        elif choice == '4':
            transpose()

        elif choice == '5':
            matrix = create_matrix()
            print(get_determinant(matrix))

        elif choice == '6':
            matrix = create_matrix()
            print_matrix(get_inverse(matrix))


        elif choice == '0':
            exit()

        else:
            print("Invalid choice. Please try again.")
# main()
