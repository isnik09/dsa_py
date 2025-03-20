# Backtracking
- [Backtracking](#backtracking)
  - [What is backtracking?](#what-is-backtracking)
  - [How it is different from Recursion?](#how-it-is-different-from-recursion)
  - [How backtracking works?](#how-backtracking-works)
  - [Pass by reference or changes in place](#pass-by-reference-or-changes-in-place)
  - [Blueprint to solve backtracking](#blueprint-to-solve-backtracking)
  - [When to use backtracking?](#when-to-use-backtracking)
    - [USE](#use)
    - [NOT](#not)

## What is backtracking? 
- Backtracking is an algorithmic approach for solving the problems by trying to build a solution incrementally, one piece at a time, and making changes to the state of the problem in place. it involves removing those solutions that fail to satisfy the constraints of the problem at any point in time, differentiating it from pruned recursion by the way it reverts state changes when backtracking. 
- Solutions are built step by step using recursion. 
- If a path doesn't  lead to a solution or violates the constraints then it is abandoned. 
- TLDR : 
  - It is controlled recursion 
  - we make changes in place using pass by reference.

## How it is different from Recursion? 
Recursion is recursion 
in backtracking we keep track of inputs and use different approach when we can't get the desired output

## How backtracking works? 
- Explore one option 
- Keep building the solution with recursion
- if condition is violated then use different path
- else it is valid solution, return it


## Pass by reference or changes in place

## Blueprint to solve backtracking 

```
fn(){
  if solved ==> save the soln 
                return 
                (it is base condition)

  for choice in choices {
    if isValid(choice){
      choose
      helper()
    }revert choice ==> (this is backtracking part)
  }
  helper()
}
```

## When to use backtracking? 
### USE
- Use when problem requires you to see all possible paths 
- There are multiple solutions and you want all of them
  
### NOT 
- Not for optimization problems
  