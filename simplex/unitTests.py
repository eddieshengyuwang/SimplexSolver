from simplex import sef, print_lp
from linearProgram import LinearProgram
import unittest
import numpy as np

np.set_printoptions(threshold=np.nan)

typeMin = 'min'
typeMax = 'max'

obj1 = np.array([[1],[1],[-9]])
matrix1 = np.array([ [-1,0,2], [2,-3,4] ])
ineq1 = np.array([['&le;'], ['=']])
b1 = np.array([[10],[5]])
vars1 = np.array([['free'], ['&le; 0'], ['&ge; 0']])
LP1 = LinearProgram(typeMax, obj1, matrix1,
                    ineq1, b1, vars1)

sol_obj1 = np.array([[1],[-1],[-1],[-9],[0]])
sol_matrix1 = np.array([ [-1,1,0,2,1], [2,-2,3,4,0] ])
sol_ineq1 = np.array([['='], ['=']])
sol_b1 = np.array([[10],[5]])
sol_vars1 = np.array([['&ge; 0'], ['&ge; 0'], ['&ge; 0'], ['&ge; 0'], ['&ge; 0']])
sol_LP1 = LinearProgram(typeMax, sol_obj1, sol_matrix1,
                        sol_ineq1, sol_b1, sol_vars1)

#----------------------------------------------------------------------

obj2 = np.array([[3], [2], [-1], [1]])
matrix2 = np.array([[1, 2, 1, -1],  
                    [-2, -4, 1, 1]])
ineq2 = np.array([['&le;'], ['&le;']])
b2 = np.array([[5],[-1]])
vars2 = np.array([['&ge; 0'], ['&le; 0'], ['free'], ['free']])
LP2 = LinearProgram(typeMax, obj2, matrix2, ineq2, b2, vars2)

sol_obj2 = np.array([[3],[-2],[-1],[1],[1],[-1],[0],[0]])
sol_matrix2 = np.array([[1,-2,1,-1,-1,1,1,0],
                       [-2,4,1,-1,1,-1,0,1]])
sol_ineq2 = np.array([['='],['=']])
sol_b2 = np.array([[5],[-1]])
sol_vars2 = np.array([['&ge; 0'],['&ge; 0'],['&ge; 0'],['&ge; 0'],
                      ['&ge; 0'],['&ge; 0'],['&ge; 0'],['&ge; 0']])
sol_LP2 = LinearProgram(typeMax, sol_obj2, sol_matrix2,
                        sol_ineq2, sol_b2, sol_vars2)

#----------------------------------------------------------------------
obj3 = np.array([[1],[1],[-4],[-9]])
matrix3 = np.array([[-1,0,2,5],
                    [2,-3,4,-3],
                    [-1,9,-5,7],
                    [-1,-3,4,-9]])
ineq3 = np.array([['&le;'], ['&ge;'], ['&ge;'], ['=']])
b3 = np.array([[10],[5],[-7],[0]])
vars3 = np.array([['&ge; 0'], ['free'], ['&le; 0'], ['free']])
LP3 = LinearProgram(typeMin, obj3, matrix3,
                    ineq3, b3, vars3)

sol_obj3 = np.array([[-1],[-1],[1],[-4],[9],[-9],[0],[0],[0]])
sol_matrix3 = np.array([[-1,0,0,-2,5,-5,1,0,0],
                        [2,-3,3,-4,-3,3,0,-1,0],
                        [-1,9,-9,5,7,-7,0,0,-1],
                        [-1,-3,3,-4,-9,9,0,0,0]])
sol_ineq3 = np.array([['='], ['='], ['='], ['=']])
sol_b3 = np.array([[10],[5],[-7],[0]])
sol_vars3 = np.array([['&ge; 0'], ['&ge; 0'],
                      ['&ge; 0'], ['&ge; 0'],
                      ['&ge; 0'], ['&ge; 0'],
                      ['&ge; 0'], ['&ge; 0'],
                      ['&ge; 0']])
sol_LP3 = LinearProgram(typeMax, sol_obj3, sol_matrix3,
                        sol_ineq3, sol_b3, sol_vars3)

#----------------------------------------------------------------------
obj4 = np.array([[100],[200]])
matrix4 = np.array([[11,12],
                    [21,22]])
ineq4 = np.array([['&le;'], ['&ge;']])
b4 = np.array([[2000],[1000]])
vars4 = np.array([['&ge; 0'], ['free']])
LP4 = LinearProgram(typeMax, obj4, matrix4,
                    ineq4, b4, vars4)

sol_obj4 = np.array([[100],[200],[-200],[0],[0]])
sol_matrix4 = np.array([[11,12,-12,1,0],
                    [21,22,-22,0,-1]])
sol_ineq4 = np.array([['='], ['=']])
sol_b4 = np.array([[2000],[1000]])
sol_vars4 = np.array([['&ge; 0'], ['&ge; 0'], ['&ge; 0'], ['&ge; 0'], ['&ge; 0']])
sol_LP4 = LinearProgram(typeMax, obj4, matrix4,
                    ineq4, b4, vars4)
sol_LP4 = LinearProgram(typeMax, sol_obj4, sol_matrix4,
                        sol_ineq4, sol_b4, sol_vars4)

#----------------------------------------------------------------------
obj5 = np.array([[1],[2],[3],[4]])
matrix5 = np.array([[3,1,-2,0],
                    [4,-3,1,2],
                    [1,-4,2,3]])
ineq5 = np.array([['&le;'], ['&ge;'], ['=']])
b5 = np.array([[10],[13],[8]])
vars5 = np.array([['free'], ['&le; 0'], ['&ge; 0'], ['&ge; 0']])
LP5 = LinearProgram(typeMin, obj5, matrix5,
                    ineq5, b5, vars5)

sol_obj5 = np.array([[-1],[1],[2],[-3],[-4],[0],[0]])
sol_matrix5 = np.array([[3,-3,-1,-2,0,1,0],
                        [4,-4,3,1,2,0,-1],
                        [1,-1,4,2,3,0,0]])
sol_ineq5 = np.array([['='], ['='], ['=']])
sol_b5 = np.array([[10],[13],[8]])
sol_vars5 = np.array([['&ge; 0'], ['&ge; 0'], ['&ge; 0'], ['&ge; 0'],
                      ['&ge; 0'], ['&ge; 0'], ['&ge; 0']])
sol_LP5 = LinearProgram(typeMax, sol_obj5, sol_matrix5,
                        sol_ineq5, sol_b5, sol_vars5)
#------------------------------------------------------------------------
obj6 = np.array([[-8],[-10],[-7]])
matrix6 = np.array([[1,3,2],
                    [-1,-5,-1]])
ineq6 = np.array([['&le;'], ['&ge;']])
b6 = np.array([[10],[-8]])
vars6 = np.array([['&ge; 0'], ['&ge; 0'], ['&ge; 0']])
LP6 = LinearProgram(typeMin, obj6, matrix6,
                    ineq6, b6, vars6)

sol_obj6 = np.array([[8],[10],[7],[0],[0]])
sol_matrix6 = np.array([[1,3,2,1,0],
                    [-1,-5,-1,0,-1]])
sol_ineq6 = np.array([['='], ['=']])
sol_b6 = np.array([[10],[-8]])
sol_vars6 = np.array([['&ge; 0'], ['&ge; 0'], ['&ge; 0'],
                  ['&ge; 0'], ['&ge; 0']])
sol_LP6 = LinearProgram(typeMax, sol_obj6, sol_matrix6,
                    sol_ineq6, sol_b6, sol_vars6)
#------------------------------------------------------------------------

class TestSEF(unittest.TestCase):

    def sef_equal(self, LP1, LP2):
#        yo1 = LP1
#        yo2 = LP2
        np.testing.assert_equal(LP1.obj, LP2.obj)
        np.testing.assert_equal(LP1.matrix, LP2.matrix)
        np.testing.assert_equal(LP1.ineq, LP2.ineq)
        np.testing.assert_equal(LP1.b, LP2.b)
        np.testing.assert_equal(LP1.vars, LP2.vars)
    
    def test_sef1(self):
        newLP1 = sef(LP1)
        self.sef_equal(newLP1, sol_LP1)     
        
    def test_sef2(self):
        newLP2 = sef(LP2)
        self.sef_equal(newLP2, sol_LP2)

    def test_sef3(self):
        newLP3 = sef(LP3)
        self.sef_equal(newLP3, sol_LP3)
        
    def test_sef4(self):
        newLP4 = sef(LP4)
        self.sef_equal(newLP4, sol_LP4)
        
    def test_sef5(self):
        newLP5 = sef(LP5)
        self.sef_equal(newLP5, sol_LP5)
        
    def test_sef6(self):
        newLP6 = sef(LP6)
        self.sef_equal(newLP6, sol_LP6)
        
class TestSEF2(unittest.TestCase):

    def sef_equal(self, LP1, LP2):
#        yo1 = LP1
#        yo2 = LP2
        np.testing.assert_equal(LP1.obj, LP2.obj)
        np.testing.assert_equal(LP1.matrix, LP2.matrix)
        np.testing.assert_equal(LP1.ineq, LP2.ineq)
        np.testing.assert_equal(LP1.b, LP2.b)
        np.testing.assert_equal(LP1.vars, LP2.vars)
        
    def test_sef1(self):
        newLP1 = sef(LP1)
        self.sef_equal(newLP1, sol_LP1)   

if __name__ == '__main__':
    unittest.main(exit=False)
