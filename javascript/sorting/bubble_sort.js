/*
Алгоритм: Сортировка пузырьком (Bubble Sort)
-------------------------------------------
RU: Сравнивает соседние элементы и меняет их местами, если они стоят в неверном порядке.
    После каждого прохода наибольший элемент перемещается в конец списка.
EN: Compares adjacent elements and swaps them if they are in the wrong order.
    After each pass, the largest element moves to the end of the list.

Сложность / Complexity:
- Время / Time: O(n^2)
- Память / Space: O(1)
*/


function bubble_sort(arr) {
    const n = arr.length;
    let swapped;
    for (let i = 0; i < n - 1; i++) {
        swapped = false;  // Сбрасываем флаг на каждый проход
        for (let idx = 0; idx < n - i - 1; idx++) {
            if (arr[idx] > arr[idx + 1]) {
                // Меняем элементы местами
                const temp = arr[idx];
                arr[idx] = arr[idx + 1];
                arr[idx + 1] = temp;
                swapped = true;
            }
        }
        if (!swapped) break;  // Если за проход перестановок не было — выходим
    }
    return arr;
}
