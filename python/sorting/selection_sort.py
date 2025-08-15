"""
Алгоритм: Сортировка выбором (Selection Sort)
-------------------------------------------
RU: результате второго прохода к нему переместится следующее по величине значение. По мере выполнения
    алгоритма последующие элементы будут перемещаться в нужное место согласно их значению. 
    Последний элемент будет перемещен после (N – 1)-го прохода. Таким образом, сортировка выбором требует N – 1 проходов для
    сортировки N элементов

EN: the second pass will move the next largest value to it. As the algorithm runs, subsequent elements will be moved to the 
    correct place according to their value. The last element will be moved after the (N – 1)th pass. 
    Thus, selection sort requires N – 1 passes to sort N elements

Сложность / Complexity:
- Время / Time: O(n2)
- Память / Space: O(1)

"""

def selection_sort(list):
    for fill_slot in range(len(list) - 1, 0, -1):
        max_index = 0

        # Находим индекс максимального элемента в оставшейся части
        # Find the index of the maximum element in the remaining part
        for location in range(1, fill_slot + 1):
            if list[location] > list[max_index]:
                max_index = location

        # Меняем местами максимальный элемент с элементом на позиции fill_slot
        # Swap the maximum element with the element at fill_slot position
        list[fill_slot],list[max_index] = list[max_index],list[fill_slot]
    return list 


print(selection_sort([44, 16, 83, 7, 67, 21, 34, 45, 10]))


