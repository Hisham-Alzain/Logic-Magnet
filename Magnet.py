class Node:
    def __init__(self,pos_x,pos_y):
        self.pos_x=pos_x
        self.pos_y=pos_y
    def get_position(self):
        return [self.pos_x,self.pos_y]

class Magnet(Node):

    def __init__(self, color, pos_x, pos_y):
        self.color = color
        super().__init__(pos_x,pos_y)

    def get_position(self):
        return super().get_position()

    def get_color(self):
        return self.color

    def change_position(self, new_x, new_y):
        self.pos_x = new_x
        self.pos_y = new_y

    def change_position(self, new_pos):
        self.pos_x = new_pos[0]
        self.pos_y = new_pos[1]
