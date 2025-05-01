# merge_sort.py
"""Сортировка слиянием.

1. Сортируемый массив разбивается
   на две примерно одинаковых части.
   
2. Каждая из полученных частей
   сортируется отдельно, например, 
   тем же самым алгоритмом (массив
   длины 1 считается уже отсортированным).
   
3. Два упорядоченных массива половинного
   размера сливаются в один.

Пример: [5, 6, 3, 9, 1, 4]
1. [5, 6, 3] [9, 1, 4]
2. [5] [6, 3] [9] [1, 4]
3. [5] [6] [3] [9] [1] [4]
4. [5] [3, 6] [9] [1, 4]
5. [3, 5, 6] [1, 4, 9]
6. [1, 3, 4, 5, 6, 9]

>>> merge_sort([5, 6, 3, 9, 1, 4])
[1, 3, 4, 5, 6, 9]
"""
import logging
logger = logging.getLogger(__name__)

def merge_sort(arr):
    """Сортировка слиянием.
    
    >>> merge_sort([])
    []
    >>> merge_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> merge_sort([1, 8, 1, 4, 5, 4])
    [1, 1, 4, 4, 5, 8]
    """
    
    #split array
    n = len(arr)
    n1 = n // 2
    n2 = n - n1
    
    logger.debug(f"{arr=}")
    logger.debug(f"{n=}, {n1=}, {n2=}")
    
    if n1 > 1:
        result1 = merge_sort(arr[:n1])
    else:
        result1 = arr[:n1]
        
    if n2 > 1:
        result2 = merge_sort(arr[n1:])
    else:
        result2 = arr[n1:]
    logger.debug(f"{result1=}, {result2=}")
    
    #merge arraies
    i1, i2 = 0, 0
    result = []
    
    for i in range(n):
        if i1 < n1 and i2 < n2:
            if result1[i1] <= result2[i2]:
                result.append(result1[i1])
                i1 += 1
            else:
                result.append(result2[i2])
                i2 += 1
        elif i1 < n1 and i2 >= n2:
            result.append(result1[i1])
            i1 += 1
        else:
            result.append(result2[i2])
            i2 += 1
    
    logger.debug(f"{result=}")
        
    return result
    
def main():
    #logging.basicConfig(level=logging.DEBUG)
    
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    main()
