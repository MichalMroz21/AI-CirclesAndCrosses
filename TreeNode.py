import copy

class TreeNode:
    def __init__(self, N, sign=None, x=None, y=None, board=None):
        self.sign = sign  # data
        self.firstRow = x
        self.secondColumn = y
        self.children = []  # references to other nodes

        if board is None:
            self.board = [['_' for j in range(N)] for i in range(N)]
        else: self.board = board


    def traverse(self):
        # moves through each node referenced from self downwards
        nodeQueue = [self]

        while len(nodeQueue) > 0:
            current_node = nodeQueue.pop()
            print(current_node.sign)

            for child in current_node.children:
                nodeQueue.append(child)
            


def backtrackDFS(root, boardSize, movingPlayer):

        for i in range(0, len(root.board)):
            for j in range(0, len(root.board[i])):

                if root.board[i][j] == '_':

                    root.board[i][j] = movingPlayer

                    child = TreeNode(boardSize, movingPlayer, j, i, copy.deepcopy(root.board))
                    root.children.append(child)
                    backtrackDFS(root.children[-1], boardSize, 'o' if movingPlayer == 'x' else 'x')

                    root.board[i][j] = '_'

        print("end")


def createNeuralTree(boardSize, startingPlayer):
    root = TreeNode(boardSize)

    backtrackDFS(root, boardSize, startingPlayer)

    return root