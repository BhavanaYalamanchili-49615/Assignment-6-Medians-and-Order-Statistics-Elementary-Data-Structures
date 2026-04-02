# Assignment 6: Medians and Order Statistics and Elementary Data Structures

### Assignment Overview
The assignment is aimed at the application and analysis of selection algorithms and elementary data structures. The main objective will be to investigate the Median of Medians and Randomized Quickselect algorithms used to locate the k th smallest element of an array and evaluate their effectiveness. It also involves the implementation of basic data structures such as; arrays, stacks, queues and linked lists and the practical use of these structures are to be discussed in-depth.

## Part 1: Selection Algorithms implementation and Analysis

### Deterministic Algorithm: Median of Medians
The Median of medians algorithm is an algorithm that is used to find the kth smallest element in an array in worst-case linear time. In this deterministic method, the array is divided in smaller groups of 5 elements, the median of these groups is determined and median of the median is determined recursively to effectively divide the array.

### Randomized Quickselect: Randomized Algorithm
Randomized Quickselect algorithm is a method that is used to pick the k th minimum element of an array in the expected linear time. Since it uses one partition to identify the kth smallest element, this algorithm performs better than deterministic algorithms by randomly picking a pivot and subdividing the array.

## Part 2: Implementation and Discussion of Elementary Data Structures

### Arrays and Matrices
Such basic operations as insertion, deletion and access are implemented on arrays. The matrix is a list of lists which allow such operations as inserting of rows and elements, deleting the rows and elements and access of the elements. These functions allow good management of two-dimensional and one-dimensional arrays.

### Stacks and Queues
The Python lists are used to implement both stacks and queues. The stack is based on the principle of Last In First Out (LIFO), which has such operations as push, pop, and peek. The queue is based on the idea of the First In First out (FILO) and thus it supports enqueue, dequeue, and peek operations. Such implementations show simple queue and stack operations whose time complexity is O(1) in the operation of these.

### Linked Lists
An implementation of a singly linked list makes possible such operations as head insertion, value deletion, and traversal. The linked list is dynamic and it handles the elements where each node holds data and a reference to the next node, hence it is good when dealing with data structure that is dynamic.

### Performance Analysis
#### Complexity of Operation with Time
In the array implementation, insertion and deletion is in worst case, O(n) and access is O(1). The time complexity of push/enqueue, pop/dequeue and peek operations of stacks and queues are O(1). In the case of linked lists, the cost of adding and removing a node at the head is O(1) and at other positions is O(n) and the cost of traversing the list is O(n).

#### Trade-offs between Arrays and Linked Lists in Stacks and Queues
Arrays are fast with regards to constant-time access at the cost of size and resizing, so arrays are less efficient in processes requiring dynamism. Linked lists on the other are more efficient with repetitive additions and removals and when the size of the data structure varies dynamically.

### Discussion: Uses and Counteractions Practical Applications and when each data structure should be used
The arrays can best fit applications where indexing is important for example, look-ups and matrix operations.
Stacks are employed in undo operations, expression evaluation and function calls.
Queues are used in the systems of task scheduling, buffering, and passing messages.
Linked lists can be used where memory needs to be managed dynamically e.g. in a real time simulation or operating system.

### Empirical Analysis
The empirical test is between the Median of Medians and the Randomized Quickselect algorithm performance on arrays of various sizes. The performance of both algorithms can be determined by the measurement and comparison of the running time, as the results reveal that they both have a linear time complexities, with the Randomized Quickselect performing much faster usually with a large dataset.

### Instructions to Run the Code
Run the Python Code:
Go to the folder with the code and execute the Python code:
python <filename.py>

### Testing
The algorithms of selection are tested using arrays of different sizes.
The implementations of the data structures undergo experiments to basic operations such as insertion, deletion and access.

### Conclusion
In this assignment, basic selection algorithms and basic data structures were implemented, and some information was obtained about their performance and practical use. The empirical study and discussions indicate the significance in using proper data structures depending on performance and memory demands.
