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

public class InsertionSort {

    public static int[] insertionSort(int[] list) {
        for (int i = 1; i < list.length; i++) {
            int elementNext = list[i]; // текущий элемент / current element
            int j = i - 1;

            // Сдвигаем элементы вправо, пока они больше текущего / Shift elements to the right while they are larger than the current one
            while (j >= 0 && list[j] > elementNext) {
                list[j + 1] = list[j];
                j--;
            }
            // Вставляем текущий элемент на нужное место / Insert the current element in the desired place
            list[j + 1] = elementNext;
        }
        return list;
    }

    public static void main(String[] args) {
        int[] arr = {5, 6, 2, 1, 9, 7};
        insertionSort(arr);

        // Вывод результата / Output of the result
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}