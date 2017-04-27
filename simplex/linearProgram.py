class LinearProgram:

    def __init__(self, obj, matrix, ineq, b, vars):
        self.obj = obj
        self.matrix = matrix
        self.ineq = ineq
        self.b = b
        self.vars = vars
    
