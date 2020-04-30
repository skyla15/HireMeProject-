# Queue ( First-in First-out )
- Networked Printer 
- Web server responding to requests 
- Queueing theory 
### ADT
- Q.enqueue(e): Add element to the back of queue Q 
- Q.dequeue(): Remove and return the front element of queue Q. Error, if empty
- Q.first(): Return a reference to the element at the front of queue Q 
- Q.is_empty(): Return True if queue Q is empty 
- len(Q): Return the number of elements in queue Q; (in Python, special method uses \_\_len__)
### 6.2.2. Array-Based Queue Implementation

- Inefficient implementation 
  - Q.append(e) : add an e to the end 

  - Q.pop(0) : delete and return the first element  

    - When pop(non-default) is used, __loop__ is executed to __shift all elements beyond the specified index to the left__. pop(0) : 𝜣(n) time. 

    - Use a reference 'f' to None and maintain the front index of the queue. O(1) time 

      => Size of total length of queue can be enormous because this way, I don't empty the previous fronts instead I just move the reference 'f' to the next front index. 

      - => Circular Queue 

- Circular Queue 

  - In this book, when enqueing, it uses a method to wrap around at the end of underlying array, with the front assigned to 0. 
    - When enqueing, double the size of the current queue, assign the front to index 0 
  - Advance the front index by using modulo operation : f = ( f+1 ) % N 

___ 

### The Adapter Design Pattern
- Modify an existing class so that its methods match those of a related but diffrent class or interface.  
Ex) New Class

Stack Method|Python List Method|Big-O|
----------|----------|-----------| 
S.push(e) |L.append(e)|O(1)|
S.pop(e) |L.pop(e)|O(1)|
S.top() |L\[-1\] |O(1)|
S.is_empty() |len(L)==0|O(1)|
len(S)|len(L)|O(1)|

- In my example, adapter design pattern is applied to modify \_\_len\_\_(self) method

### Analysis of the Array-Based Stack 
- top, is_empty, len : index reference => constatant time O(1)
- push and top are amortized boudns => O(1) 
    - (Chapter5...needs to be updated...)
    
Stack Method|Python List Method|Big-O|
----------|----------|-----------| 
S.push(e) |L.append(e)|O(1)|
S.pop(e) |L.pop(e)|O(1)|
S.top() |L\[-1\] |O(1)|
S.is_empty() |len(L)==0|O(1)|
len(S)|len(L)|O(1)|


- Example Practiced Date
    - Matching Markup : 0429 







