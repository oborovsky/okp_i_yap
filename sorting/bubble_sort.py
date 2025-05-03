#bubble_sort.py
"""Сортировка пузырьком.

Проходит по массиву, сравнивая соседние
элементы, и меняем их местами, если они
расположены в неправильном порядке.
Пример:[2, 1, 6, 7, 4]
1. [1, 2, 6, 4, 7]
2. [1, 2, 4, 6, 7]

>>> bubble_sort([2, 1, 6, 4, 7])
[1, 2, 4, 6, 7]
"""

def bubble_sort(arr_):
    """Сортировка пузырьком.
    
    >>> bubble_sort([])
    []
    >>> bubble_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> bubble_sort([4, 7, 3, 9, 1, 5, 3])
    [1, 3, 3, 4, 5, 7, 9]
    """
    arr = arr_.copy()
    n = len(arr)
    
    for i in range(n):
        is_sorted = True
        
        for j in range(n - 1, i, -1):
           if arr[j] < arr[j - 1]:
               arr[j], arr[j -1] = arr[j -1], arr[j]
               is_sorted = False
        
        if is_sorted:
            break
    
    return arr

def main():
    import doctest
    doctest.testmod()
    
if __name__ == "__main__":
    main()
    