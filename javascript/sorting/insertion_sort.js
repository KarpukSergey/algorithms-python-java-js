/*
Алгоритм: Сортировка вставками (Insertion Sort)
-------------------------------------------
RU: На первой итерации мы сортируем два элемента данных. 
    Затем мы расширяем выборку: берем третий элемент и находим для него позицию согласно его значению. 
    Алгоритм выполняется до тех пор, пока все элементы не будут перемещены в правильное положение.
    Как правило, сортировка вставкой используется в работе с небольшими структурами данных. 
    Для больших структур этот алгоритм не рекомендуется, поскольку обладает квадратичной средней производительностью.

EN: In the first iteration, we sort two data elements.
    Then we expand the selection: we take the third element and find its position according to its value.
    The algorithm is executed until all elements are moved to the correct position.
    As a rule, insertion sort is used when working with small data structures.
    For larger structures, this algorithm is not recommended, since it has a quadratic average performance.

Сложность / Complexity:
- Время / Time: **O(n²)** worst case, **O(n)** best case
- Память / Space: O(1)
*/

function insertion_sort(list) {
    for (let i = 1; i < list.length; i++) {
        let element_next = list[i]; // текущий элемент / current element
        let j = i - 1;

        // Сдвигаем элементы вправо, пока они больше текущего / Shift elements to the right while they are larger than the current one
        while (j >= 0 && list[j] > element_next) {
            list[j + 1] = list[j];
            j = j - 1;
        }
        // Вставляем текущий элемент на нужное место / Insert the current element in the desired place
        list[j + 1] = element_next;
    }
    return list;
}

let list = [5, 6, 2, 1, 9, 7]

// Вывод результата / Output of the result
console.log(insertion_sort(list))
