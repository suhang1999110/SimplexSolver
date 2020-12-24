import numpy as np
from functools import wraps
import time


def timer(func):
    '''
    Record running time of func
    '''
    @wraps(func)
    def _timer(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print('Elapsed time: {} seconds'.format(np.round(time.time() - start, 4)))
        return ret

    return _timer


class SimplexSolver(object):
    '''
    Simplex solver for linear programming
    '''
    def __init__(self, A, b, c):
        '''
        create a simplex solver
        params:
            A: coefficient matrix of x
            b: rhs of equality constraints
            c: cost coefficient
        '''
        A = np.array(A)
        b = np.array(b).reshape(-1,1)
        c = np.array(c).reshape(-1,1)

        self.A = A
        self.b = b 
        self.c = c

        self.basis = set()
        self.decision_vars = set()
        self.auxiliary_vars = set()
        
        # Check the dimensions of inputs
        assert A.shape[0] == b.shape[0], 'A has {} rows, but b has {} rows'.format(A.shape[0], b.shape[0])
        assert A.shape[1] == c.shape[0], 'A has {} columns, but c has {} columns'.format(A.shape[1], c.shape[0])
        assert b.shape[1] == 1, 'b is not a column vector'
        assert c.shape[1] == 1, 'c is not a column vector'

        np.set_printoptions(precision=3)


    @timer
    def solve(self, verbose=True, max_iterations=10000):
        '''
        Interface function for simplex method
        params:
            max_iterations: Max iterations of simplex method (default 10000)
        '''
        
        self.max_iterations = max_iterations
        self.verbose = verbose

        if verbose:
            print('In auxiliary problem:\n')

        tableau, iteration1 = self._initialize()

        if verbose:
            print('In primal problem:\n')
            print('Initial tableau:')
            self._print_tableau(tableau)
            print('Initial basis:')
            self._print_basis()
            print('')

        tableau, x, z, iteration2 = self._solve(tableau)

        return x, z, iteration1, iteration2


    def _solve(self, tableau):
        '''
        Run simplex method
        '''
        # Main procedure of simplex
        is_optimal = False

        for iteration in range(self.max_iterations):
            assert len(self.basis) == tableau.shape[0] - 1
            assert not np.any(tableau[:-1,-1] < 0)

            # Terminate the algorithm if optimal solution is found
            if self._terminate(tableau):
                auxiliary_basis = self.basis & self.auxiliary_vars
                if auxiliary_basis:
                    # Let one auxiliary variable leave basis
                    aux = auxiliary_basis.pop()
                    for p in range(tableau.shape[0]-1):
                        if tableau[p,aux] == 1:
                            break
                    if np.all(tableau[p,:tableau.shape[1]-1-len(self.auxiliary_vars)] == 0):
                        # Remove redundant constraint
                        tableau = np.vstack((tableau[:p,:], tableau[p+1:,:]))
                        self.basis.remove(aux)
                    else:
                        for q in range(tableau.shape[1]-1-len(self.auxiliary_vars)):
                            if tableau[p,q] != 0:
                                break
                        self.basis.remove(aux)
                        self.basis.add(q)

                        tableau = self._update(tableau, p, q)

                        if self.verbose:
                            print('Iteration #{}'.format(iteration+1))
                            print('pivot at ({},{}) is {}'.format(p+1, q+1, pivot))
                            print('tableau after pivoting:')
                            self._print_tableau(tableau)
                            print('Basis are:')
                            self._print_basis()
                            print('')

                else:
                    is_optimal = True
                    break
            else:
                p,q = self._get_pivot(tableau)

                pivot = tableau[p,q]
                for j in self.basis:
                    if tableau[p,j] == 1:
                        self.basis.remove(j)
                        break
                self.basis.add(q)
                tableau = self._update(tableau, p, q)
                
                if self.verbose:
                    print('Iteration #{}'.format(iteration+1))
                    print('pivot at ({},{}) is {}'.format(p+1, q+1, pivot))
                    print('tableau after pivoting:')
                    self._print_tableau(tableau)
                    print('Basis are:')
                    self._print_basis()
                    print('')
        
        x, z = self._get_variables(tableau)
        if self.verbose:
            if is_optimal:
                print('#'*50)
                print('Optimal solution found in {} iterations\n'.format(iteration+1))
                print('Optimal solution:')
                self._print_variables(x, z)
                print('#'*50)
            else:
                x, z = self._get_variables(tableau)
                print('#'*50)
                print('Exceed max iterations')
                print('Current solution:')
                self._print_variables(x, z)
                print('#'*50)

        return tableau, x, z, iteration


    def _initialize(self):
        '''
        Initialize algorithm to find basic feaible solution
        '''
        m, n = self.A.shape

        basis_flag = np.zeros_like(self.b)
        # Find all slack variables from input
        for i in range(n):
            if self.c[i] == 0:
                for j in range(m):
                    if self.A[j,i] == 1 and basis_flag[j] == 0:
                        self.basis.add(i)
                        basis_flag[j] = 1
                        break
            else:
                self.decision_vars.add(i)

        if len(self.basis) != m:
            return self._phase_one(basis_flag)
        else:
            tableau = np.zeros((m+1, n+1))
            tableau[:m,:n] = self.A
            tableau[:-1,-1] = self.b.squeeze()
            tableau[-1,:-1] = self.c.squeeze()
        
        return tableau, 0
        

    def _phase_one(self, basis_flag):
        '''
        Solve the auxiliary problem
        '''
        # Ensure all b > 0
        m, n = self.A.shape
        for i in range(m):
            if self.b[i] < 0:
                self.b[i] = -self.b[i]
                self.A[i] = -self.A[i]
        
        tableau = np.zeros((m+1,n+1+(m-len(self.basis))))
        tableau[:m,:n] = self.A
        tableau[:-1,-1] = self.b.squeeze()
        
        for i in set(np.arange(n)) - self.basis:
            tableau[-1,i] = -np.sum(tableau[:-1,i])        
        tableau[-1,-1] = -np.sum(tableau[:-1,-1])

        # Introduce auxiliary variables
        j = 0
        for i, flag in enumerate(basis_flag):
            if flag == 0:
                tableau[i,n+j] = 1
                self.basis.add(n+j)
                self.auxiliary_vars.add(n+j)
                j += 1

        if self.verbose:
            print('Initial tableau of auxiliary problem:')
            self._print_tableau(tableau)
            print('Initial basis:')
            self._print_basis()
            print('')


        tableau, x, z, iteration = self._solve(tableau)
        
        if abs(tableau[-1,-1] - 0) > 1e-5:
            raise Exception('Primal problem has no feasible solution!')

        primal_tableau = np.zeros((tableau.shape[0],n+1))
        primal_tableau[:m,:n] = tableau[:m,:n]
        primal_tableau[-1,:-1] = self.c.squeeze()
        primal_tableau[:-1,-1] = tableau[:-1,-1]

        # Update basis columns
        for i in self.basis:
            if primal_tableau[-1,i] != 0:
                primal_tableau[-1] -= primal_tableau[np.argmax(tableau[:-1,i])] * primal_tableau[-1,i]

        assert not np.any(tableau[:-1,-1] < 0)

        return primal_tableau, iteration


    def _get_variables(self, tableau):
        '''
        Get all current x and objectives
        '''
        x = []
        for i in range(tableau.shape[1]-1):
            if i in self.basis:
                x.append(tableau[np.argmax(tableau[:-1,i]),-1])
            else:
                x.append(0)

        return x, -tableau[-1,-1]
        

    def _update(self, tableau, p, q):
        '''
        Update tableau with given pivot
        '''
        pivot = tableau[p,q]

        # Update other rows
        for i, row in enumerate(tableau):
            if i == p:
                continue
            tableau[i] = tableau[i] - tableau[p] * tableau[i,q] / pivot

        # Divide the pivot row by pivot
        tableau[p] = tableau[p] / tableau[p,q]

        return tableau


    def _get_pivot(self, tableau):
        '''
        Get the index of pivot
        '''
        q = self._get_enter_var(tableau)
        p = self._get_leave_var(tableau, q)

        return p, q


    def _get_leave_var(self, tableau, q):
        '''
        Get leaving variable by Bland's rule
        '''
        m, n = tableau.shape[0] - 1, tableau.shape[1] - 1

        p = 0
        min_ratio = float('inf')
        for i in range(m):
            if tableau[i,q] <= 0:
                continue
            ratio = tableau[i,-1] / tableau[i,q]
            if ratio < min_ratio:
                min_ratio = ratio
                p = i
        return p


    def _get_enter_var(self, tableau):
        '''
        Get entering variable by Bland's rule
        '''
        for q, r in enumerate(tableau[-1,:-1]):
            if r < 0:
                break
        if np.all(tableau[:-1,q] <= 0):
            raise Exception('Problem is unbounded !')
        return q


    def _terminate(self, tableau):
        '''
        Determine whether the algorithm should terminate
        '''
        return np.all(tableau[-1,:-1] >= 0)


    def _print_tableau(self, tableau):
        '''
        Print current tableau
        '''
        print(tableau)


    def _print_basis(self):
        '''
        Print current basis
        '''
        for i in self.basis:
            print('x{} '.format(i+1),end='')
        print('')
        

    def _print_variables(self, x, z):
        '''
        Print all variables
        '''
        print('z  =  {}\n'.format(np.round(z,5)))
        print('Decision variables:')
        for i in self.decision_vars:
            print('x{}  =  {}'.format(i+1, x[i]))
        print('')
        if len(set(np.arange(len(x))) - self.decision_vars) != 0:
            print('Slack or Artificial variables:')
            for i in set(np.arange(len(x))) - self.decision_vars:
                print('x{}  =  {}'.format(i+1, x[i]))