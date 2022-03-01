
# NOTES:
#    : str is a parameter annotation
#    -> is a return value annotation
#    unused loop variables can be replaced with '_'
#    use __str__ method to display string class representation instead of memory address

# USING 3D GEOMETRY:
#    POSITIVE X - FRONT
#    NEGATIVE X - BACK
#    POSITIVE Y - RIGHT
#    NEGATIVE Y - LEFT
#    POSITIVE Z - UP
#    NEGATIVE Z - DOWN

class Cube:
    
    def __init__(self, cube_str: str):
        
        # Rubik's cube dimension - 3x3x3
        self.cube = [[[Brick() for _ in range(3)] for _ in range(3)] for _ in range(3)]
        
    def __str__(self):
        return f'Cube({self.__init__(cube_str)})'

# smaller cubes making up big cube
class Brick:
    
    def __init__(self):
        self.pos_x = ''
        self.neg_x = ''
        self.pos_y = ''
        self.neg_y = ''
        self.pos_z = ''
        self.neg_z = ''
        
    def rotate(self):
        pass
    
    