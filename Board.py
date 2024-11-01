class Board:

    def __init__(self, n, magnets, whites, no_moves):
        self.n = n
        self.no_moves = no_moves
        self.grid = [["-" for _ in range(n)] for _ in range(n)]
        for white in whites:
            self.grid[white.pos_x][white.pos_y] = "*"
        for magnet in magnets:
            if magnet.color == "red":
                self.grid[magnet.pos_x][magnet.pos_y] = "R"
            elif magnet.color == "purple":
                self.grid[magnet.pos_x][magnet.pos_y] = "P"
            elif magnet.color == "gray":
                self.grid[magnet.pos_x][magnet.pos_y] = "G"

    def display_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.grid[i][j] + " ", end="")
            print()

    def isIngrid(self, x, y):
        return x < self.n and y < self.n and x >= 0 and y >= 0

    def move_magnet(self, x_prev, y_prev, x_next, y_next):
        if not self.isIngrid(x_prev, y_prev) or not self.isIngrid(x_next, y_next):
            print("out of bound")
            return
        elif self.grid[x_prev][y_prev] in ["-", "*"]:
            print("wrong move")
            return
        elif self.grid[x_prev][y_prev] == "G":
            print("Can't move gray magnets")
            return
        elif self.grid[x_prev][y_prev] == "R":
            if self.grid[x_next][y_next] in ["-", "*"]:
                self.grid[x_prev][y_prev] = "-"
                self.grid[x_next][y_next] = "R"
                for i in range(self.n):
                    if self.grid[i][y_next] in ["G", "P"]:
                        if self.isIngrid(i-1, y_next):
                            if self.grid[i-1][y_next] in ["-", "*"]:
                                self.grid[i-1][y_next] = self.grid[i][y_next]
                                self.grid[i][y_next] = "-"
                    if self.grid[x_next][i] in ["G", "P"]:
                        if self.isIngrid(x_next, i-1):
                            if self.grid[x_next][i-1] in ["-", "*"]:
                                self.grid[x_next][i-1] = self.grid[x_next][i]
                                self.grid[x_next][i] = "-"
            else:
                print("illegal move")
        elif self.grid[x_prev][y_prev] == "P":
            if self.grid[x_next][y_next] in ["-", "*"]:
                self.grid[x_prev][y_prev] = "-"
                self.grid[x_next][y_next] = "P"
                for i in range(self.n):
                    if self.grid[i][y_next] in ["G", "R"]:
                        if self.isIngrid(i+1, y_next):
                            if self.grid[i+1][y_next] in ["-", "*"]:
                                self.grid[i+1][y_next] = self.grid[i][y_next]
                                self.grid[i][y_next] = "-"
                                break
                    if self.grid[x_next][i] in ["G", "R"]:
                        if self.isIngrid(x_next, i+1):
                            if self.grid[x_next][i+1] in ["-", "*"]:
                                self.grid[x_next ][i+1] = self.grid[x_next][i]
                                self.grid[x_next][i] = "-"
                                break
            else:
                print("illegal move")
