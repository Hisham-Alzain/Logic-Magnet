from Magnet import Magnet
from Magnet import Node
from Board import Board

p1 = Magnet("red",3,0)
g1 = Magnet("gray",2,2)
magnets=[p1,g1]
w11= Node(2,1)
w12= Node(2,3)
whites=[w11,w12]
level1=Board(4,magnets,whites,1)
level1.display_board()
level1.move_magnet(3,0,0,2)
level1.display_board()