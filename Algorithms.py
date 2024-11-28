from copy import deepcopy
from Board import Board
import math


class Algorithms:
    def __init__(self):
        self.visited = []

    def BFS(self, board, queue):
        self.visited.append(board)
        if board.isGoal():
            print("Goal!!, The path is:")
            for path in board.path:
                path.display_board()
            return
        for i in range(board.n):
            for j in range(board.m):
                if board.grid[i][j] in ["P", "R"]:
                    for k in range(board.n):
                        for l in range(board.m):
                            tempBoard = Board
                            tempBoard = deepcopy(board)
                            if tempBoard.grid[k][l] not in ["G", "R", "P"]:
                                tempBoard.move_magnet(i, j, k, l)
                                if tempBoard not in self.visited:
                                    queue.append(tempBoard)
        result = queue.pop(0)
        result.display_board()
        self.BFS(result, queue)

    def DFS(self, board, stack):
        self.visited.append(board)
        if board.isGoal():
            print("Goal!!, The path is:")
            for path in board.path:
                path.display_board()
            return
        if board.no_moves == 0:
            if len(stack) == 0:
                print("lose!")
                return
            result = stack.pop()
            result.display_board()
            return self.DFS(result, stack)
        for i in range(board.n):
            for j in range(board.m):
                if board.grid[i][j] in ["P", "R"]:
                    for k in range(board.n):
                        for l in range(board.m):
                            tempBoard = Board
                            tempBoard = deepcopy(board)
                            if tempBoard.grid[k][l] not in ["G", "R", "P"]:
                                tempBoard.move_magnet(i, j, k, l)
                                if tempBoard not in self.visited:
                                    stack.append(tempBoard)
        result = stack.pop()
        result.display_board()
        self.DFS(result, stack)

    def UCS(self, board, queue):
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
                if board.grid[i][j] in ["P", "R"]:
                    for k in range(board.n):
                        for l in range(board.m):
                            tempBoard = Board
                            tempBoard = deepcopy(board)
                            if tempBoard.grid[k][l] not in ["G", "R", "P"]:
                                tempBoard.move_magnet(i, j, k, l)
                                tempBoard.cost += 1
                                if tempBoard not in self.visited:
                                    queue.append(tempBoard)
        min = queue[0]
        min_cost = queue[0].cost
        min_index = 0
        index = 0
        for brd in queue:
            index += 1
            if brd.cost < min_cost:
                min = brd
                min_cost = brd.cost
                min_index = index
        queue.remove(min)
        min.display_board
        self.UCS(min, queue)

    def Heuristic_cost(self, board, pos_x, pos_y):
        distances = []
        for white in board.whites:
            dist_x = abs(pos_x - white[0])
            dist_y = abs(pos_y - white[1])
            distances.append(dist_x + dist_y)
        return min(distances)

    def Heuristic_function(self, board):
        heuristic = 0
        for i in range(board.n):
            for j in range(board.m):
                if board.grid[i][j] == "G":
                    heuristic += self.Heuristic_cost(board, i, j)
                if board.grid[i][j] in ["R", "P"]:
                    if (i, j) not in board.whites:
                        heuristic += 1
        return heuristic

    def Hill_Climbing(self, board):
        if board.isGoal():
            print("Goal!!")
            print("The path is:")
            for path in board.path:
                path.display_board()
            return
        Heuristic = []
        for i in range(board.n):
            for j in range(board.m):
                if board.grid[i][j] in ["P", "R"]:
                    for k in range(board.n):
                        for l in range(board.m):
                            tempBoard = Board
                            tempBoard = deepcopy(board)
                            if tempBoard.grid[k][l] not in ["G", "R", "P"]:
                                tempBoard.move_magnet(i, j, k, l)
                                heuristic_value = self.Heuristic_function(tempBoard)
                                Heuristic.append((i, j, k, l, heuristic_value))
        if Heuristic:
            print(Heuristic)
            min_i, min_j, min_k, min_l, min_heuristic = min(
                Heuristic, key=lambda x: x[4]
            )
            if min_heuristic < self.Heuristic_function(board):
                tempBoard = Board
                tempBoard = deepcopy(board)
                tempBoard.move_magnet(min_i, min_j, min_k, min_l)
                self.Hill_Climbing(tempBoard)
            else:
                print("No valid solution found")
                print(f"best heuristic cost is {self.Heuristic_function(board)}")
                board.display_board()
    def A_Star(self,board):
        if board.isGoal():
            print("Goal!!")
            print("The path is:")
            for path in board.path:
                path.display_board()
            return
        Heuristic = []
        for i in range(board.n):
            for j in range(board.m):
                if board.grid[i][j] in ["P", "R"]:
                    for k in range(board.n):
                        for l in range(board.m):
                            tempBoard = Board
                            tempBoard = deepcopy(board)
                            if tempBoard.grid[k][l] not in ["G", "R", "P"]:
                                tempBoard.move_magnet(i, j, k, l)
                                tempBoard.cost += 1
                                heuristic_value = self.Heuristic_function(tempBoard)
                                Heuristic.append((i, j, k, l, heuristic_value))
        if Heuristic:
            min_i=0; min_j=0; min_k=0; min_l=0; min_cost=board.cost+self.Heuristic_function(board)
            for h in Heuristic:
                tempBoard = Board
                tempBoard = deepcopy(board)
                tempBoard.move_magnet(h[0], h[1], h[2], h[3])
                if tempBoard.cost+ h[4]<min_cost:
                    min_i=h[0]; min_j=h[1]; min_k=h[2]; min_l=h[3]; min_cost=tempBoard.cost+h[4]
            if min_cost < self.Heuristic_function(board)+board.cost:
                tempBoard = Board
                tempBoard = deepcopy(board)
                tempBoard.move_magnet(min_i, min_j, min_k, min_l)
                tempBoard.display_board()
                self.A_Star(tempBoard)
            else:
                print("No valid solution found")
                print(f"best cost is {self.Heuristic_function(board)+board.cost}")
                board.display_board()
