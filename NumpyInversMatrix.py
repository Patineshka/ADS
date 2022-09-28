import timeit
import numpy as np


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


def OutputMatrix(matrix, size_n, size_m):
    for i in range(size_n):
        for j in range(size_m):
            print(matrix[i][j], end=' ')
        print()


matrix = InputMatrix()
start_time = timeit.default_timer()
martixInv = np.linalg.inv(matrix)

print("Обратная матрица:")
OutputMatrix(martixInv, 3, 3)
print("Время выполнения")
print(timeit.timeit())


