import csv
import numpy as np
from simplex import *


def test_1():
    A = np.array([[6, 1,-2,-1, 0, 0],
                  [1, 1, 1, 0, 1, 0],
                  [6, 4,-2, 0, 0,-1]])
    b = np.array([[5],[4],[10]])
    c = np.array([[5],[2],[-4],[0],[0],[0]])

    x_star = np.array([[5/3], [4/3], [1]])
    z_star = np.array([3])

    solver = SimplexSolver()


def test_2():
    A = np.array([[1 ,  0,0,1,0,0],
                  [20,  1,0,0,1,0],
                  [200,20,1,0,0,1]])
    b = np.array([[1],[100],[10000]])
    c = np.array([[-100],[-10],[-1],[0],[0],[0]])

    x_star = np.array([[0],[0],[10000]])
    z_star = np.array([-10000])


def test_3():
    A = []
    b = []
    c = []
    x_star = []

    with open('data/A.csv', 'r') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            A.append([float(data) for data in row])
    with open('data/b.csv', 'r') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            b.append([float(data) for data in row])
    with open('data/c.csv', 'r') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            c.append([float(data) for data in row])
    with open('data/x_star.csv', 'r') as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            x_star.append([float(data) for data in row])

    A = np.array(A)
    b = np.array(b)
    c = np.array(c)
    x_star = np.array(x_star)


test_1()
# test_2()
# test_3()