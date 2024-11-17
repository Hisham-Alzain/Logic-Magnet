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
            for j in range(board.m):
                if board.grid[i][j] in ['P','R']:
                    for k in  range(board.n):
                        for l in range(board.m):
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
        if board.no_moves==0:
            if len(stack)==0:
                print("lose!")
                return
            result=stack.pop()
            result.display_board()
            return self.DFS(result,stack)
        for i in range(board.n):
            for j in range(board.m):
                if board.grid[i][j] in ['P','R']:
                    for k in  range(board.n):
                        for l in range(board.m):
                            tempBoard=Board
                            tempBoard=deepcopy(board)
                            if tempBoard.grid[k][l] not in ['G','R','P']:
                                tempBoard.move_magnet(i,j,k,l)
                                if tempBoard not in self.visited:
                                    stack.append(tempBoard)
        result=stack.pop()
        result.display_board()
        self.DFS(result,stack)

    def UCS(self,board,queue):
        self.visited.append(board)
        if board.isGoal():
            print("Goal!!")
            print("The path is")
            for path in board.path:
                path.display_board()
            print(f"The cost is {board.cost}")
            return
        for i in range(board.n):
            for j in range(board.m):
                if board.grid[i][j] in ['P','R']:
                    for k in  range(board.n):
                        for l in range(board.m):
                            tempBoard=Board
                            tempBoard=deepcopy(board)
                            if tempBoard.grid[k][l] not in ['G','R','P']:
                                tempBoard.move_magnet(i,j,k,l)
                                tempBoard.cost+=1
                                if tempBoard not in self.visited:
                                    queue.append(tempBoard)
        min=queue[0]
        min_cost=queue[0].cost
        min_index=0
        index=0
        for brd in queue:
            index+=1
            if(brd.cost< min_cost):
                min=brd
                min_cost=brd.cost
                min_index=index
        queue.remove(min)
        min.display_board
        self.UCS(min,queue)