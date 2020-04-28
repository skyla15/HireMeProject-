Khan Academy (Korean) 
https://ko.khanacademy.org/computing/computer-science/algorithms/asymptotic-notation/a/big-o-notation

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

- Asymptotic Analysis 
  - Big-O Notation ( The worst case, the running time is always greater than or equal to O(g(n) )
    - Given a function g(n), f(n) <= c*g(n), namely, f(n) is "less than or equal to" c*g(n), f(n) is O(g(n))  
    - Constants can be ignored. g(n) = 2n + 7, O(n) << hen there is n inputs, an algorithm calculates 2n + 7 times  >>
    - 5n^4 +3n^3 +2n^2 +4n+1 is O(n4) because 5n^4 + 3n^3 + 2n^2 + 4n + 1 ≤ ( 5 + 3 + 2 + 4 + 1)n^4 = c*n^4. g(n) = n^4, O(g(n)) = n^4 
  - Big-Omega(𝞨) ( The best case, the running time is always less than or equal to 𝞨(g(n)) ) 
    - given a function g(n), f(n) >= c*g(n), namely, f(n) is "greater than or equal to" c*g(n), f(n) is 𝞨(g(n)) 
    - 3n log n − 2n is Ω(n log n) because 3nlogn−2n = nlogn+2n(logn−1) ≥ nlogn, g(n) = nlogn, 𝞨(g(n)) = 𝞨(nlogn)
