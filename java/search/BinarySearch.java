/*
Алгоритм: Бинарный поиск (Binary Search)
-------------------------------------------

**EN:** 
For the binary search algorithm to work correctly, a sorted list is needed. In my example, I use the bubble sort algorithm. You will find the description and example code in the Readme file.

A necessary condition for the binary search algorithm to work is that the data is ordered. The algorithm iteratively divides the list into two parts and tracks the lowest and highest indices until it finds the desired value.
Binary (also called "binary") search is so named because at each iteration the algorithm divides the data into two parts.
If the data contains N elements, the iteration will require at most O(logN) steps. This means that the algorithm has an execution time of **O(logN)**.

**RU:** 
Что бы алгоритм бинарно поиска работал коректно, нужно отсортированый список. В моём примере, я использую алгоритм сортировки пузырьком. Описание и пример кода вы найдёте в Reasdme файле .

Необходимым условием для работы алгоритма бинарного поиска является упорядоченность данных. Алгоритм итеративно делит список на две части и отслеживает самые низкие и самые высокие индексы, пока не найдет искомое значение.
Бинарный (говорят также «двоичный») поиск назван так потому, что на каждой итерации алгоритм разделяет данные на две части. 
Если данные содержат N элементов, для итерации потребуется максимум O(logN) шагов. Это означает, что алгоритм имеет время выполнения **O(logN)**.

Сложность / Complexity:
- Время / Time: O(logN)
- Память / Space: O(logN)
*/

package java.search;

public class BinarySearch {

    public static int[] bubbleSort(int[] arr) {
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

        return arr;
    }

    public static boolean binarySearch(int[] list, int item){
        
        int first = 0;
        int last = list.length - 1;
        boolean found = false;

        while(first <= last && !found){
            int midpoint = (first + last) / 2;
            if (list[midpoint] == item){
                found = true;
            }else{
                if(list[midpoint] > item){
                    last = midpoint - 1;
                }else{
                    first = midpoint + 1;
                }
            }
        }
        
        return found;

    }

    public static void main(String[] args) {
        int[] list = {12, 33, 11, 99, 22, 55, 90};
        int[] sorted_list = bubbleSort(list);
        System.out.println(binarySearch(sorted_list, 22));
    }   
    
}
