# collections_ext: extended Python data structure with highly efficient implementation



[![https://gitter.im/pydata/pandas](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/pydata/pandas?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

## What is it
Standard Python lacks many popular data structures, such as BinaryHeap, BST, etc. This reposotory is 
an extension of the collections package in the standard Python.

## Available Data Strucures
### Heap
Implementation of binary heap using array list (https://en.wikipedia.org/wiki/Heap_(data_structure)). 
The object can be a list of any objects as long their values can be mutually compared.

```python
# Creating a heap is simple
from collections_ext import Heap
pq = Heap([1,2,3,4,5]); pq
Out: [5, 3, 4, 2, 1]

# By default, the constructor makes a copy of the input array therefore does not mutate the input.
# Alternatively, inplace arguement can be specified in order to save the time of coping a big array.
array = [1, 2, 3, 4, 5]
pq = Heap(array); array # array is not mutated
Out: [1, 2, 3, 4, 5]

pq = Heap(array, inplace=True); array # array is mutated
Out: [5, 3, 4, 2, 1]

# The implementation supports insert, pop and replace:
pq.insert(3.5); pq
Out: [5, 3, 4, 2, 1, 3.5]

pq.replace(4.5)
Out: 5

pq
Out: [4.5, 3, 4, 2, 1, 3.5]

while pq:
    print(pq.pop(), end=', ')
Out: 4.5, 4, 3.5, 3, 2, 1, 

# To achieve minimum priority queue, one can change the default key:
array = [1, 2, 3, 4, 5]
pq = Heap(array, key = lambda x : -x); pq
Out: [1, 2, 3, 4, 5]


# Applying the same idea one can use list of tuples or other objects 
# to construct the heap
array = [(1, 'apple'), (2, 3.14159), (3, [0,1,2]), (4, {'key':'value'})]
pq = Heap(array, key = lambda x : x[0]); pq
Out: [(4, {'key': 'value'}), (3, [0, 1, 2]), (2, 3.14159), (1, 'apple')]
```

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/ustcscgyer/collections_ext

## License
TBD

## Documentation
TBD

## Contribution
I currently work by myself on this project and haven't yet thought about how to cooperate. But if you are interested to work together, 
you are more than welcome to contact me (ustcscgyer@gmail.com) so we can discuss about that. 

## Report Issues
There is no guarantee about the performance and the correctness of the implementations. If you encounter problems or if you have 
suggestions for improvement, please contact me (ustcscgyer@gmail.com).
