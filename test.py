import processor

test_matrix = processor.Matrix(3, 3)
test_matrix.add_row([2, -1, 0])
test_matrix.add_row([0, 1, 2])
test_matrix.add_row([1, 1, 0])

answer_matrix = processor.Matrix(3, 3)
answer_matrix.add_row([0.3333, 0, 0.3333])
answer_matrix.add_row([-0.3333, 0, 0.6667])
answer_matrix.add_row([0.1667, 0.5, -0.3333])

assert(processor.get_inverse(test_matrix).matrix == answer_matrix.matrix)