import numpy as np

class SimplexSolver(object):
    def __init__(self, verbose=True):
        A = []
        b = []
        c = []
        m = -1
        n = -1
        x = []
        tableau = []
        verbose = verbose
        z = -1


    def solve(self, A, b, c):
        '''
        Solve linear programming by simplex method
        params:
            A: m by n coefficient matrix of x
            b: rhs of the equality constraint
            c: coefficient matrix of cost function
        '''
        self.A = np.array(A)
        self.b = np.array(b)
        self.c = np.array(c)

        assert A.shape[0] == b.shape[0], 'A has {} rows, but b has {} rows'.format(A.shape[0], b.shape[0])
        assert A.shape[1] == c.shape[0], 'A has {} columns, but c has {} columns'.format(A.shape[1], c.shape[0])
        assert b.shape[1] == 1, 'b is not a column vector'
        assert c.shape[1] == 1, 'c is not a column vector'

        self.m, self.n = A.shape
        self.x = np.zeros((self.n,1))
        self.tableau = np.zeros((self.m+1, self.n+1))

        # Phase one
        try:
            self._initialize()
        except Exception as e:
            # primal problem is unfeasible
            print(e)
            return
        


    def _initialize(self):
        '''
        Construct auxiliary problem and find one basic feasible solution
        '''




