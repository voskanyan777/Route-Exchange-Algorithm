import math
import random
import string

NOISE = string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase
NOISE += 'абвгдезийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789!@#$%^&*()'


def get_start_points(rows: int, columns: int) -> tuple:
    # r_new = ((rows ** (columns ** 0.5))) * (columns ** 2)
    # c_new = ((columns ** (rows ** 0.5))) * (rows ** 2)

    r_new = ((rows ** (columns ** 0.5))) * (columns ** 2)
    c_new = ((columns ** (rows ** 0.5))) * (rows ** 2)

    # r_new = ((rows ** (columns ** 0.5)))
    # c_new = ((columns ** (rows ** 0.5)))

    start_row_point = (math.factorial(rows)) % r_new
    start_column_point = (math.factorial(columns)) % c_new

    return (int(start_row_point), int(start_column_point), (int(r_new), int(c_new)))


def encode(message: str, params: tuple, original_rows: int, original_column: int):
    rows = params[2][0]
    columns = params[2][1]
    matrix = [[0] * columns for _ in range(rows)]
    # for row in matrix:
    #     print(row)

    start_row = params[0]
    start_column = params[1]

    parity = 1
    for i in range(len(matrix)):
        count = 0
        # ищем строку старта в матрице
        if i < start_row - 1:
            continue

        # ищем колонку старта в матрице
        for j in range(len(matrix[i])):
            if j < start_column - 1:
                continue
            # заполняем матрицу нашим сообщением
            if message:
                matrix[i][j] = message[0]
                message = message[1:]
                count += 1
                if count == original_column:
                    parity += 1
                    # if parity % 2 == 0:
                    #     matrix[i][j] = (matrix[i][j])[::-1]

                    break
    # for row in matrix:
    #     print(row)

    # заполняем матрицу шумом
    for column in matrix:
        for i in range(len(column)):
            if column[i] == 0:
                column[i] = random.choice(NOISE)
    # for row in matrix:
    #     print(row)

    # Кодируем сообщение
    encrypted_text = ""

    index = columns - 1
    while index >= 0:
        for i, row in enumerate(matrix):
            encrypted_text += str(row[index])
        index -= 1
    return encrypted_text


def decode(encode_message: str, params: tuple, original_rows: int, original_columns: int):
    rows = params[2][0]
    columns = params[2][1]

    decrypted_text = ""

    decrypted_matrix = [[0] * columns for _ in range(rows)]

    # заполнение зашифрованной матрицы
    # index = columns - 1
    # while index >= 0:
    #     print(f'{index = }')
    #     for row in decrypted_matrix:
    #         row[index] = encode_message[0]
    #         encode_message = encode_message[1:]
    #     index -= 1
    index = 0  # Используем индекс для работы с encode_message
    for col in range(columns - 1, -1, -1):
        for row in decrypted_matrix:
            if index < len(encode_message):
                row[col] = encode_message[index]
                index += 1

    # for row in decrypted_matrix:
    #     print(row)

    start_row = params[0]
    start_column = params[1]

    # расшифровка текста
    parity = 1
    original_matrix = [[0] * original_columns for _ in range(original_rows)]

    for i in range(len(decrypted_matrix)):
        count = 0
        # ищем строку старта в матрице
        if i < start_row - 1:
            continue
        # проверка на то, что мы считали всю оригинальную строку
        if len(decrypted_text) == original_columns * original_rows:
            break
        # ищем колонку старта в матрице
        for j in range(len(decrypted_matrix[i])):
            if j < start_column - 1:
                continue
            count += 1
            decrypted_text += decrypted_matrix[i][j]
            if count == original_columns:
                parity += 1

                break

    return decrypted_text


def original_encode(message: str, rows: int, columns: int):
    matrix = [[0] * columns for _ in range(rows)]

    for index, row in enumerate(matrix):
        for i in range(len(row)):
            row[i] = message[0]
            message = message[1:]
        if (index + 1) % 2 == 0:
            matrix[index] = row[::-1]

    print('до подстановки из словаря')
    for row in matrix:
        print(row)

    # подстановка из словаря

    print('после подстановки из словаря')
    for row in matrix:
        print(row)

    encrypted_text = ""

    index = columns - 1

    while index >= 0:
        for i, row in enumerate(matrix):
            encrypted_text += row[index]
        index -= 1

    return encrypted_text


def original_decode(encode_message: str, rows: int, columns: int):
    decrypted_text = ""


    decrypted_matrix = [[0] * columns for _ in range(rows)]

    # Заполнение матрицы
    for i in range(columns - 1, -1, -1):
        for row in decrypted_matrix:
            row[i] = encode_message[0]
            encode_message = encode_message[1:]

    for row in decrypted_matrix:
        print(row)

    for index, row in enumerate(decrypted_matrix):
        if index % 2 == 0:
            for symbol in row:
                decrypted_text += symbol
        else:
            for symbol in row[::-1]:
                decrypted_text += symbol

    return decrypted_text



