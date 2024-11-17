from Magnet import Magnet
from Magnet import Node
from Board import Board
from Algorithms import Algorithms

def play(level):
    end_game = False
    while not level.isGoal() and level.no_moves > 0:
        level.display_board()
        if input("If you want to end the game, enter 'e': ").lower() == "e":
            print("Game ended by user.")
            return
        x_prev, y_prev = input(
            "Enter the position of the magnet you want to move (x,y):"
        ).split(",")
        x_new, y_new = input(
            "Enter the coordnates of where you want the to move (x,y):"
        ).split(",")
        level.move_magnet(int(x_prev), int(y_prev), int(x_new), int(y_new))
    if level.isGoal():
        level.display_board()
        print("Congratulations! You have solved the puzzle.")
    elif level.no_moves==0:
        level.display_board()
        print("Game over! You ran out of moves.")


def get_level_configuration():
    x = int(input("Enter level (1-25): "))

    levels = {
        1: {
            "row": 3,
            "col": 4,
            "purplePieces": [(2, 0)],
            "redPieces": [],
            "whitePieces": [(1, 1), (1, 3)],
            "grayPieces": [(1, 2)],
            "no_moves": 1,
        },
        2: {
            "row": 5,
            "col": 5,
            "purplePieces": [(4, 0)],
            "redPieces": [],
            "whitePieces": [(0, 2), (2, 0), (2, 2), (2, 4), (4, 2)],
            "grayPieces": [(1, 2), (2, 1), (2, 3), (3, 2)],
            "no_moves": 1,
        },
        3: {
            "row": 3,
            "col": 4,
            "purplePieces": [(2, 0)],
            "redPieces": [],
            "whitePieces": [(0, 3), (2, 3)],
            "grayPieces": [(1, 2)],
            "no_moves": 2,
        },
        4: {
            "row": 5,
            "col": 3,
            "purplePieces": [(2, 0)],
            "redPieces": [],
            "whitePieces": [(0, 0), (0, 2), (4, 1)],
            "grayPieces": [(1, 1), (3, 1)],
            "no_moves": 2,
        },
        5: {
            "row": 4,
            "col": 3,
            "purplePieces": [(3, 1)],
            "redPieces": [],
            "whitePieces": [(0, 0), (1, 0), (3, 0), (0, 2), (1, 2)],
            "grayPieces": [(1, 0), (1, 2), (2, 0), (2, 2)],
            "no_moves": 2,
        },
        6: {
            "row": 3,
            "col": 5,
            "purplePieces": [(2, 0)],
            "redPieces": [],
            "whitePieces": [(1, 2), (0, 3), (2, 3)],
            "grayPieces": [(1, 1), (1, 3)],
            "no_moves": 4,
        },
        7: {
            "row": 5,
            "col": 4,
            "purplePieces": [(2, 1)],
            "redPieces": [],
            "whitePieces": [(0, 0), (1, 0), (2, 3), (3, 2), (4, 3)],
            "grayPieces": [(1, 0), (2, 0), (3, 1), (3, 2)],
            "no_moves": 2,
        },
        8: {
            "row": 3,
            "col": 4,
            "purplePieces": [(2, 0)],
            "redPieces": [],
            "whitePieces": [(0, 0), (0, 2), (2, 2)],
            "grayPieces": [(1, 1), (1, 2)],
            "no_moves": 2,
        },
        9: {
            "row": 1,
            "col": 7,
            "purplePieces": [(0, 0)],
            "redPieces": [],
            "whitePieces": [(0, 1), (0, 3), (0, 6)],
            "grayPieces": [(0, 3), (0, 5)],
            "no_moves": 2,
        },
        10: {
            "row": 4,
            "col": 4,
            "purplePieces": [(0, 0)],
            "redPieces": [],
            "whitePieces": [(1, 1), (1, 3), (3, 0), (3, 3)],
            "grayPieces": [(2, 2), (2, 3), (3, 1)],
            "no_moves": 2,
        },
        11: {
            "row": 2,
            "col": 5,
            "purplePieces": [],
            "redPieces": [(1, 2)],
            "whitePieces": [(0, 1), (0, 2), (0, 3)],
            "grayPieces": [(0, 0), (0, 4)],
            "no_moves": 1,
        },
        12: {
            "row": 5,
            "col": 4,
            "purplePieces": [],
            "redPieces": [(3, 1)],
            "whitePieces": [(1, 0), (2, 0), (4, 0), (4, 2)],
            "grayPieces": [(0, 0), (1, 0), (4, 3)],
            "no_moves": 1,
        },
        13: {
            "row": 3,
            "col": 6,
            "purplePieces": [],
            "redPieces": [(2, 3)],
            "whitePieces": [(0, 3), (2, 1), (1, 1), (0, 4)],
            "grayPieces": [(0, 0), (0, 4), (0, 5)],
            "no_moves": 2,
        },
        14: {
            "row": 4,
            "col": 4,
            "purplePieces": [],
            "redPieces": [(3, 3)],
            "whitePieces": [(1, 0), (1, 2), (2, 2), (2, 1)],
            "grayPieces": [(0, 3), (2, 0), (3, 0)],
            "no_moves": 2,
        },
        15: {
            "row": 3,
            "col": 5,
            "purplePieces": [(1, 2)],
            "redPieces": [(2, 2)],
            "whitePieces": [(1, 4), (0, 0), (0, 2), (2, 4)],
            "grayPieces": [(0, 3), (0, 1)],
            "no_moves": 2,
        },
        16: {
            "row": 5,
            "col": 5,
            "purplePieces": [(2, 4)],
            "redPieces": [(2, 0)],
            "whitePieces": [(0, 3), (0, 4), (4, 3), (4, 0)],
            "grayPieces": [(1, 2), (3, 2)],
            "no_moves": 3,
        },
        17: {
            "row": 4,
            "col": 4,
            "purplePieces": [(3, 3)],
            "redPieces": [(0, 0)],
            "whitePieces": [(1, 1), (1, 3), (2, 2), (3, 1)],
            "grayPieces": [(0, 2), (2, 0)],
            "no_moves": 2,
        },
        18: {
            "row": 5,
            "col": 6,
            "purplePieces": [(4, 3)],
            "redPieces": [(4, 2)],
            "whitePieces": [(2, 3), (2, 1), (2, 2), (2, 5), (1, 3)],
            "grayPieces": [(2, 0), (0, 3), (2, 5)],
            "no_moves": 2,
        },
        19: {
            "row": 5,
            "col": 5,
            "purplePieces": [(0, 2)],
            "redPieces": [(2, 2)],
            "whitePieces": [(1, 0), (3, 0), (2, 1), (3, 2), (3, 4), (1, 4)],
            "grayPieces": [(0, 3), (0, 1), (4, 1), (4, 3)],
            "no_moves": 4,
        },
        20: {
            "row": 5,
            "col": 4,
            "purplePieces": [(4, 2)],
            "redPieces": [(4, 3)],
            "whitePieces": [(0, 1), (0, 3), (1, 0), (2, 0), (3, 0)],
            "grayPieces": [(0, 1), (0, 2), (4, 0)],
            "no_moves": 2,
        },
        21: {
            "row": 3,
            "col": 4,
            "purplePieces": [(2, 0)],
            "redPieces": [(2, 3)],
            "whitePieces": [(1, 0), (1, 1), (0, 2), (2, 0), (2, 1)],
            "grayPieces": [(0, 1), (1, 1), (1, 2)],
            "no_moves": 2,
        },
        22: {
            "row": 4,
            "col": 5,
            "purplePieces": [(0, 0)],
            "redPieces": [(3, 2)],
            "whitePieces": [(0, 1), (0, 3), (1, 0), (1, 4), (2, 1)],
            "grayPieces": [(0, 3), (0, 4), (3, 0)],
            "no_moves": 3,
        },
        23: {
            "row": 4,
            "col": 5,
            "purplePieces": [(3, 4)],
            "redPieces": [(3, 2)],
            "whitePieces": [(0, 2), (2, 1), (2, 2), (2, 3), (3, 2)],
            "grayPieces": [(0, 3), (1, 4), (2, 0)],
            "no_moves": 3,
        },
        24: {
            "row": 5,
            "col": 5,
            "purplePieces": [(1, 4)],
            "redPieces": [(3, 0)],
            "whitePieces": [(0, 3), (2, 1), (2, 3), (4, 1), (4, 2)],
            "grayPieces": [(0, 1), (1, 3), (3, 4)],
            "no_moves": 3,
        },
        25: {
            "row": 5,
            "col": 4,
            "purplePieces": [(4, 0)],
            "redPieces": [(0, 3)],
            "whitePieces": [(0, 0), (0, 3), (2, 0), (4, 0), (4, 1), (4, 2)],
            "grayPieces": [(0, 0), (1, 2), (3, 2), (4, 3)],
            "no_moves": 3,
        },
    }

    return levels.get(x, "Invalid level. Please enter a level between 1 and 25.")


def get_level():
    level_config = get_level_configuration()
    magnets = []
    for Pmagnet in level_config["purplePieces"]:
        magnets.append(Magnet("purple", Pmagnet[0], Pmagnet[1]))

    for Rmagnet in level_config["redPieces"]:
        magnets.append(Magnet("red", Rmagnet[0], Rmagnet[1]))

    for Gmagnet in level_config["grayPieces"]:
        magnets.append(Magnet("gray", Gmagnet[0], Gmagnet[1]))

    whites = [Node(w[0], w[1]) for w in level_config["whitePieces"]]

    # Initialize the board
    level = Board(level_config["row"],level_config["col"], magnets, whites, level_config["no_moves"])
    return level


level = get_level()
# play(level)
algorithms =Algorithms()
queue=[]
path=[]
algorithms.UCS(level,queue)