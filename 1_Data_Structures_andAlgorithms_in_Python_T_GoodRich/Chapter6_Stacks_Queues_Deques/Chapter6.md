## Stack ( Last In First Out, LIFO )
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
__New Class__  
 Stack Method|Python List Method|
  ----------|----------|
  S.push(e)|L.append(e)|
  S.pop(e)|L.pop(e)|
  S.top()|L\[-1\]|
  S.is_empty()|len(L)==0|
  len(S)|len(L)|


 
