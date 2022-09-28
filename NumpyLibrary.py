import numpy as np


def InputMatrix():
    print("Введите размер матрицы:")
    size_n, size_m = int(input("n = ")), int(input("m = "))
    matrix = []
    print("Введите матрицу размера", size_n, "х", size_m, ":")
    for i in range(size_n):
        stroka = list(map(int, input().split()))
        while len(stroka) != size_m:
            print("Неверное количество значений!")
            stroka = list(map(int, input().split()))
        matrix.append(stroka)
    return matrix, size_n, size_m


def OutputMatrix(matrix, size_n, size_m):
    for i in range(size_n):
        for j in range(size_m):
            print(matrix[i][j], end=' ')
        print()


matrix1, matrix1Size_n, matrix1Size_m = InputMatrix()

# Транспонирование матриц
npMatrix1 = np.array(matrix1)
npMatrixTrans = npMatrix1.T

print("Транспонированная матрица")
OutputMatrix(npMatrixTrans, matrix1Size_m, matrix1Size_n)

# Ранг матрицы
rang = np.linalg.matrix_rank(npMatrix1)
print("Ранг матрицы:", rang)

# Умножение матриц
matrix2, matrix2Size_n, matrix2Size_m = InputMatrix()

npMatrix2 = np.array(matrix2)
npMatrixMulti = np.dot(npMatrix1, npMatrix2)

print("Результат умножения матриц:")
OutputMatrix(npMatrixMulti, matrix1Size_n, matrix2Size_m)



