/*
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
 */

import java.util.Arrays;

public class MergeSort {
    
    public static int[] merge_sort(int[] list){
        // Базовый случай рекурсии — если массив состоит из одного элемента, он уже отсортирован
        // The base case of recursion is that if the array has one element, it is already sorted
        if(list.length > 1){
            // Находим середину массива
            // Find the middle of the array
            int mid = list.length / 2;

            // Левая и правая половины
            // Left and right halves
            int[] left = Arrays.copyOfRange(list, 0, mid); 
            int[] right = Arrays.copyOfRange(list, mid, list.length);

            // Рекурсивная сортировка каждой половины
            // Recursively sort each half
            merge_sort(left);
            merge_sort(right);

            // Индексы для прохода по left, right и результирующему массиву
            // Indexes for traversing left, right and the resulting array
            int a = 0;
            int b = 0;
            int c = 0;

            // Слияние: выбираем меньший элемент из левой или правой части
            // Merge: select the smaller element from the left or right side
            while (a < left.length && b < right.length) {
                if(left[a] < right[b]){
                    list[c] = left[a];
                    a = a + 1;
                }else{
                    list[c] = right[b];
                    b = b + 1;
                }
                c = c + 1;
            }

            // Добавляем оставшиеся элементы левой части (если есть)
            // Add the remaining elements of the left side (if any)
            while (a < left.length) {
                list[c] = left[a];
                a = a + 1;
                c = c + 1;
            }

            // Добавляем оставшиеся элементы правой части (если есть)
            // Add the remaining elements of the right side (if any)
            while (b < right.length) {
                list[c] = right[b];
                b = b + 1;
                c = c + 1;
            }
        }
        return list;
    }

    public static void main(String[] args){
        // Пример использования / Example usage
        int[] list = {44, 16, 83, 7, 67, 21, 34, 45, 10};
        merge_sort(list);

        for(int i = 0; i < list.length; i++){
            System.out.println(list[i]);
        }
    }

}
