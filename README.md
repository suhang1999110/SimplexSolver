# SI152_Project
This is the final project of SI152 Numerical Optimization

## Project Description

Implement a primal simplex method for solving the standard form of linear 

$$
\min_{x\in \mathbb{R}^n}c^Tx \quad \\
s.t.\quad Ax = b, \quad x \ge 0
$$
where 
$
A \in \mathbb{R}^{m\times n}, c \in \mathbb{R}^n
$
and
$
b \in \mathbb{R}^m
$.
You can implement either the classic primal simplex method or the revised simplex method. You may need a first-phase to find basic feasible solution to initialize your algorithm.

Notice the following aspects:
* Your implementation could be in either python/matlab
* It is understandable your implementation is simply a prototype. However, it is your duty to make your codes "user-friendly" as much as possible
* After successfully solving a linear problem, your code should output the "primal-dual optimal solution".
* Your final report should be neat and well written.