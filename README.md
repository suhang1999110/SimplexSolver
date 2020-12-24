# Simplex Solver
This is the final project of SI152 Numerical Optimization

## Project Description

Implement a primal simplex method for solving the standard form of linear programming.

![](https://latex.codecogs.com/gif.latex?\min_{x\in%20\mathbb{R}^{n}}c^{T}x%20\quad%20\\%20s.t.\quad%20Ax%20=%20b,%20\quad%20x%20\ge%200)

where 
![](https://latex.codecogs.com/gif.latex?A%20\\in%20\\mathbb{R}^{m\\times%20n},%20c%20\\in%20\\mathbb{R}^{n})
and
![](https://latex.codecogs.com/gif.latex?b%20\in%20\mathbb{R}^{m})

## Dependency
Python > 3.7 (Recommended)

Numpy

## Usage

Class TestSimplex is implemented to evaluate the correctness of simplex solver for convenience.  A, b, c and x_star are required for TestSimplex.
### Data from array
``` Python
from test_simplex import TestSimplex

A = [[2,1,2],
     [3,3,1]]
b = [4,3]
c = [4,1,1]

x_star = [0,2/5,9/5]
z_star = 11/5

test = TestSimplex(A=A,b=b,c=c,x_star=x_star,z_star=z_star)
test.test(verbose=False)
```

### Data from csv
``` Python
from test_simplex import TestSimplex
test = TestSimplex(A='data/A.csv', b='data/b.csv', c='data/c.csv', 
                   x_star='data/x_star.csv')
test.test(verbose=False)
```

If you don't have optimal solution of a LP problem, you can use the class SimplexSolver to get solution directly.
```Python
from simplex import SimplexSolver

A = [[2,1,2],
     [3,3,1]]
b = [4,3]
c = [4,1,1]

solver = SimplexSolver(A, b, c)
x, z, num1, num2 = solver.solve(verbose=False, max_iterations=10000)
print('#pivots (Phase I): {}\t #pivots (Phase II): {}'.format(num1, num2))
print('z:', z)
print('x:', x)
```

**Note:** 
+ Set verbose=True will output tableau, basis and pivot of each iteration
+ Please refer to the csv files under *data* folder for csv data format
