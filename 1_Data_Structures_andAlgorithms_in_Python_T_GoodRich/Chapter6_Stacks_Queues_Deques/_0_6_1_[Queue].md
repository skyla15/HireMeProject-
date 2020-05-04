# Queue ( First-in First-out )

- Networked Printer 
- Web server responding to requests 
- Queueing theory 
  - 참고자료 : [Garbage Collector](https://github.com/skyla15/HireMeProject-/blob/master/0_Learning_Python/가비지콜렉터.md)
### ADT
- Q.enqueue(e): Add element to the back of queue Q 
- Q.dequeue(): Remove and return the front element of queue Q. Error, if empty
- Q.first(): Return a reference to the element at the front of queue Q 
- Q.is_empty(): Return True if queue Q is empty 
- len(Q): Return the number of elements in queue Q; (in Python, special method uses \_\_len__)
### 6.2. Array-Based Queue Implementation

- Inefficient implementation 
  
- Desirable property of a queue implementation is to have its space usage be 𝜣(n)
  
- Q.append(e) : add an e to the end 
  
- Q.pop(0) : delete and return the first element  
  
  - When pop(non-default) is used, __loop__ is executed to __shift all elements beyond the specified index to the left__. pop(0) : 𝜣(n) time. 
  
  - Use a reference 'f' to None and maintain the front index of the queue. O(1) time 
  
    => Size of total length of queue can be enormous because this way, I don't empty the previous fronts instead I just move the reference 'f' to the next front index. 
  
      - => Circular Queue 
  
- Circular Queue 

  - In this book, when enqueing, it uses a method to wrap around at the end of underlying array, with the front assigned to 0. 
    
    - When enqueing, double the size of the current queue, assign the front to index 0 
    
  - Advance the front index by using a modulo operation : f = ( f+1 ) % N 

  - enqueue() : insert an element, __double the size__ at full capacity 

    - Insert new element at the tail by using a modulo operation 
      - tail = (self._front + self._size)%len(self._data)
        - Take, Capacity 10, current size 3, front at index 5 => status : q[5] q[6] q[7] 
        - The last index takes a place at 7 ( 5 + 3 - 1), therefore the next available index is 8, which is ( 5 + 3 ). I use modulo operation to wrap-around the queue

  - dequeue() : return and remove an element at the front. 

    - Space usage has to be 𝜣(n) to be  a desirable queue implementation
      - __A robust apporaoch __
        - __To reduce the array to half of its current size, whenever the number of elements stored in it falls below one fourth of its capacity__

  - Robust Circular Queue : When the initial q is full, double the size of the q 

    ~~~python
        def dequeue(self):
            '''
                remove and return the element at the front
                raise exeption if q is empty
            '''
            assert not self.is_empty(), 'Q is empty'
            if 0 < self._size < len(self._data)//4:
              	self._resize(len(self._data)//2)
            # Shrink the Q, when the number of its capacity falls below one fourth of its capacity
            e = self._data[self._front]
            self._data[self._front] = None          
            # Help garbage collection ( Chapter 15 )
            self._front = (self._front + 1) % len   
            # advance the front to the next index
            self._size -= 1
            return e
          
        def enqueue(self, e):
            '''add an element to the back of queue'''
            if self._size == len(self._data):    
            # if the existing q is full, double the size  
                self._resize( 2*len(self._data))
    				# get the next available index
            tail = (self._front + self._size) % len(self._data)
            # add an element
            self._data[tail] = e                   
            # increase the size of the q
            self._size += 1                        
    
        def _resize(self, wrapover):
            '''resize a new list of capacity'''
            # Keeping the existing q
            old_data = self._data         
            # Double the size of the existing q
            self._data = [None]*wrapover    
            for k in range(self._size):     
    	          # Reassign the xisting q to the double-sized q
                self._data[k] = old_data[self._front]
                temp_front = (self.front + 1) % len(old_data)         
    				# front is realigned
            self._front = 0                 
    ~~~
    
    

___

### Analysis of the Array-Based Queue implementation 
- Except for the _resize utility ( O(n) ), all of the ADT ( O(1) )relies on a constant number of statements involving 
- __arithmetic operations, compararisons, assignments __ 

Stack Method|Python List Method|Big-O
----------|----------|-----------
Q.enqueue(e) |[Queue Implementation](6.2.-Array-Based-Queue-Implementation)|O(1)
Q.dequeue(e) |[Queue Implementation](6.2.-Array-Based-Queue-Implementation)|O(1)
Q.first() |\_data[self._front] |O(1)
Q.is_empty() |\_size == 0|O(1)
len(Q)|_size|O(1)
Q._resize()|[Queue Implementation](6.2.-Array-Based-Queue-Implementation)|O(n)<br />Space Usage : 𝜣(n)

- Reference : page 200 on the book, Excercise C-5.16 ~ 5.20 









