def sum_diag(matrix):
    result = []

    for i in range(len(matrix)):
        suma = 0
        for j in range(len(matrix[i])):
            if i != j:
                suma += matrix[i][j]

        result.append(suma == matrix[i][i])
        # if suma == matrix[i][i]:
        #     result.append(True)
        # else:
        #     result.append(False)

    return result


def max_line_file(filename):
    f = open(filename, 'r')

    result = []

    for line in f:
        words = line.split(' ')

        max_length = 0
        max_word = ''

        for word in words:
            word = word.strip()

            if len(word) > max_length:
                max_word, max_length = word, len(word)

        result.append(max_length)

    f.close()
    return result


def is_palindrom(word):
    return word == word[::-1]


def find_count(filename, word):
        f = open(filename, 'r')
        count = 0

        for line in f:
            words = line.split(' ')

            for w in words:
                if word == w.strip():
                    count += 1

        f.close()
        return count


def count_pali(filename):
    f = open(filename, 'r')
    result = {}

    for line in f:
        words = line.split(' ')

        for word in words:
            if is_palindrom(word):
                result[word] = find_count(filename, word.strip())
    
    f.close()
    return result


def perfect(numar):
    suma = 0

    for i in range(1, (numar // 2) + 1):
        if numar % i == 0:
            suma += i

    return numar == suma


def suma_coloane(matrix, j):
    suma = 0

    for i in range(len(matrix)):
        suma += matrix[i][j]

    return suma


def summe_spalte_perfect(matrix):
    for i in range(len(matrix)):
        suma = suma_coloane(matrix, i)

        if perfect(suma) == False:
            return False

    return True


def matrix_continua(matrix):
    i = 0

    while i < len(matrix):
        j = 1

        while j < len(matrix):
            if i % 2 == 0:
                if matrix[i][j] < matrix[i][j - 1]:
                    return False
                j += 1
            else:
                if matrix[i][j - 1] < matrix[i][j]:
                    return False
                j -= 1



def test_matrix_continua():
    assert matrix_continua([
        [1, 2, 3],
        [6, 5, 4],
        [7, 8, 9]
    ]) == True


def test_count_pali():
    assert count_pali('data2.input') == {'anna': 2, 'abbcbba': 1, 'abba': 2}


def test_max_line_file():
    assert max_line_file('data.input') == [4, 4]


def test_sum_diag():
    assert sum_diag([
        [4, 3, 1],
        [1, 2, 1],
        [0, 5, 1]
         ]
        ) == [True, True, False]


def test_summe_spalte_perfect():
    assert summe_spalte_perfect([
        [4, 3, 10],
        [1, 2, 10],
        [1, 1, 8]
    ]) == True

def main():
    pass


test_count_pali()
test_max_line_file()
test_sum_diag()
test_summe_spalte_perfect()
test_matrix_continua()
main()

