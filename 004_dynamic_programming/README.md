# Dynamic Programming

- [Dynamic Programming](#dynamic-programming)
  - [What is Dynamic Programming?](#what-is-dynamic-programming)
  - [Approaches](#approaches)
    - [Memorization (top down approach)](#memorization-top-down-approach)
    - [Tabulation (bottom up approach)](#tabulation-bottom-up-approach)
  - [Writing the recursive solution helps in coming up with bottom up solution?](#writing-the-recursive-solution-helps-in-coming-up-with-bottom-up-solution)
  - [How to identify DP questions?](#how-to-identify-dp-questions)


Many problems that can be solved with recursion can  be solved with DP in better way.

## What is Dynamic Programming? 
It is the method to solve complex problem where problems exhibit 
- a. Overlapping sub-problems
- b. Optimal sub-structure
  - Optimal solution can to a problem can be constructed from optimal solution of it's sub-problems

## Approaches 

- Write the recursion solution 
- Memorization / Top Down 
- Tabulation / Bottom Up 
- Space Optimization

### Memorization (top down approach)
- Starts with the original/large problem (top)
### Tabulation (bottom up approach)
- Starts with smallest subproblem first (bottom of the hierarchy)

## Writing the recursive solution helps in coming up with bottom up solution?
- ### Understanding the subproblem
  Recursive solutions inherently break down a problem into smaller sub-problems. By writing recursive solutions, we gain a clear understanding of that these sub-problems are, which is essential for any DP approach. 
- ### Transition Formula
  The recursion's base case and the way recursive calls are made help in identifying the transition formula. The formula is crucial for filling out the DP table in the bottom-up approach
- ###  Base Conditions 
  The base case in recursion translates to the initial condition in our DP table. This are crucial for the correctness of the bottom-up solution. 

## How to identify DP questions?
HINTS 
- ### You have asked to find the optimal solution 
- ### Problem involves choices