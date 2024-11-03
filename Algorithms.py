from copy import deepcopy
from Board import Board
class Algorithms:
    def __init__(self):
        self.visited=[]

    def BFS(self,board,queue):
        self.visited.append(board)
        if board.isGoal():
            print("Goal!!")
            return
        for i in range(board.n):
            for j in range(board.n):
                if board.grid[i][j] in ['P','R']:
                    for k in  range(board.n):
                        for l in range(board.n):
                            tempBoard=Board
                            tempBoard=deepcopy(board)
                            if tempBoard.grid[k][l] not in ['G','R','P']:
                                tempBoard.move_magnet(i,j,k,l)
                                if tempBoard not in self.visited:
                                    queue.append(tempBoard)
        result=queue.pop(0)
        result.display_board()
        self.BFS(result,queue)

    def DFS(self,board,stack):
        self.visited.append(board)
        if board.isGoal():
            print("Goal!!")
            return
        for i in range(board.n):
            for j in range(board.n):
                if board.grid[i][j] in ['P','R']:
                    for k in  range(board.n):
                        for l in range(board.n):
                            tempBoard=Board
                            tempBoard=deepcopy(board)
                            if tempBoard.grid[k][l] not in ['G','R','P']:
                                tempBoard.move_magnet(i,j,k,l)
                                if tempBoard not in self.visited:
                                    stack.append(tempBoard)
        result=stack.pop()
        result.display_board()
        self.DFS(result,stack)