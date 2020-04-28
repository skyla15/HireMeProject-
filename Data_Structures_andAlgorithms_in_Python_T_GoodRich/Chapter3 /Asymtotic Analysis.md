[Khan Academy(Korean)](https://ko.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/big-o-notation)    

### Primitive Operations
- Primitive opration corresponds to a low-level instruction with an execution time that is constant 
  - Assigning an identifier to an object 
  - Determining the object associated with an identifier 
  - Performing an arithmetic operation ( +, * ... ) 
  - Accessing a single element of a Python list by index 
  - Calling a function 
  - Returning from a function 

- Nested Loop  
  -
The quadratic function can arise in the context of nested loops where the first iteration of a loop uses one operation, the second uses two operations, the third uses three operations, and so on. That is, the number of operations is
1+2+3+···+(n−2)+(n−1)+n. => n(n+1)/2 

- Comparing Growth Rates 
  
- O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^3) < O(a^n) 
  
- Asymptotic Analysis ( implies n grows to infinity, n 값이 무한정으로 커질 경우에 점근적인 상한,하한,중간값 )
  - Big-O Notation ( Upper Boundary, the given function f(n) is always below O(g(n) )
    - Given a function g(n), f(n) <= c*g(n), namely, f(n) is "less than or equal to" c*g(n), f(n) is O(g(n))  
    - Constants can be ignored. g(n) = 2n + 7, O(n) << hen there is n inputs, an algorithm calculates 2n + 7 times  >>
    - 5n^4 +3n^3 +2n^2 +4n+1 is O(n4) because 5n^4 + 3n^3 + 2n^2 + 4n + 1 ≤ ( 5 + 3 + 2 + 4 + 1)n^4 = c*n^4.   g(n) = n^4, O(g(n)) = n^4 
  - Big-Omega(𝞨) ( Lower Boundary, the given function f(n) is always above 𝞨(g(n)) ) 
    - given a function g(n), f(n) >= c*g(n), namely, f(n) is "greater than or equal to" c*g(n), f(n) is 𝞨(g(n)) 
    - 3n log n − 2n is Ω(n log n) because 3nlogn−2n = nlogn+2n(logn−1) ≥ nlogn, g(n) = nlogn, 𝞨(g(n)) = 𝞨(nlogn)
  - Big-Theta(𝜣) 
    - given a function g(n), for a constant c', c'', if c'g(n) <= f(n) <= c''g(n), f(n) is 𝜣(g(n)) 
    - 3nlogn+4n+5logn is Θ(nlogn) because 3nlogn ≤ 3nlogn+4n+5logn ≤ (3+4+5)nlogn 
    
    
### Example of Algorithm Analysis 
#### Constant-Time Operations 
- Random Access Machine(RAM) : 프로그램 카운터 등으로 접근할 수 있는 메모리. 컴퓨터 램(Random Access Memory 아님)
  - 𝜣(1)
  - computing ( +, -, *, /, &, |, ^ ) on regiters 
  - store regiester into memory @some place 
- List, a call to a function, len(data)
  - Using index, the computer hardware supports constant-time access to an element based on its memory address. Therefor we say the data[j] is evaluated in O(1) time.
  - For each list, there is an instance variable that records the length of the current list. This allows it to immediately report that length without iteration of the list. 
  - Function call is also stored in Stack memory, which means it can also be accessed using memory index -> O(1) time 

#### Revisiting the Problem of Finding the Maximum of a sequence 

~~~python
def find_max(data):
 ”””Return the maximum element from a nonempty Python list.”””
	biggest = data[0]			# The initial value to beat
						# initialization ( O(1) ), 1개 인덱스 접근 
	for val in data:			# For each value	( O(n) )
		if val > biggest:		# if it is greater than the best so far
			biggest = val		# we have found a new best so far
	return biggest				# when loop ends, biggest is the max 
						# return 		( O(1) )
  # f(n) = n + 2 <= g(n) = c*n
  # find_max 함수는 O(g(n)) = O(n)
~~~

- If the data was in increasing order, the biggest value is reassigned n-1 times. ( O(n) )
- If the data was in random order, the probability of the 4th element is the large of the first j elements is 1/j. the expected number of tiems we update the biggest is Hn = ∑1/j ( j=1..n). Hn is the Harmonic Number and it is evaluated to  logn + Θ(1). Hence, O(logn)
-  data in increasing order -> O(n), random order -> O(logn)



#### Prefix_Average

###### Quadratic Time

~~~python
def prefix_average1(S):
    n = len(S)			# Assignment of n with len -> constant * 2 => O(1)
    A = [0] * n                 # Assignment of list with length n 
    				# with all entries equal to zero 
      				# Constant number of primitive operation per element
        			# n * 1 => O(n)
    for j in range(n):
        total = 0		# total is initialized n times O(n)
        for i in range(j+1):    # 1, 2, ...., n times executed -> n(n+1)/2
            total += S[i]          
        A[j] = total / (j + 1)	# executed n times, O(n)
        			# f(n) = 2 + n + 2n + n(n+1)/2 => O(n^2)
        

def prefix_average2(S):
    n = len(S)				# Assignment of n with len -> constant * 2 => O(1)
    A = [0] * n                		# O(n) 위와 같음
    for j in range(n):			# 함수와 슬라이싱 사용으로 큰 차이 안남. 
        A[j] = sum(S[0:j+1]) / (j + 1)  # sum function call -> O(j+1) 
        				# 슬라이스 사용 시, 새로운 리스트를 생성함
          				# Slice -> O(j+1)
            				# Therefore, 1 + 2 + 3... + n => O(n^2)
              				# f(n) = 1 + n + n(n+1)/2
# 결과값
# prefix_average1, 4.465381860733032
# prefix_average2, 0.6748650074005127 
~~~

###### Linear Time 

~~~python
def prefix_average3(S):
    n = len(S)            	# Assignment ( O(1) )
    A = [0] * n           	# O(n)
    total = 0			# Assignment ( O(1) )
    for j in range(n):
        total += S[j]        	# Arithmetic Operation ( O(1) )
        A[j] = total / (j + 1)	# Arithmetic Operation, +, /, = ( 3, O(1) )
				# * n times 
          			# O(n)
         			# f(n) = 1 + 1 + 1 + 3n => O(n)
# 결과값
# prefix_average3, 0.0021581649780273438
~~~



#### Three-Way Set Disjointness 

~~~python
# O(n^3)
def set_1(A, B, C):
    for a in A:					
        for b in B:
            for c in C:
                if a == b == c:		# Worst-case running time is O(n#)
                    return False
    return True
  
  
# O(n^2)
def set_2(A, B, C):
    for a in A:             		# A 루프   -> ( O(n)   )	    
        for b in B:            		# A~B 루프 -> ( O(n^2) ) 
            if a == b:        		# (a,b)가 짝을 갖는 최대 경우는 n개.
              				# a == b 검사 -> O(n^2)
                for c in C:		# if a == b -> 최대 n개,
                    if a == c:  	# 따라서 C 루프에서도 사용되는 시간은 B 루프 시간내에서 루프를 돌게됨으로
                      			# a == c 검사 또한 최대 n번, 따라서 O(n^2)
                                
                        return False
    return True

~~~

