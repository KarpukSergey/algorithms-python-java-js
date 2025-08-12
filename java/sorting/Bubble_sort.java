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

package java.sorting;

public class Bubble_sort {

    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        boolean swapped;
        for (int i = 0; i < n - 1; i++) {
            swapped = false;
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap arr[j] and arr[j + 1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                    swapped = true;
                }
            }
            // If no two elements were swapped by inner loop, then break
            if (!swapped) break;
        }
    }
} 