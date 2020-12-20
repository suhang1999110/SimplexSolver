# SI152_Project
This is the final project of SI152 Numerical Optimization

## Project Description

Implement a primal simplex method for solving the standard form of linear programming.

![](https://latex.codecogs.com/gif.latex?\min_{x\in%20\mathbb{R}^{n}}c^{T}x%20\quad%20\\%20s.t.\quad%20Ax%20=%20b,%20\quad%20x%20\ge%200)
where 
![](https://latex.codecogs.com/gif.latex?A%20\\in%20\\mathbb{R}^{m\\times%20n},%20c%20\\in%20\\mathbb{R}^{n})
and
![](https://latex.codecogs.com/gif.latex?b%20\in%20\mathbb{R}^{m})
You can implement either the classic primal simplex method or the revised simplex method. You may need a first-phase to find basic feasible solution to initialize your algorithm.

Notice the following aspects:
* Your implementation could be in either python/matlab
* It is understandable your implementation is simply a prototype. However, it is your duty to make your codes "user-friendly" as much as possible
* After successfully solving a linear problem, your code should output the "primal-dual optimal solution".
* Your final report should be neat and well written.
