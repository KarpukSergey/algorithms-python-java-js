"""
Алгоритм: Сортировка пузырьком (Bubble Sort)
-------------------------------------------
RU: Сравнивает соседние элементы и меняет их местами, если они стоят в неверном порядке.
    После каждого прохода наибольший элемент перемещается в конец списка.
EN: Compares adjacent elements and swaps them if they are in the wrong order.
    After each pass, the largest element moves to the end of the list.

Сложность / Complexity:
- Время / Time: O(n^2)
- Память / Space: O(1)
"""

def bubble_sort(arr): 
    last_index = len(arr) - 1
    for i in range(last_index, 0, -1):
        for idx in range(i):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
    return arr    
