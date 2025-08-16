/*
Алгоритм: Линейный поиск (Linear Search)
-------------------------------------------

**EN:**  
One of the simplest strategies for searching data is to simply iterate through all the elements in search of the target.
Each data point is searched for a match. If the searched data is found, the algorithm returns the result and exits the loop. Otherwise, it continues searching until it reaches the end of the data structure. The obvious disadvantage of this algorithm is that it is very slow, since it performs an exhaustive search.
The advantage is that the data does not need to be sorted, as required by other algorithms.

**RU:**  
Одна из простейших стратегий поиска данных состоит в том, чтобы просто перебрать все элементы в поисках цели. 
В каждой точке данных выполняется поиск совпадения. При обнаружении искомых данных алгоритм возвращает
результат и выходит из цикла. В противном случае он продолжает поиск дотех пор, пока не достигнет конца структуры данных. Очевидным недостатком алгоритма является то, что он очень медленный, поскольку осуществляет исчерпывающий поиск. 
Преимущество же заключается в том, что данные не нужно сортировать, как того требуют другие алгоритмы.

Сложность / Complexity:
- Время / Time: O(n)
- Память / Space: O(n)
*/

function linear_search(list, item){
    let index = 0;
    let found = false;
    // Сравниваем значение с каждым элементом данных
    // Compare the value with each data element
    while(index < list.length && !found){
        if(list[index] === item){
            found = true
        } else {
            index = index + 1
        }
    }
    return found;
}

let list = [56, 12, 4, 90, 19, 45];
console.log(linear_search(list, 19))