"""

Алгоритм: Сортировка Шелла (Shell Sort)
-------------------------------------------
RU: На первом проходе мы используем элементы, расположенные с фиксированным промежутком (вместо ближайших соседей). 
    В итоге получаем подсписок, состоящий из пар элементов данных. Процесс показан на диаграмме (рис. 3.10).
    На втором проходе алгоритм сортирует подсписки, содержащие по четыре элемента данных. 
    В последующих проходах количество элементов в каждом подсписке увеличивается, а количество самих подсписков уменьшается. 
    Когда остается только один подсписок, содержащий все элементы данных, сортировка завершена.

EN: In the first pass, we use elements located at a fixed interval (instead of nearest neighbors).
    As a result, we obtain a sublist consisting of pairs of data elements. The process is shown in the diagram (Fig. 3.10).
    In the second pass, the algorithm sorts sublists containing four data elements.
    In subsequent passes, the number of elements in each sublist increases, and the number of sublists themselves decreases.
    When only one sublist remains, containing all the data elements, the sorting is complete.

Сложность / Complexity:
- Время / Time: O(n)
- Память / Space: O(n)

"""

def shellSort(list):
    distance = len(list) // 2
    while distance > 0:
        for i in range(distance, len(list)):
            temp = list[i]
            j = i
            # Сортировка подсписка для текущего значения дистанции
            # Sort the sublist for the current distance value
            while j >= distance and list[j - distance] > temp:
                list[j] = list[j - distance]
                j = j-distance
            list[j] = temp
        # Уменьшаем расстояние до следующего элемента
        # Reduce the distance to the next element
        distance = distance // 2
    return list


list = [29, 1, 15, 4, 89, 12, 45, 3, 9]

print(shellSort(list))


