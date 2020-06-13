## LinkedList  

1. [\__slots\_\_  와 \_\_dict\_\_](#----slots-----와----dict----)
2. [Nested Class](#Nested-Class)
3. [Linked List](#Linked-List)
4. Singly_Linked_Lists 
   - Stack 
   - Queue 
   - Cirucularly Linked List 
5. Circularly_Linked_Lists 
   - Deque 
6. Positinal List ADT 

___

### \_\_slots\_\_  와 \_\_dict\_\_

- 만약 사용되는 속성이 고정되있고, 해당 클래스의 객체가 많이 사용이 된다면 \__slots__ 를 사용하는 것이 메모리면으로 효율적이다.

- 클래스 생성시, 기본적으로 class-namespace의 인스턴스들을 built-in dict class를 통해 관리(딕셔너리형) 

  -  \__dict__ : Class의 인스턴스는 를 통해 "딕셔너리 형으로 저장되어 관리된다.
    - RAM 공간을 많이 차지함 ( 특히 해당 객체의 수가 많아질 수록 소비되는 RAM 자원이 커짐 )

  ~~~python
  class foo:
    pass 
  
  def main():
    foo1 = foo() 
    foo1.foo = 'foo'
    foo1.__dict__			# {'foo': 'foo'}
    foo1.foo					# foo
  ~~~

- \__slots__ 

  - 기존에 클래스의 인스턴스 관리를 위해 사용되던 dictionary를 고정된(fixed) set형으로 관리하여 클래스가 사용할 수 있는 속성을 제한한다.

  - 빠른 인스턴스 억세스( __Fast access to class instances__ )

    - \__dict__ 생성을 막음 

    - \__slots__ 에 추가되지 않은 속성을 사용 시 'AttributeError' 발생

  ~~~python
  class foo:
    __slots__ = 'foo'
  
  def main():
    foo1 = foo() 
    foo1.foo = 'foo'
    foo1.__dict__			# AttributeError: 'foo' object has no attribute '__dict__'
    foo1.foo					# foo 
  ~~~

___

### Nested Class 

- Nesting one class in the scope of another makes clear that the nested class exists for support of the outer class.
- Help reduce potential name conflicts because it allows for a similarly named class to exist in another context. (p. 99)

___

### Linked List 

- Difference between Array and Linked List 
  - Array : provides the more centralized representation with one large chunk of memory 
  - Linked List : relies on a more distributed representation in which a  _node_ is allocated for each element 
- Components and terms 

  - Head 
    - The pointer that represents the first node of the linked list 
    - Conventionally, explicitly denote the first node of the list 
  - Tail & Size
    - The pointer that represents the last node that haves None as its next reference 
    - To avoid the large traversal, it is commonly denoted explicitly.
    - In similar regard, keeping the track of __size__ is commonly used
  - Traversng : By starting at the head and moving from one node to another by following each node's next refererence.  
  - link hopping : Moving from one node to another  

___

### Singly Linked List 

- Insertion, Removal from a Sinlgy Linked List

  -  Inserting an element at the Head of a Singly Linked List ( O(1) )

    - Create a new node 
  - Assign its next reference to the head 
    - Assign the head rerefrence to new node 
    
    ~~~python
    def add_first(L, e):
      new_node = Node(e)
      new_node.next = L.head 
      L.head = new_node 
      L.size += 1 
    ~~~
    
    
    
  - Inserting an element at the tail of a Singly Linked List ( O(1) )

    - Create a new node
    - Assign its next reference to None
    - Set the next reference of the tail to new node 
    - Assign the tail reference to new node 

    ~~~python 
    def add_last(L, e):
      new_node = Node(e)
      new_node.next = None 
      L.tail.next = new_node
      L.tail = new_node 
      L.size += 1 # 넣어주는 것이 Traverse없이 리스트의 사이즈를 확인할 수 있음.
    ~~~

  - Removing an element from the head ( O(1) )  

    - Check if list is empty.

    - Assign head reference to the next node of head 

    - Garbage Collection will do the rest for the removed node.

      ( C++, deallocate the memory of the removed node) 

    ~~~python
    def remove_first(L):
      assert not is_empty(), 'List is empty'
      L.head = L.head.next
      L.size -= 1 
    ~~~

  - Removing an element from the last ( O(n) )

    - We can not directly access the node before the last order because tail reference only indicates the last node of the list  
      - Solution : Implement Doubly Linked List 
    - Need to traverse from the first node to the node before the last node.  

    ~~~python 
    def remove_last(L):
      assert not is_empty(), 'List is empty'
      temp = L.head
      while temp.next != None:
        temp = temp.next 
    	L.tail = temp 
      L.size -= 1 
    ~~~

- Stack 

- Queue