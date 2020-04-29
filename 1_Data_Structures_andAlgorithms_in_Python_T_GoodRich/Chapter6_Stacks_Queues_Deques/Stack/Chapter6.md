# Stack ( Last In First Out, LIFO )
- Internet Web browsers store the address of recently visited sites
- Test Editors' 'undo' function 
  
### ADT
- S.push(e) : Add element e to the top of the S
- S.pop() : Remvoe and Return the top 
- S.top() : Return a reference to the top 
- S.is_empty() : Return True if S is empty, otherwise False
- len(S) : Return the number of e in S
  
### Python Implicit Functions 
- list.append(e) : add an e to the end 
- list.pop() : delete and return the last e 
  
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
  
### Reversing Data  






 
