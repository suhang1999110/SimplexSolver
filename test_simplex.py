import csv
import numpy as np
from simplex import *

class TestSimplex(object):
    def __init__(self, A, b, c, x, z=None):
        self.A = self._read_csv(A) if type(A) == str else A
        self.b = self._read_csv(b) if type(b) == str else b
        self.c = self._read_csv(c) if type(c) == str else c
        self.x_star = self._read_csv(x) if type(x) == str else x

        self.A = np.array(self.A)
        self.b = np.array(self.b)
        self.c = np.array(self.c)
        self.x_star = np.array(self.x_star)

        self.z_star = z if z else np.sum(self.c * self.x_star)


    def test(self, verbose=True, eps=1e-8):
        solver = SimplexSolver(self.A, self.b, self.c)
        x, z = solver.solve(verbose=verbose)
        error = z - self.z_star
        
        print('Simplex objective result = ', z)
        print('Optimal objective = ', self.z_star)

        if error < eps:
            print('\033[32mTest passed!\033[0m')
        else:
            print('\033[31mTest failed!\033[0m (Error = {}) '.format(error))


    def _read_csv(self, path):
        '''
        Read csv data from given path
        '''
        data = []
        with open(path, 'r')as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                data.append([float(i) for i in row])
        
        return np.array(data)


def test_0():
    A = [[2,1,1,1,0,0],
         [1,2,3,0,1,0],
         [2,2,1,0,0,1]]
    b = [2,5,6]
    c = [-3,-1,-3,0,0,0]
    
    x_star = [1/5, 0, 8/5, 0, 0, 4]
    z_star = -27/5

    print('*'*10, 'Testcase #0','*'*10)
    test = TestSimplex(A=A, b=b, c=c, x=x_star, z=z_star)
    test.test(verbose=False)


def test_1():
    A = [[6, 1,-2,-1, 0, 0],
         [1, 1, 1, 0, 1, 0],
         [6, 4,-2, 0, 0,-1]]
    b = [5,4,10]
    c = [5,2,-4,0,0,0]

    x_star = [5/3, 4/3, 1]
    z_star = 3

    print('*'*10, 'Testcase #1','*'*10)
    test = TestSimplex(A=A, b=b, c=c, x=x_star, z=z_star)
    test.test(verbose=False)


def test_2():
    A = [[1 ,  0,0,1,0,0],
         [20,  1,0,0,1,0],
         [200,20,1,0,0,1]]
    b = [1,100,10000]
    c = [-100,-10,-1,0,0,0]

    x_star = [0,0,10000]
    z_star = -10000

    print('*'*10, 'Testcase #2','*'*10)
    test = TestSimplex(A=A, b=b, c=c, x=x_star, z=z_star)
    test.test(verbose=False)



def test_3():
    A = [[2,1,2],
         [3,3,1]]
    b = [4,3]
    c = [4,1,1]

    x_star = [0,2/5,9/5]
    z_star = 11/5

    print('*'*10, 'Testcase #3','*'*10)
    test = TestSimplex(A=A, b=b, c=c, x=x_star, z=z_star)
    test.test(verbose=False)


def test_4():
    A = [[1,0,0,1/4,-8,-1,9],
         [0,1,0,1/2,-12,-1/2,3],
         [0,0,1,0,0,1,0]]
    b = [0,0,1]
    c = [0,0,0,-3/4,20,-1/2,6]

    x_star = [3/4,0,0,1,0,1,0]
    z_star = -5/4

    print('*'*10, 'Testcase #4','*'*10)
    test = TestSimplex(A=A, b=b, c=c, x=x_star, z=z_star)
    test.test(verbose=False)


def test_5():
    print('*'*10, 'Testcase #5','*'*10)
    test = TestSimplex(A='data/A.csv', b='data/b.csv', c='data/c.csv', x='data/x_star.csv')
    test.test(verbose=False)


test_0()
test_1()
test_2()
test_3()
test_4()
test_5()