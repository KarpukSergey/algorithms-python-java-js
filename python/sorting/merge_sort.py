"""
Алгоритм: Сортировка слиянием  (Merge Sort)
-------------------------------------------
RU: На этапе разделения алгоритм рекурсивно разбивает данные на две части до тех
    пор, пока размер данных не станет меньше определенного порогового значения.
    На этапе слияния алгоритм объединяет данные, пока мы не получим окончательный результат.

EN: In the split stage, the algorithm recursively splits the data into two parts 
    until the data size is less than a certain threshold. 
    In the merge stage, the algorithm combines the data until we get the final result.

Сложность / Complexity:
- Время / Time: O(n lon n)
- Память / Space: O(n)

"""

def merge_sort(list):
    # Базовый случай рекурсии — если массив состоит из одного элемента, он уже отсортирован
    # The base case of recursion is that if the array has one element, it is already sorted
    if len(list) > 1:
        # Находим середину массива
        # Find the middle of the array
        mid = len(list) // 2

        # Левая и правая половины
        # Left and right halves
        left = list[:mid]
        right = list[mid:]

        # Рекурсивная сортировка каждой половины
        # Recursively sort each half
        merge_sort(left)
        merge_sort(right)

        # Индексы для прохода по left, right и результирующему массиву
        # Indexes for traversing left, right and the resulting array
        a = 0
        b = 0 
        c = 0

        # Слияние: выбираем меньший элемент из левой или правой части
        # Merge: select the smaller element from the left or right side
        while a < len(left) and b < len(right):
            if left[a] < right[b]:
                list[c] = left[a]
                a = a + 1
            else: 
                list[c] = right[b]
                b = b + 1
            c = c + 1

        # Добавляем оставшиеся элементы левой части (если есть)
        # Add the remaining elements of the left side (if any)
        while a < len(left):
            list[c] = left[a]
            a = a + 1
            c = c + 1

        # Добавляем оставшиеся элементы правой части (если есть)
        # Add the remaining elements of the right side (if any)
        while b < len(right):
            list[c] = right[b]
            b = b + 1
            c = c + 1
    
    return list

# Пример использования / Example usage
print(merge_sort([44, 16, 83, 7, 67, 21, 34, 45, 10]))
            