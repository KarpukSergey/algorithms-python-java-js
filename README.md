# algorithms-python-java-js
**RU:** Реализация 40 популярных алгоритмов на Python, Java и JavaScript с объяснением и примерами.  
**EN:** Implementation of 40 popular algorithms in Python, Java, and JavaScript with explanations and examples.

---

## 📚 Оглавление / Table of Contents
1. [Bubble Sort / Сортировка пузырьком](#bubble-sort--сортировка-пузырьком)
2. [Insertion Sort / Сортировка вставками](#insertion-sort--сортировка-вставками)
3. [Merge Sort / Сортировка слиянием](#merge-sort--сортировка-слиянием)
4. [Shell Sort / Сортировка шелла](#shell-sort--сортировка-шелла)

---

## 🗂 Структура проекта / Project Structure
```
/python/sorting/-|bubble_sort.py
                 |insertion_sort.py
                 |merge_sort.py
                 |shell_sort.py
                 |selection_sort.py
/java/sorting/-|BubbleSort.java
               |InsertionSort.java
               |MergeSort.java
               |ShellSort.java
               |SelectionSort.java
/javascript/sorting/-|bubble_sort.js
                     |insertion_sort.js
                     |merge_sort.js
                     |shell_sort.js
                     |selection_sort.ja

```
---

### Выбор алгоритма сортировки

Выбор правильного алгоритма сортировки зависит как от размера, так и от состояния имеющихся входных данных. 
Для небольших отсортированных списков использование продвинутого алгоритма приведет к ненужному усложнению
кода при незначительном приросте производительности. Например, не следует использовать сортировку слиянием для небольших наборов данных. Сортировка пузырьком будет намного проще как для понимания‚ так для и реализации.
Если данные частично отсортированы, мы можем воспользоваться этим преимуществом и применить сортировку вставкой. Для больших наборов данных лучше всего использовать алгоритм сортировки слиянием

---

---

## Bubble Sort / Сортировка пузырьком

**EN:**  
Bubble sort is one of the simplest sorting algorithms, but it is quite slow.  
The idea is that on each pass, the largest element "bubbles up" to the end of the list.  
In the worst case, its time complexity is **O(n²)**, so it should only be used for small datasets.

**RU:**  
Сортировка пузырьком — один из самых простых алгоритмов сортировки, но при этом довольно медленный.  
Идея в том, что на каждом шаге самый большой элемент «всплывает» к концу списка.  
В худшем случае время работы алгоритма — **O(n²)**, поэтому применять его стоит только для небольших массивов данных.

---

### 📌 Сложность / Complexity
- Time: **O(n²)**
- Space: **O(1)**

---

### 💻 Примеры кода / Example code
Ссылки на файлы :
- Python: `python/sorting/bubble_sort.py`
- Java: `java/sorting/BubbleSort.java`
- JavaScript: `javascript/sorting/bubble_sort.js`

---

## Insertion Sort / Сортировка вставками

**EN:**  
The basic idea of insertion sort is that at each iteration we take the next element from the unsorted part of the list and insert it into the correct position in the sorted part.  
In the best case (already sorted array), the algorithm runs in **O(n)**.  
In the worst case (reverse order), it runs in **O(n²)**.

**RU:**  
Основная идея сортировки вставками заключается в том, что на каждой итерации мы берём следующий элемент из неотсортированной части массива и вставляем его на нужное место в отсортированной части.  
В лучшем случае (массив уже отсортирован) алгоритм работает за **O(n)**.  
В худшем случае (обратный порядок) — за **O(n²)**.

---

### 📌 Сложность / Complexity
- Time: **O(n²)** worst case, **O(n)** best case
- Space: **O(1)**


### 💻 Примеры кода / Example code
Ссылки на файлы :
- Python: `python/sorting/insertion_sort.py`
- Java: `java/sorting/InsertionSort.java`
- JavaScript: `javascript/sorting/insertion_sort.js`

---



## Merge Sort / Сортировка слиянием

**EN:**  
We have studied two sorting algorithms: bubble sort and insertion sort. Both of them perform better if the data is already partially sorted. The third algorithm we will look at is merge sort , developed in 1940 by John von Neumann. **The distinguishing feature of this algorithm is the fact that its performance does not depend on the ordering of the input data**. Like MapReduce and other big data processing algorithms, it is based on a divide and conquer strategy.

**RU:**  
Мы изучили два алгоритма сортировки: пузырьком и вставками. Производительность обоих будет лучше, если данные уже частично отсортированы. Третий алгоритм, с которым мы познакомимся, — алгоритм сортировки слиянием , разработанный в 1940 году Джоном фон Нейманом. **Отличительной чертой этого алгоритма является тот факт, что его производительность не зависит от упорядоченности входных данных**. Подобно MapReduce и другим алгоритмам обработки больших данных, в его основе лежит стратегия «разделяй и властвуй».

---

### 📌 Сложность / Complexity
- Time: **O(n lon n)** 
- Space: **O(n)**


### 💻 Примеры кода / Example code
Ссылки на файлы :
- Python: `python/sorting/merge_sort.py`
- Java: `java/sorting/MergeSort.java`
- JavaScript: `javascript/sorting/merge_sort.js`

---


## Shell Sort / Сортировка Шелла

**EN:**  
Bubble Sort compares the values of adjacent elements and swaps them if they are not in the desired order.
If the list is partially sorted, we get acceptable performance: the sort is complete as soon as the loop stops swapping values.
In the case of a completely unsorted list of size N, the algorithm must make N – 1 full passes.
Donald Shell proposed his sorting algorithm, questioning the need to select adjacent elements for comparison and swapping. The algorithm was called Shell Sort
Shell Sort is not designed for large data. It is used for medium-sized data sets. Roughly speaking, the algorithm will give fairly good performance when working with a list containing up to 6000 elements.
**If the data is partially sorted, the performance will be better**.
Ideally, the list is completely sorted, then only one pass through N elements is required to check the order, which will provide the best performance **O(N)**.

**RU:**  
Алгоритм сортировки пузырьком сравнивает значения соседних элементов и меняет их местами, если они не стоят в нужном порядке. 
Если список частично отсортирован, мы получаем приемлемую производительность: сортировка завершается, как только в цикле прекращается обмен значениями.
В случае с полностью неотсортированным списком размера N алгоритм должен совершить N – 1 полных проходов.
Дональд Шелл предложил свой алгоритм сортировки, поставив под сомнение необходимость выбора соседних элементов для сравнения и обмена. Алгоритм получил название сортировка Шелла
Сортировка Шелла не предназначена для больших данных. Она используется для наборов данных среднего размера. Грубо говоря, алгоритм даст достаточно хорошую производительность при работе со списком, содержащим до 6000 элементов. 
**Если данные частично упорядочены, производительность будет выше**. 
В идеале список полностью отсортирован, тогда для проверки порядка потребуется только один проход через N элементов, что обеспечит наилучшую производительность **O(N)**.
---

### 📌 Сложность / Complexity
- Time: **O(n)** 
- Space: **O(n)**


### 💻 Примеры кода / Example code
Ссылки на файлы :
- Python: `python/sorting/shell_sort.py`
- Java: `java/sorting/ShellSort.java`
- JavaScript: `javascript/sorting/shell_sort.js`

---

## Selection Sort / Сортировка выбором 

**EN:**  
As we have seen, bubble sort is one of the simplest sorting algorithms.
Selection sort is an improved version of it. With it, we try to minimize the total number of
exchanges of variable values. Each pass performs one exchange (compare to N – 1 in bubble sort). Instead of moving the largest value in small steps, we look for it at each iteration and put it at the end of the list.
This means that the first pass will result in the largest value being on the right, and the second pass will move the next largest value to it. As the algorithm runs, subsequent elements will be moved to the right place according to their value.
The last element will be moved after the (N – 1)th pass. Thus, selection sort requires N – 1 passes to
sort N elements

**RU:**  
Как мы выяснили, сортировка пузырьком является одним из простейших алгоритмов сортировки. 
Сортировка выбором — это его улучшенная версия. С ее помощью мы стараемся минимизировать общее количество
обменов значений переменных. За каждый проход выполняется один обмен (сравните с N – 1 в случае сортировки пузырьком). Вместо того чтобы перемещать наибольшее значение маленькими шагами, мы ищем его на каждой итерации и ставим в конец списка. 
Это значит, что в результате первого прохода наибольшее значение окажется справа, а в результате второго прохода
к нему переместится следующее по величине значение. По мере выполнения алгоритма последующие элементы будут перемещаться в нужное место согласно их значению. 
Последний элемент будет перемещен после (N – 1)-го прохода. Таким образом, сортировка выбором требует N – 1 проходов для
сортировки N элементов
---

### 📌 Сложность / Complexity
- Time: **O(n2)** 
- Space: **O(1)**


### 💻 Примеры кода / Example code
Ссылки на файлы :
- Python: `python/sorting/selection_sort.py`
- Java: `java/sorting/SelectionSort.java`
- JavaScript: `javascript/sorting/selection_sort.js`

---