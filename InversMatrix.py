import timeit


def InputMatrix():
    M = []
    print("Введите матрицу размера 3х3:")
    for i in range(3):
        line = list(map(int, input().split()))
        while len(line) != 3:
            print("Неверное количество значений!")
            line = list(map(int, input().split()))
        M.append(line)
    return M


def Determinant(M):
    det = ((M[0][0] * M[1][1] * M[2][2]) + (M[0][1] * M[1][2] * M[2][0]) + (M[0][2] * M[1][0] * M[2][1]) -
           (M[0][2] * M[1][1] * M[2][0]) - (M[0][1] * M[1][0] * M[2][2]) - (M[0][0] * M[1][2] * M[2][1]))
    if det == 0:
        print("Определитель равен нулю => обратной матрицы не существует")
        exit()
    return det


def AlgAdd(M, x, y):
    i_min, i_max, j_min, j_max = 0, 0, 0, 0
    for i in range(3):
        if i != x:
            i_min = i_max
            i_max = i
    for j in range(2, -1, -1):
        if j != y:
            j_max = j_min
            j_min = j
    return M[i_min][j_min] * M[i_max][j_max] - M[i_min][j_max] * M[i_max][j_min]


def InversMatrix(M):
    det = Determinant(M)
    martixOfAlgebAdd = []
    for i in range(3):
        line = []
        for j in range(3):
            line.append(AlgAdd(M, i, j) * (-1) ** (i + j) * det ** (-1))
        martixOfAlgebAdd.append(line)

    print("Обратная матрица:")
    for i in range(3):
        for j in range(3):
            print(martixOfAlgebAdd[j][i], end=' ')
        print()


matrix = InputMatrix()
start_time = timeit.default_timer()
InversMatrix(matrix)

print("Время выполнения")
print(timeit.timeit())
