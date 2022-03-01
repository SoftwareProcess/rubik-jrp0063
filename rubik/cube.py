import math

# USING 3D GEOMETRY:
#    POSITIVE X - FRONT
#    NEGATIVE X - BACK
#    POSITIVE Y - RIGHT
#    NEGATIVE Y - LEFT
#    POSITIVE Z - UP
#    NEGATIVE Z - DOWN

class Cube:
    
    def __init__(self, cube_str: str):
        
        # cube dimensions (e.g.3x3)
        self.n = int(math.sqrt(len(cube_str) // 6))
        
    def xy_plane(self):
        pass
    
    def yz_plane(self):
        pass
        
    def zx_plane(self):
        pass
        
    # POS X
    def front(self):
        pass
    
    # NEG X
    def back(self):
        pass
    
    # POS Y
    def right(self):
        pass
    
    # NEG Y
    def left(self):
        pass
    
    # POS Z
    def up(self):
        pass
    
    # NEG Z
    def down(self):
        pass
    

# smaller cubes making up big cube
class Brick:
    
    def __init__(self):
        self.pos_x = ''
        self.neg_x = ''
        self.pos_y = ''
        self.neg_y = ''
        self.pos_z = ''
        self.neg_z = ''