
# NOTES:
#    a leading underscore is used to indicate a private method/attribute
#    use __str__ method to display string class representation instead of memory address
#    unused loop variables can be replaced with '_'
#    : str is a parameter annotation
#    -> is a return value annotation

# CUBE ORIENTATION:
#    POSITIVE X - FRONT
#    NEGATIVE X - BACK
#    POSITIVE Y - RIGHT
#    NEGATIVE Y - LEFT
#    POSITIVE Z - UP
#    NEGATIVE Z - DOWN

FACE_NAMES = ("front", "right", "back", "left", "up", "down")
OPERATIONS = {name[0]: name for name in FACE_NAMES}

class Cube:
    
    def __init__(self, cube_str: str):
        self.cube_str = cube_str
        self.faces = {
            face: [
                [cube_str[offset + 0], cube_str[offset + 1], cube_str[offset + 2]],
                [cube_str[offset + 3], cube_str[offset + 4], cube_str[offset + 5]],
                [cube_str[offset + 6], cube_str[offset + 7], cube_str[offset + 8]],
            ]
            for face, offset in zip(FACE_NAMES, (0, 9, 18, 27, 36, 45))
        }
    
    def rotate(self, rotation: str) -> None:
        # upper case - clockwise, lower case - counterclockwise
        motion = rotation.isupper()
    
    def __str__(self):
        return f'{self.cube_str}'
    
    def _test(self):
        return self.faces

c = Cube('gggggggggrrrrrrrrrbbbbbbbbbooooooooowwwwwwwwwyyyyyyyyy')
print(c._test())
