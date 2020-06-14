# Deque ( Deouble-ended Queue ) 

- This can be applied to a circumstance where __the first person__ in a queue in a restaurant might be removed from the queue only to find no tables vacnant or __the last person__ in the queue becomes impatient and leaves the restaurant 
- So much so that the book has the detail of an ArrayDeque implementation in Exercise __P-6.32__ 
## ADT

- D. add_first(e)
- D.add_last(e)
- D.delete_first()
- D.delete_last()
- D.first()
- D.last()
- D.is_empty()
- D.resize() 
- len(D)
  - O(n) for D.resize(), O(1) for other methods 
### 6.3.2 Implementing Deque with Circular Array 

> __add_last(e)__ equals __enqueue(e)__ and __delete_first()__ equals __dequeue()__ 

>  add_first() and delete_last() only need a little bit of modification of methods above 

- Index of the back of the deque / the first available slot beyond the back
  
  - ( self.\_front + self.\_size - 1 )  % len( self.\_data )
  
- A call to __self.add\_first__ may need to wrap around the beginning of the queue 

  - self.\_front = ( self._front - 1 ) % len( self.\_data )

- add_last() : insert an element, __double the size__ at full capacity 
  
- ( self._front + self._size )%len( self._data )
  
- delete_first() : return and remove an element at the front. 

  - Space usage has to be 𝜣(n) to be  a desirable queue implementation
    - __A robust apporaoch__
      
      - __To reduce the array to half of its current size, whenever the number of elements stored in it falls below one fourth of its capacity__
      
        ~~~python
        if 0 < self._size < len(self._data) // 4:
        	self._resize(len(self._data) // 2)
        ~~~

___

### Collections Module

-  collections.deque constructor supports an optional __maxlen parameter__ to enforce a fixed-length deque
- if a call to append at either end is invoked, when a deque is full, drops an element from the opposite side. 
- It is implemented using doubly linked list 
- Collections.deque class guarantees 
  - O(1)-time operations at either end 
  - O(n)-time when using index notation near the middle of the deque

| collections.deque    | My Deque ADT     | Description                            |
| -------------------- | ---------------- | -------------------------------------- |
| len(D)               | len(D)           | return # of elementse                  |
| D.appendleft(e)      | D.add_first(e)   | add to beginning                       |
| D.appendright(e)     | D.add_last(e)    | add to end                             |
| D.popleft()          | D.delete_frist   | remove first element                   |
| D.pop()         | D.delete_last    | remove last element                    |
| D[0], D[-1] | D.first() / D.last() | access first/last element   |
| D[j], D[j] = val |  | access/modify arbitrary entry by index<br />=> __worst case : O(n)__ |
| D.clear() |         |                                        |
| D.rotate(k) |       | Circularly shift rightward k steps     |
|D.remove(e)||remove first matching element|
|D.count(e)||count the number of mathces for e|



### Analysis of the Array-Based Deque implementation 

- Except for the _resize utility ( O(n) ), all of the ADT ( O(1) ) relies on a constant number of statements involving 
  - __arithmetic operations, compararisons, assignments__ 









