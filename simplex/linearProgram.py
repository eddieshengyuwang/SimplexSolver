class LinearProgram:

    def __init__(self, type, obj, matrix, ineq, b, vars):
        self.type = type
        self.obj = obj
        self.matrix = matrix
        self.ineq = ineq
        self.b = b
        self.vars = vars
    
