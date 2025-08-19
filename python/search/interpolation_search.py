"""
Алгоритм: Интерполяционный поиск(Interpolation search)
-------------------------------------------

**EN:**  
Binary search is based on the logic that it focuses on the middle part of the data. 
Interpolation search is more complex. It uses a target value to estimate the position of an element in a sorted array. 
Let's try to understand this with an example. Suppose we want to find a word in the English dictionary, for example, river. 
We will use this information for interpolation and start searching for words starting with r.
If the data is not uniformly distributed, the performance of the interpolation search algorithm will be poor. 
**The worst-case performance of this algorithm is O(N)**, **the best-case performance is O(log(log N))** if the data is fairly uniform.

**RU:**  
Бинарный поиск основан на логике, согласно которой он сосредотачивается на средней части данных. 
Интерполяционный поиск более сложен. Он использует целевое значение для оценки положения элемента в отсортированном массиве. 
Давайте попробуем понять это на примере. Предположим, мы хотим найти слово в словаре английского языка, например river. 
Мы будем использовать эту информацию для интерполяции и начнем поиск слов, начинающихся с r.
Если данные распределены неравномерно, производительность алгоритма интерполяционного поиска будет низкой. 
**Наихудшая производительность этого алгоритма — O(N)**, **наилучшая — O (log(log N))**, если данные достаточно однородны.ов, 
для итерации потребуется максимум O(logN) шагов. Это означает, что алгоритм имеет время выполнения **O(logN)**.

Сложность / Complexity:
- Время / Time: O(log(logN))
- Память / Space: O(log(logN))
"""
def IntPolsearch(list, x):
    idx0 = 0
    idxn = (len(list) - 1)
    found = False
    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:
        # Looking for the middle point
        # Ищем срединную точку
        mid = idx0 +int(((float(idxn - idx0)/( list[idxn] - list[idx0])) * ( x - list[idx0])))
        # Compare the value at the midpoint with the search value
        # Сравниваем значение в средней точке со значением поиска
        if list[mid] == x:
            found = True
            return found
        if list[mid] < x:
            idx0 = mid + 1
    return found


list = [12, 33, 55, 99, 156, 987]
print(IntPolsearch(list, 99))