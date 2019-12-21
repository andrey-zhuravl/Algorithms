# ==================================================
#
#   Lection 12.
#   Подсчет минимального количества посимвольных исправлений, необходимых для
#   приведения исходной строки к аналогичному виду другой строки, используя 
#   такие допустимые виды исправлений, как вставка, замена и удаление.
#
#   asymptotics: O(N*M)
#
# ==================================================

""" 
    суть алгоритма - вычисление минимального количества элементарных манипуляций (редакционных правок), которые требуется выполнить 
    с текущим (i-ым) символом подпоследовательности (подстроки) размером [0:i] исходной последовательности (строки)
    на текущем (i-ом) проходе внешнего цикла для приведения его к виду эталонного текущего (j-го) символа текущей подстроки 
    размером [0:j] эталонной строки, выбранного на j-м проходе вложенного цикла, в зависимости от степени равенства друг другу
    последних (рассматриваемых в данный момент на текущих проходах циклов) символов соответствующих подстрок, с последовательным использованием
    уже известных (либо заданных изначально, либо вычисленных в процессе) значений предыдущих соседних позиций слева, сверху и слева-сверху, 
    с получением значения в последней позиции последней строки в качестве конечного результата  """

def levensteinLenght(A, B):

    """
    Второстепенная часть. Генератор подготавливает двумерный список размером M на N
    со значениями, равными i в строке j=0, равными j в столбце i=0 и нулевыми элементами в остальных позициях"""
    F = [[(i+j) if i*j == 0 else 0 for j in range(len(B) + 1)] for i in range(len(A) + 1)]

    """
    Второстепенная часть. Запуск циклов for, пробегающих каждую строку размером N позиций
    и каждый столбец размером M позиций """
    for i in range(1, len(A)+1):
        for j in range(1, len(B) + 1):

            """ 
            Основная часть алгоритма - определение метода подсчета значения текущей позиции двумерного массива и сам подсчет, 
            те есть либо пропуск подсчета при равенстве текущих элементов, либо увеличение на 1 наименьшего значения из трех значений
            предыдущих соседних позиций при неравных текущих элементах """
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1]
            else:
                F[i][j] = min(F[i-1][j], F[i][j-1], F[i-1][j-1]) + 1
    """ Второстепенная часть алгоритма. Собственно, просто возврат функцией конечного результата вычислений"""
    return F[len(A)][len(B)]


A = "abas"
B = "dyemdf"

print(levensteinLenght(A, B))