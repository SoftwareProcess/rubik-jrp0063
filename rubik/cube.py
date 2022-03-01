# faces are read in this order from sequence
FACES = ('front', 'right', 'back', 'left', 'up', 'down')

class Cube:
    
    
    def __init__(self, cube_str: str):
        self.face_assign = {
            face: [
                [cube_str[offset + 0], cube_str[offset + 1], cube_str[offset + 2]],
                [cube_str[offset + 3], cube_str[offset + 4], cube_str[offset + 5]],
                [cube_str[offset + 6], cube_str[offset + 7], cube_str[offset + 8]],
                ]
            for face, offset in zip(FACES, (0, 9, 18, 27, 36, 45))
            }