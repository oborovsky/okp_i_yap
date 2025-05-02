#shell_sort.py

"""Сортировка Шелла.

Анологична сортировки вставками, 
только шаг выбора d > 1 и уменьшается
до 1. Эмпирическая последовательность
шага d = {1, 4, 10, 23, 57, ...} - 
Мартина Циура (А102549 в OEIS).
Используем критерий для d: 3*d <= N,
где d - длина шага, N - длина массива.
Вычисляем шаг по формуле: d = 2^i - 1 <= N/2,
для i € N, т.е. 0 < i <= [log(N/2 + 1)]

1. В начальный момент отсортированная
   последовательность пуста.
2. На каждом шаге алгоритма выбираем один из
   элементов входных данных и помещаем в
   уже отсортированную последовательность
   на нужную позицию до тех пор, пока набор
   входных данных не будет исчерпан.

Пример: [4, 7, 2, 9, 10, 3, 8]
d=3
[4, 7, 2, 8, 10, 3, 9]
d=2
[2, 3, 4, 7, 9, 8, 10]
d=1
[2, 3, 4, 7, 8, 9, 10]

>>> shell_sort([4, 7, 2, 9, 10, 3, 8])
[2, 3, 4, 7, 8, 9, 10]
"""
import logging
logger = logging.getLogger(__name__)
#logging.basicConfig(level=logging.DEBUG)

def shell_sort(arr_):
    """Сортировка Шелла.
    
    >>> shell_sort([])
    []
    >>> shell_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> shell_sort([5, 6, 5, 7, 1, 2])
    [1, 2, 5, 5, 6, 7]
    """
    arr = arr_.copy()
    n = len(arr)
    
    logger.debug(f"{n=}")
    
    if n == 0:
        return arr
    
    steps = get_steps(n)
    logger.debug(f"{steps=}")
    
    for d in steps:
        for i in range(d, n, d):
            cur = arr[i]
            j = i - d
        
            while j >= 0:
                if arr[j] > cur:
                    arr[j + d] = arr[j]
                    j -= d
                else:
                    break
                    
            if j != i - d:
                arr[j + d] = cur
        
        logger.debug(f"{d=} {arr=}")
        
    return arr

def get_steps(n):
    """Вычисляем последовательность шагов.
    
    По формуле: d = {2^i - 1 <= n/2 | i:N},
    т.е. 0 < i <= [log(n/2+1)]
    """
    import math
    
    return [2**i - 1 for i in range(math.floor(math.log2(n/2+1)), 0, -1)]
    
def main():
    logging.basicConfig(level=logging.DEBUG)
    
    import doctest
    doctest.testmod()
    
if __name__ == "__main__":
    main()
