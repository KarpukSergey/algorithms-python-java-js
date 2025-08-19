# algorithms-python-java-js
**RU:** Реализация 40 популярных алгоритмов на Python, Java и JavaScript с объяснением и примерами.  
**EN:** Implementation of 40 popular algorithms in Python, Java, and JavaScript with explanations and examples.

---

## 📚 Оглавление / Table of Contents
0. [Выбор алгоритма сортировки / Selecting a sorting algorithm](#выбор-алгоритма-сортировки--selecting-a-sorting-algorithm)
1. [Bubble Sort / Сортировка пузырьком](#bubble-sort--сортировка-пузырьком)
2. [Insertion Sort / Сортировка вставками](#insertion-sort--сортировка-вставками)
3. [Merge Sort / Сортировка слиянием](#merge-sort--сортировка-слиянием)
4. [Shell Sort / Сортировка шелла](#shell-sort--сортировка-шелла)
5. [Selection Sort / Cортировка выбором](#selection-sort--сортировка-выбором)
0. [Выбор алгоритма поиска / Selecting a search algorithm](#выбор-алгоритма-поиска--selecting-a-search-algorithm)
1. [Linear Search / Линейный Поиск](#linear-search--линейный-поиск)
2. [Binary Search / Бинарный Поиск](#binary-search--бинарный-поиск)
3. [interpolation Search / Интерполяционный Поиск](#interpolation-search--интерполяционный-поиск)

---

## 🗂 Структура проекта / Project Structure
```
/python/sorting/-|bubble_sort.py
                 |insertion_sort.py
                 |merge_sort.py
                 |shell_sort.py
                 |selection_sort.py
       /search/-|linear_search.py
                |binary_search.py
                |interpolation_search.py 
/java/sorting/-|BubbleSort.java
               |InsertionSort.java
               |MergeSort.java
               |ShellSort.java
               |SelectionSort.java
     /search/-|LinearSearch.java
              |BinarySearch.java
              |InterpolationSearch.java
/javascript/sorting/-|bubble_sort.js
                     |insertion_sort.js
                     |merge_sort.js
                     |shell_sort.js
                     |selection_sort.js
           /search/-|linear_search.js
                    |binary_search.js
                    |interpolation_search.js
```
---

### Выбор алгоритма сортировки / Selecting a sorting algorithm

**RU:**Выбор правильного алгоритма сортировки зависит как от размера, так и от состояния имеющихся входных данных. 
Для небольших отсортированных списков использование продвинутого алгоритма приведет к ненужному усложнению
кода при незначительном приросте производительности. Например, не следует использовать сортировку слиянием для небольших наборов данных. Сортировка пузырьком будет намного проще как для понимания‚ так для и реализации.
Если данные частично отсортированы, мы можем воспользоваться этим преимуществом и применить сортировку вставкой. Для больших наборов данных лучше всего использовать алгоритм сортировки слиянием

**EN:**Choosing the right sorting algorithm depends on both the size and the state of the input data.
For small sorted lists, using an advanced algorithm will unnecessarily complicate the code with little performance gain. For example, merge sort should not be used for small data sets. Bubble sort will be much simpler to understand and implement.
If the data is partially sorted, we can take advantage of this and use insertion sort. For large data sets, the merge sort algorithm is best
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

---

### Выбор алгоритма поиска / Selecting a search algorithm

**RU:**
Инструменты эффективного и точного поиска в структуре данных на практике имеют решающее значение. 
В зависимости от выбранного алгоритма поиска вам может потребоваться предварительная сортировка данных. 
Выбор подходящих алгоритмов сортировки и поиска зависит от типа и размера данных, а также от характера задачи, 
которую вы пытаетесь решить.

**EN:**
Tools for efficient and accurate search in a data structure are crucial in practice.
Depending on the search algorithm you choose, you may need to pre-sort your data.
The choice of appropriate sorting and search algorithms depends on the type and size of the data, as well as the nature of the problem you are trying to solve.

---

---

## Linear Search / Линейный поиск 

**EN:**  
One of the simplest strategies for searching data is to simply iterate through all the elements in search of the target.
Each data point is searched for a match. If the searched data is found, the algorithm returns the result and exits the loop. Otherwise, it continues searching until it reaches the end of the data structure. The obvious disadvantage of this algorithm is that it is very slow, since it performs an exhaustive search.
The advantage is that the data does not need to be sorted, as required by other algorithms.

**RU:**  
Одна из простейших стратегий поиска данных состоит в том, чтобы просто перебрать все элементы в поисках цели. 
В каждой точке данных выполняется поиск совпадения. При обнаружении искомых данных алгоритм возвращает
результат и выходит из цикла. В противном случае он продолжает поиск дотех пор, пока не достигнет конца структуры данных. Очевидным недостатком алгоритма является то, что он очень медленный, поскольку осуществляет исчерпывающий поиск. 
Преимущество же заключается в том, что данные не нужно сортировать, как того требуют другие алгоритмы.

---

### 📌 Сложность / Complexity
- Time: **O(n)** 
- Space: **O(n)**


### 💻 Примеры кода / Example code
Ссылки на файлы :
- Python: `python/search/linear_search.py`
- Java: `java/search/LinearSearch.java`
- JavaScript: `javascript/search/linear_search.js`

---

---

## Binary Search / Бинарный поиск

**EN:**  
A necessary condition for the binary search algorithm to work is that the data is ordered. The algorithm iteratively divides the list into two parts and tracks the lowest and highest indices until it finds the desired value.
Binary (also called "binary") search is so named because at each iteration the algorithm divides the data into two parts.
If the data contains N elements, the iteration will require at most O(logN) steps. This means that the algorithm has an execution time of **O(logN)**.

**RU:**  
Необходимым условием для работы алгоритма бинарного поиска является упорядоченность данных. Алгоритм итеративно делит список на две части и отслеживает самые низкие и самые высокие индексы, пока не найдет искомое значение.
Бинарный (говорят также «двоичный») поиск назван так потому, что на каждой итерации алгоритм разделяет данные на две части. 
Если данные содержат N элементов, для итерации потребуется максимум O(logN) шагов. Это означает, что алгоритм имеет время выполнения **O(logN)**.

---

### 📌 Сложность / Complexity
- Time: **O(logN)** 
- Space: **O(logN)**


### 💻 Примеры кода / Example code
Ссылки на файлы :
- Python: `python/search/binary_search.py`
- Java: `java/search/BinarySearch.java`
- JavaScript: `javascript/search/binary_search.js`

---

---

## Interpolation search / Интерполяционный поиск

**EN:**  
Binary search is based on the logic that it focuses on the middle part of the data. Interpolation search is more complex. It uses a target value to estimate the position of an element in a sorted array. Let's try to understand this with an example. Suppose we want to find a word in the English dictionary, for example, river. We will use this information for interpolation and start searching for words starting with r.
If the data is not uniformly distributed, the performance of the interpolation search algorithm will be poor. **The worst-case performance of this algorithm is O(N)**, **the best-case performance is O(log(log N))** if the data is fairly uniform.

**RU:**  
Бинарный поиск основан на логике, согласно которой он сосредотачивается на средней части данных. Интерполяционный поиск более сложен. Он использует целевое значение для оценки положения элемента в отсортированном массиве. Давайте попробуем понять это на примере. Предположим, мы хотим найти слово в словаре английского языка, например river. Мы будем использовать эту информацию для интерполяции и начнем поиск слов, начинающихся с r.
Если данные распределены неравномерно, производительность алгоритма интерполяционного поиска будет низкой. **Наихудшая производительность этого алгоритма — O(N)**, **наилучшая — O (log(log N))**, если данные достаточно однородны.

---

### 📌 Сложность / Complexity
- Time: **O(log(logN))** 
- Space: **O(log(logN))**


### 💻 Примеры кода / Example code
Ссылки на файлы :
- Python: `python/search/interpolation_search.py`
- Java: `java/search/InterpolationSearch.java`
- JavaScript: `javascript/search/interpolation_search.js`

---