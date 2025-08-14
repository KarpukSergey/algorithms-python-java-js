# algorithms-python-java-js
**RU:** Реализация 40 популярных алгоритмов на Python, Java и JavaScript с объяснением и примерами.  
**EN:** Implementation of 40 popular algorithms in Python, Java, and JavaScript with explanations and examples.

---

## 📚 Оглавление / Table of Contents
1. [Bubble Sort / Сортировка пузырьком](#bubble-sort--сортировка-пузырьком)
2. [Insertion Sort / Сортировка вставками](#insertion-sort--сортировка-вставками)


---

## 🗂 Структура проекта / Project Structure
```
/python/sorting/bubble_sort.py
                insertion_sort.py
/java/sorting/BubbleSort.java
              InsertionSort.java
/javascript/sorting/bubble_sort.js
                    insertion_sort.js

```

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