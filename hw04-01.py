# 1. Напишите функцию для транспонирования матрицы

def transpose_matrix(input_m: list[list]) -> list[list]:
    result = [
        [input_m[j][i] for j in range(len(input_m))] for i in
        range(len(input_m[0]))
    ]
    return result


matrix = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11]
]

print(transpose_matrix(matrix))
