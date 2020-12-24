import csv
import numpy as np
from simplex import *


def test_0():
    A = [[2,1,1,1,0,0],
         [1,2,3,0,1,0],
         [2,2,1,0,0,1]]
    b = [2,5,6]
    c = [-3,-1,-3,0,0,0]
    
    x_star = [1/5, 0, 8/5, 0, 0, 4]
    z_star = -27/5

    solver = SimplexSolver(A=A, b=b, c=c)
    x, z = solver.solve()

    assert abs(z_star - z) < 1e-5, 'Not optimal solution'


def test_1():
    A = [[6, 1,-2,-1, 0, 0],
         [1, 1, 1, 0, 1, 0],
         [6, 4,-2, 0, 0,-1]]
    b = [5,4,10]
    c = [5,2,-4,0,0,0]

    x_star = [5/3, 4/3, 1]
    z_star = 3

    solver = SimplexSolver(A=A, b=b, c=c)
    x, z = solver.solve()

    assert abs(z_star - z) < 1e-5, 'Not optimal solution'


def test_2():
    A = [[1 ,  0,0,1,0,0],
         [20,  1,0,0,1,0],
         [200,20,1,0,0,1]]
    b = [1,100,10000]
    c = [-100,-10,-1,0,0,0]

    x_star = [0,0,10000]
    z_star = -10000

    solver = SimplexSolver(A=A, b=b, c=c)
    x, z = solver.solve()

    assert abs(z_star - z) < 1e-5, 'Not optimal solution'


def test_3():
    A = [[2,1,2],
         [3,3,1]]
    b = [4,3]
    c = [4,1,1]

    x_star = [0,2/5,9/5]
    z_star = 11/5

    solver = SimplexSolver(A=A, b=b, c=c)
    x, z = solver.solve()


def test_4():
    A = [[1,0,0,1/4,-8,-1,9],
         [0,1,0,1/2,-12,-1/2,3],
         [0,0,1,0,0,1,0]]
    b = [0,0,1]
    c = [0,0,0,-3/4,20,-1/2,6]

    x_star = []
    z_star = []

    solver = SimplexSolver(A=A, b=b, c=c)
    x, z = solver.solve()


def test_5():
    solver = SimplexSolver(A_path='data/A.csv', b_path='data/b.csv', c_path='data/c.csv')
    x, z = solver.solve()

    # assert abs(z_star - z) < 1e-5, 'Not optimal solution'

# test_0()
# test_1()
# test_2()
# test_3()
# test_4()
test_5()