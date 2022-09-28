def InputMatrix():
    print("Введите размер матрицы:")
    size_n, size_m = int(input("n = ")), int(input("m = "))
    matrix = []
    print("Введите матрицу размера", size_n, "х", size_m, ":")
    for i in range(size_n):
        line = list(map(int, input().split()))
        while len(line) != size_m:
            print("Неверное количество значений!")
            line = list(map(int, input().split()))
        matrix.append(line)
    return matrix, size_n, size_m


def Transposition(matrix, size_n, size_m):
    print("Транспонированная матрица:")
    for i in range(size_m):
        for j in range(size_n):
            print(matrix[j][i], end=' ')
        print()


def Multiplication(M1, M2, size1_n, size1_m, size2_m):
    multiMatrix = []
    for i in range(size1_n):
        lineMultiMatrix = []
        for j in range(size2_m):
            value = 0
            for k in range(size1_m):
                value += M1[i][k] * M2[k][j]
            lineMultiMatrix.append(value)
        multiMatrix.append(lineMultiMatrix)

    # Вывод умноженной матрицы
    print("Результат умножения матриц:")
    for i in range(size1_n):
        for j in range(size2_m):
            print(multiMatrix[i][j], end=' ')
        print()


def Rang(matrix, size_n, size_m):
    for k in range(1, size_n):
        if matrix[k - 1][k - 1] != 0:
            for i in range(k, size_n):
                if matrix[i][k - 1] != 0:
                    value = matrix[i][k - 1]
                    for j in range(size_m):
                        matrix[i][j] = matrix[i][j] * matrix[k - 1][k - 1] - matrix[k - 1][j] * value

    rang = 0
    for i in range(size_n):
        flag = 0
        for j in range(size_m):
            if matrix[i][j] != 0:
                flag = 1
                break
        if flag != 0:
            rang += 1
    print("Ранг матрицы:")
    print(rang)


matrix1, matrix1Size_n, matrix1Size_m = InputMatrix()
Transposition(matrix1, matrix1Size_n, matrix1Size_m)
matrix2, matrix2Size_n, matrix2Size_m = InputMatrix()
Multiplication(matrix1, matrix2, matrix1Size_n, matrix1Size_m, matrix2Size_m)
Rang(matrix1, matrix1Size_n, matrix1Size_m)
