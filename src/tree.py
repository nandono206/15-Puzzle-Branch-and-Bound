#kelas state space tree

class Tree:
    def __init__(self, matrix, parent=None, depth = 0, cost=0, move=""):
        self.parent = parent
        self.matrix = matrix
        self.depth = depth
        self.cost = cost
        self.move = move

    