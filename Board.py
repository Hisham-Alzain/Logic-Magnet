class Board:

    def __init__(self, n, magnets, whites, no_moves):
        self.n = n
        self.no_moves = no_moves
        self.grid = [["-" for _ in range(n)] for _ in range(n)]
        for white in whites:
            for i in range(self.n):
                if white.pos_x == i:
                    for j in range(self.n):
                        if white.pos_y == j:
                            self.grid[i][j] = "*"
        for magnet in magnets:
            for i in range(self.n):
                if magnet.pos_x == i:
                    for j in range(self.n):
                        if magnet.pos_y == j:
                            if magnet.color == "red":
                                self.grid[i][j] = "R"
                            elif magnet.color == "purple":
                                self.grid[i][j] = "P"
                            elif magnet.color == "gray":
                                self.grid[i][j] = "G"

    def display_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.grid[i][j] + " ", end="")
            print()
