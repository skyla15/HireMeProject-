# Deque ( Deouble-ended Queue ) 

- This can be applied to a circumstance where __the first person__ in a queue in a restaurant might be removed from the queue only to find no tables vacnant or __the last person__ in the queue becomes impatient and leaves the restaurant 
- So much so that the book has the detail of an ArrayDeque implementation in Exercise __P-6.32__ 
### ADT
- D. add_first(e)
- D.add_last(e)
- D.delete_first()
- D.delete_last()
- D.first()
- D.last()
- D.is_empty()
- len(D)
### 6.3 Implementing Deque with Circular Array 

> __add_last(e)__ equals __enqueue(e)__ and __delete_first()__ equals __dequeue()__ 

>  add_first() and delete_last() only need a little bit of modification of methods above 

- The element at the __back__ of a deque can be accessed with an index 
  - back = (self.\_front + self.\_size -1) % len(self.\_data)
- The element at the __front__ of a deque can be accessed with an index 
  - front = (self.\_front + self.\_size -1) % len(self.\_data)
- add_last() : insert an element, __double the size__ at full capacity 
  - Insert new element at the back by using a modulo operation 
    - back = (self._front + self._size)%len(self._data)
      - Take, Capacity 10, current size 3, front at index 5 => status : q[5] q[6] q[7] 
      - The last index takes a place at 7 ( 5 + 3 - 1), therefore the next available index is 8, which is ( 5 + 3 ). I use modulo operation to wrap-around the queue
- delete_first() : return and remove an element at the front. 

  - Space usage has to be 𝜣(n) to be  a desirable queue implementation
    - __A robust apporaoch __
      - __To reduce the array to half of its current size, whenever the number of elements stored in it falls below one fourth of its capacity__
- Delete_last()

___

### Analysis of the Array-Based Queue implementation 
- Except for the _resize utility ( O(n) ), all of the ADT ( O(1) )relies on a constant number of statements involving 
- __arithmetic operations, compararisons, assignments __ 

Stack Method|Python List Method|Big-O
----------|----------|-----------
Q.enqueue(e) |[Queue Implementation](6.2.2. Array-Based Queue Implementation)|O(1)
Q.dequeue(e) |[Queue Implementation](6.2.2. Array-Based Queue Implementation)|O(1)
Q.first() |\_data[self._front] |O(1)
Q.is_empty() |\_size == 0|O(1)
len(Q)|_size|O(1)
Q._resize()|[Queue Implementation](6.2.2. Array-Based Queue Implementation)|O(n)<br />Space Usage : 𝜣(n)

- Reference : page 200 on the book, Excercise C-5.16 ~ 5.20 









