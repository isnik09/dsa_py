# Recursion
- [Recursion](#recursion)
  - [What is recursion?](#what-is-recursion)
  - [When to use recursion?](#when-to-use-recursion)
  - [Recursive Leap of faith](#recursive-leap-of-faith)
  - [Recursion vs Iteration](#recursion-vs-iteration)
  - [Ways to write base condition](#ways-to-write-base-condition)
  - [Recurrence relation](#recurrence-relation)
 
## What is recursion? 
Function calling itself until base condition / terminating condition is validated is recursion. 

## When to use recursion? 
If we can solve the problem with dividing it into subproblem them we can solve it using recursion. 

## Recursive Leap of faith
- 1. Understand the problem
- 2. Identify subproblem 
- 3. Trust/Faith...?
  - You have to trust that this recursive call will correctly solve a smaller version of your problem. 
  - You don't try to mentally simulate or "unroll" the recursion; 
  - instead, you assume that if your function works for simpler case it will work more for more complex ones. 
- 4. Link 1. and 2. 
- 5. Base Condition

## Recursion vs Iteration 
- Things done recursively can also be done iteratively. 
- Iteration does not use recursive call stack, so it has better space complexity.
- Recursion has both ascending phase  (calling phase) and descending phase (returning phase)
- Iteration only has ascending phase.
  
## Ways to write base condition 
- Think about last valid input or first invalid input instead of thinking about entire recursion function. 


## Recurrence relation 
Express the solution of a problem as a function of the solutions to smaller instances of the same problem. 
