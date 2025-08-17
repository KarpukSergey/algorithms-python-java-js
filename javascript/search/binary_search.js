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

function BinarySearch(list, item){
    let first = 0;
    let last = list.length - 1;
    let found = false;
    while(first <= last && !found){
        let midpoint = Math.floor((first + last) / 2)
        if(list[midpoint] == item){
            found = true;
        } else {
            if(item < list[midpoint]){
                last = midpoint-1
            } else{
                first = midpoint + 1
            }
        }
    }
    return found;
}

let list = [12, 33, 11, 99, 22, 55, 90]
sorted_list = bubble_sort(list)
console.log(BinarySearch(list, 22))