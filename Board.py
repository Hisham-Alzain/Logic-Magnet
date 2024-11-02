class Board:

    def __init__(self, n, magnets, whites, no_moves):
        self.n = n
        self.no_moves = no_moves
        self.whites=[]
        self.grid = [["-" for _ in range(n)] for _ in range(n)]
        for white in whites:
            self.grid[white.pos_x][white.pos_y] = "*"
            self.whites.append((white.pos_x, white.pos_y))
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
        print()

    def isIngrid(self, x, y):
        return x < self.n and y < self.n and x >= 0 and y >= 0

    def isGoal(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.grid[i][j] == "*":
                    return False
        return True

    def move_magnet(self, x_prev, y_prev, x_next, y_next):
        if not self.isIngrid(x_prev, y_prev) or not self.isIngrid(x_next, y_next):
            print("out of bound")
            return

        elif self.grid[x_prev][y_prev] in ["-", "*"]:
            print("Wrong move")
            return

        elif self.grid[x_prev][y_prev] == "G":
            print("Can't move gray magnets")
            return

        elif self.grid[x_prev][y_prev] == "R":
            if self.grid[x_next][y_next] in ["-", "*"]:
                if (x_prev,y_prev) in self.whites:
                    self.grid[x_prev][y_prev] = "*"
                else:
                    self.grid[x_prev][y_prev] = "-"
                self.grid[x_next][y_next] = "R"
                self.no_moves-=1
                magnets = []
                for i in range(self.n):
                    if self.grid[i][y_next] in ["G", "P"]:
                        magnets.append((i, y_next))
                    if self.grid[x_next][i] in ["G", "P"]:
                        magnets.append((x_next, i))
                self.red_moves(magnets, x_next, y_next)
            else:
                print("illegal move")

        elif self.grid[x_prev][y_prev] == "P":
            if self.grid[x_next][y_next] in ["-", "*"]:
                if (x_prev,y_prev) in self.whites:
                    self.grid[x_prev][y_prev] = "*"
                else:
                    self.grid[x_prev][y_prev] = "-"
                self.grid[x_next][y_next] = "P"
                self.no_moves-=1
                magnets = []
                for i in range(self.n):
                    if self.grid[i][y_next] in ["G", "R"]:
                        magnets.append((i, y_next))
                    if self.grid[x_next][i] in ["G", "R"]:
                        magnets.append((x_next, i))
                self.purple_moves(magnets, x_next, y_next)
            else:
                print("illegal move")

    def purple_moves(self, magnets, x_next, y_next):
        for magnet in magnets:
            if magnet[0] > x_next:
                if self.isIngrid(magnet[0] + 1, y_next):
                    if self.grid[magnet[0] + 1][y_next] in ["-", "*"]:
                        self.grid[magnet[0] + 1][y_next] = self.grid[magnet[0]][y_next]
                        if (magnet[0],y_next) in self.whites:
                            self.grid[magnet[0]][y_next] = "*"
                        else:
                            self.grid[magnet[0]][y_next] = "-"
            elif magnet[0] < x_next:
                if self.isIngrid(magnet[0] - 1, y_next):
                    if self.grid[magnet[0] - 1][y_next] in ["-", "*"]:
                        self.grid[magnet[0] - 1][y_next] = self.grid[magnet[0]][y_next]
                        if (magnet[0],y_next) in self.whites:
                            self.grid[magnet[0]][y_next] = "*"
                        else:
                            self.grid[magnet[0]][y_next] = "-"
            if magnet[1] > y_next:
                if self.isIngrid(x_next, magnet[1] + 1):
                    if self.grid[x_next][magnet[1] + 1] in ["-", "*"]:
                        self.grid[x_next][magnet[1] + 1] = self.grid[x_next][magnet[1]]
                        if (x_next,magnet[1]) in self.whites:
                            self.grid[x_next][magnet[1]] = "*"
                        else:
                            self.grid[x_next][magnet[1]] = "-"
            elif magnet[1] < y_next:
                if self.isIngrid(x_next, magnet[1] - 1):
                    if self.grid[x_next][magnet[1] - 1] in ["-", "*"]:
                        self.grid[x_next][magnet[1] - 1] = self.grid[x_next][magnet[1]]
                        if (x_next,magnet[1]) in self.whites:
                            self.grid[x_next][magnet[1]] = "*"
                        else:
                            self.grid[x_next][magnet[1]] = "-"

    def red_moves(self, magnets, x_next, y_next):
        for magnet in magnets:
            if magnet[0] > x_next:
                if self.isIngrid(magnet[0] - 1, y_next):
                    if self.grid[magnet[0] - 1][y_next] in ["-", "*"]:
                        self.grid[magnet[0] - 1][y_next] = self.grid[magnet[0]][
                            y_next
                        ]
                        self.grid[magnet[0]][y_next] = "-"
            elif magnet[0] < x_next:
                if self.isIngrid(magnet[0] + 1, y_next):
                    if self.grid[magnet[0] + 1][y_next] in ["-", "*"]:
                        self.grid[magnet[0] + 1][y_next] = self.grid[magnet[0]][
                            y_next
                        ]
                        self.grid[magnet[0]][y_next] = "-"
            if magnet[1] > y_next:
                if self.isIngrid(x_next, magnet[1] - 1):
                    if self.grid[x_next][magnet[1] - 1] in ["-", "*"]:
                        self.grid[x_next][magnet[1] - 1] = self.grid[x_next][
                            magnet[1]
                        ]
                        self.grid[x_next][magnet[1]] = "-"
            elif magnet[1] < y_next:
                if self.isIngrid(x_next, magnet[1] + 1):
                    if self.grid[x_next][magnet[1] + 1] in ["-", "*"]:
                        self.grid[x_next][magnet[1] + 1] = self.grid[x_next][
                            magnet[1]
                        ]
                        self.grid[x_next][magnet[1]] = "-"
