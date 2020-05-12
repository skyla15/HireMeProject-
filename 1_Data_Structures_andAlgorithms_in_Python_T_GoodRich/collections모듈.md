## Collections - Contatiner Datatypes 
1. deque : Explained and Implemented in [Chater6_Stack_Queues_Deques](https://github.com/skyla15/HireMeProject-/tree/master/1_Data_Structures_andAlgorithms_in_Python_T_GoodRich/Chapter6_Stacks_Queues_Deques) [Methods](# collections.deque)
2. [namedtuple() : Factory function for creating tuple subclass with named  fields](#namedtuple)
3. [Counter : dict subclass for counting hashable objects(dictionary objects)](#Counter)
4. [OrderedDict : dict subclass that remembers the order entries were added](#OrderedDict)
5. [defaultdict : dict subclass that callsea factory function to supply missing values (+ dict.setdefault(key,default)  vs collections.defaultdict() )](#defaultdict)
6. 참고 자료 
   - [Collections](https://ddanggle.gitbooks.io/interpy-kr/ch12-Collections.html)

#### namedtuple
#### - collections.namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)

- rename : if set to True, invalid filed names are automatically replaced with positional names 
  - invalid field_names are 'reserved keywords', 'duplecate filed name'
  - Ex) field_names = ['abc', 'def', 'abc']  => ['abc', _1, _2]
- defaults : the *defaults* are applied to the rightmost parameters 
  - Ex) filed_names = ['x', 'y', 'z'] and defaults = (1,2) 
    - x will be a required argument, y will default to 1, z to 2 

- 키워드로 접근할 수 있는 이름을 갖는 튜플 생성 ( 튜플 클래스의 서브클래스 )

~~~python
import collections
Point = collections.namedtuple('NT', ['a','b'])
p = Point(1,2)
print('p : {}   p.a : {}    p.a+p.b : {}'.format(p, p.a, p.a+p.b))
# p : NT(a=1, b=2)   p.a : 1    p.a+p.b : 3
~~~

- Methods 

  - namedtuple._make(iterable) : 기존의 시퀀스 객체나, 반복가능한 객체로 부터 새로운 namedtuple 객체 생성 

     ~~~python
     t = [11, 22]
     p = p._make(t)
     print(p)
     # NT(a=11, b=22)
     ~~~

  - namedtuple._asdict() : 키워드와 값을 쌍으로 갖는 딕셔너리를 반환 

     - 3.1 ~ 3.7 버전 : OrderedDict 반환 
     - 3.8 ~ 버전 : 일반 dict 반환 

     ~~~python
     p = p._asdict() 
     print(p)
     # OrderedDict([('a', 100), ('b', 200)])
     ~~~

  - namedtuple._replace(**kwargs)

     - 네임드튜플의 특정 필드의 값을 수정할 때 사용 
     - 일반적인 상황에서는 필드 네임으로 접근하면 되지만 
       아래와 같이 데이터가 복잡하게 되있는 경우, 튜플들의 값을 수정하는 데 사용 

       ~~~python
       for partnum, record in inventory.items():
       	 inventory[partnum] = record._replace(price=newprices[partnum], timestamp=time.now())
       ~~~

  - namedtuple._fields

     - View the filed names of the namedtuple 

       ~~~python
       p._fields 
       # ('a', 'b')
       ~~~

  - namedtuple._field_defaults 

     - View the dictionary mapping filed to default values 

       ~~~python
       Account = namedtupe('AC', ['type', 'balance'], defaults = [0])
       Account._fied_defaults 
       # {'balance': 0}
       ~~~

       

- Useful for assigning field names to result tuples returned by the csv or sqlite3 modules

  ~~~python
  EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')
  
  import csv
  for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
      print(emp.name, emp.title)
  
     
  import sqlite3
  conn = sqlite3.connect('/companydata')
  cursor = conn.cursor()
  cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
  for emp in map(EmployeeRecord._make, cursor.fetchall()):
      print(emp.name, emp.title)
  ~~~

___

#### Counter
#### - class collections.Counter([iterable-or-mapping])[¶](https://docs.python.org/ko/3.8/library/collections.html#collections.Counter)

- It is a collection where elements are stored as dictionary __keys and their counts are stroede as dictionary__ values.

  - Counter(literal or mapping) : 반복가능한 객체의 갯수를 세는 데 사용 

  ~~~python
  from collections import Counter
  Counter()                           # a new, empty counter
  Counter('gallahad')                 # a new counter from an iterable
  Counter({'red': 4, 'blue': 2})      # a new counter from a mapping(iterable)
  Counter(cats=4, dogs=8)             # a new counter from keyword args(iterable)
  Counter(['eggs', 'ham'])						# a new counter from list(iterable)
  '''
  Counter()
  Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
  Counter({'red': 4, 'blue': 2})
  Counter({'dogs': 8, 'cats': 4})
  Counter({'eggs': 1, 'ham': 1})
  '''
  
  ~~~

  - Counter 객체는 딕셔너리 인터페이스를 사용하지만, 없는 키값을 호출할 경우, 에러 대신 0을 반환 

    ~~~python
    c = Counter(['eggs', 'ham'])						# a new counter from list(iterable)
    print( c['bacon'] )
    # 0
    ~~~

    

- Class Method
  - Counter.elements() : 각 아이템들의 갯수만큼 반복해주는 "이터레이터" 반환. 카운트가 0인 것은 무시 
    ~~~python
    c = Counter({'red':4, 'blue':2, 'yello':0})
    print(list(c.elements))
    # ['red', 'red', 'red', 'red', 'blue', 'blue']
    ~~~
  - Counter.most_commn(n) : return a list of the n most common elements and their counts 
    ~~~python
    Counter('abracadabra').most_common(3)
    [('a', 5), ('b', 2), ('r', 2)]
    ~~~
  - Counter.subtract[iterable-or-mapping]
    ~~~ptyhon
    c1 = collections.Counter('hello python')
    c2 = collections.Counter('i love python')
    c1.subtract(c4)
    print(c3) 
    '''
    Counter({'l': 1, 'h': 1, 'n': 0, 't': 0, 'p': 0, 'e': 0, 'o': 0, 'y': 0, 'i': -1, 'v': -1, ' ': -1})
    '''
    
    c3 = Counter(a=4, b=2, c=0, d=-2)
    c4 = Counter(a=1, b=2, c=3, d=4)
    c3.subtract(d)
    print(c3)
    '''
    Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
    ''' 
    ~~~
  - The most commn patterns with Counter objects

    ~~~python
    sum(c.values())                 # total of all counts
    c.clear()                       # reset all counts
    list(c)                         # list unique elements
    set(c)                          # convert to a set
    dict(c)                         # convert to a regular dictionary
    c.items()                       # convert to a list of (elem, cnt) pairs
    Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
    ~~~

___

#### OrderedDict
#### - class collections.OrderedDict([items])[¶](https://docs.python.org/ko/3.8/library/collections.html#collections.OrderedDict)

- An OrderedDict() remembers the order of key addition and returns them in the same order from an iterator.

  ~~~python
  from collections import OrderedDict
  quotes = OrderedDict([
  ('Moe', 'A wise guy, huh?'),
  ('Larry', 'Ow!'),
  ('Curly', 'Nyuk nyuk!'),
  ])
  
  for stooge in quotes:
  	print(stooge)
  """
  	Moe
  	Larry
  	Curly
  """
  ~~~

- From Python 3.7, regular dict gained the ability to remember insertion oreder, however

  - OrderedDict is more efficient when it comes to frequent re-ordering (memory ..) => Cache
  - OrderedDict has additonal method 'popitem', 'move_to_end'
    - OrderedDict.pop(last=True) 
      - last = True : FIFO 
      - last = False : LIFO 
    - OrderedDict.move_to_end(key, last=True)
      - last = True : move an existing key to the right end 
      - last = False : move an existing key to the left end 

- `sorted`(*iterable*, ***, *key=None*, *reverse=False*)[¶](https://docs.python.org/ko/3/library/functions.html#sorted) 

  - key = iterable의 인자 1개를 받는 데 사용하는 '함수'

    - 람다로 사용하거나 아래와 같이 사용 

  - reverse = Flase : 오름차순 , True : 내림차순 

    ~~~python
    d = OrderedDict.fromkeys('abcde')
    d.move_to_end('b')
    ''.join(d.keys())
    # 'acdeb'
    d.move_to_end('b', last=False)
    ''.join(d.keys())
    # 'bacde'
    ~~~

    

- 일반 dict : 키 혹은 값을 기준으로 정렬하기  

  ~~~python
  names = {'C':10, 'B':20, 'F':30, 'D':40 }
  
  def f1(x):
     return x[1] 	# x[1] : 값을 기준으로.
  
  res = sorted(names.items()) # 키를 기준으로 정렬
  print(res)
  # [('B', 20), ('C', 10), ('D', 40), ('F', 30)]
  
  res = sorted(names.items(), key=f1) # 값을 기준으로 정렬
  print(res)
  # [('C', 10), ('B', 20), ('F', 30), ('D', 40)]
  
  res = sorted(names.items(), key = (lambda x : x[1]), reverse = False) # 값을 기준으로 정렬
  print(res)
  # [('C', 10), ('B', 20), ('F', 30), ('D', 40)]
  ~~~

___


#### defaultdict
#### -class collections.defaultdict([*default_factory*[, *...*]])

- The first agument of the defaultdict provides the initial value for the default_factory attribute(default = None) 

- Class attribute and methods 

  - Default_factory

    - defaultdict() 인자로 생성자에서 초기화 됨 
    - 모든 키에 대해 "기본값"으로 사용되는 인자
    - \__missing__()을 통해 호출되고, 기본값은 None. 아래 참고 

  - defaultdict.\__missing__(key) 

    - Only called by  \__getitem__ method.

    -  When 'default_factory' attribute is None, this raises a KeyError.

    - ~~~python
      group = defaultdict() 	# default_factory = None 
      group.__getitem__(0)
      #     group.__getitem__(0)
      # KeyError: 0
      group
      # defaultdict(None, {})
      ~~~

    - When 'default_factory' attribute is not None, default_factory is used for the value of the key 

      ~~~python
      group = defaultdict(int)	# default_factory = int() 
      group.__getitem__(0)	
      # 0
      group
      # defaultdict(<class 'int'>, {0: 0}) 
      ~~~

      

- 사전의 기본값 처리하기 ( dict.setdefault  vs  collections.defaultdict )

  - dict.setdefault 

    - for 루프에서 setdefault 함수가 무조건 호출되므로, 약간의 성능저하가 발생할 수 있음 

    ~~~python
    def countLetters(word):
        counter = {}
        for letter in word:
            counter.setdefault(letter, 0)
            counter[letter] += 1
        return counter
    ~~~

  - collections.defaultdict

    - 사전 기본값으로 0 세팅하기 
    - collections의 defaultdict 클래스의 생성자로 기본값을 생성해주는 '함수( int(), lambda: 0)'를 넘기면 모든 키에 대해 값이 없는 경우 자동으로 생성자의 인자로 넘어온 함수를 호출하여 함수의 결과값을 키의 값으로 지정 

    ~~~python
    from collections import defaultdict
    
    def countLetters(word):
        counter = defaultdict(int) # int 함수 : 기본적으로 0을 설정 
      # counter = defaultdict(lambda: 0)  
        for letter in word:
            counter[letter] += 1
        return counter
    # defaultdict(<class 'int'>, {'g': 2, 'a': 2, 'l': 2, 'w': 1, 'y': 1, ' ': 1, 'i': 1, 'r': 1})
    ~~~

  - 사전 기본값으로 빈 세트(집합) 세팅하기 

    ~~~python
    from collections import defaultdict
    
    def groupWords(words):
        grouper = defaultdict(set)
        for word in words:
            length = len(word)
            grouper[length].add(word)
        print(grouper)
    
    words=['galway', 'galway', 'my', 'girl']
    groupWords(words)
    # defaultdict(<class 'set'>, {6: {'galway'}, 2: {'my'}, 4: {'girl'}})
    ~~~

    

  - 사전 기본값으로 빈 리스트 세팅하기 

    - 데이터를 특정 기준에 의해 카테고리로 묶을 수 있음 

    ~~~python
    from collections import defaultdict
    
    def groupWords(words):
        grouper = defaultdict(list)
        for word in words:
            length = len(word)
            grouper[length].append(word)
        print(grouper)
    
    words=['galway', 'galway', 'my', 'girl']
    groupWords(words)
    # defaultdict(<class 'list'>, {6: ['galway', 'galway'], 2: ['my'], 4: ['girl']})
    ~~~

#### collections.deque 

- Methods
  ~~~python
  D = collections.deque		
  D.len							# return # of elements 
  D.appendleft(e)		# add to beginning 
  D.append(e)				# add to end
  D.popleft()				# remove first element
  D.pop()						# remove last element 										
  D[0]							# access first element
  D[-1]							# access last element
  D[j]							# access arbitrary entry by index ( O(n) )
  D[j] = val				# access arbitrary entry by index ( O(n) )
  D.clear()				
  D.rotate(k)				# Circularly shift rightward k steps
  D.remove(e)				# remove the first matching element
  D.count(e)				# count the number of matches for e
  ~~~

  

