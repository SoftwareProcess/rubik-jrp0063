from copy import deepcopy

# NOTES:
#    use __str__ method to display string class representation instead of memory address
#    unused loop variables can be replaced with '_'
#    : str is a parameter annotation
#    -> is a return value annotation

# USING 3D GEOMETRY:
#    POSITIVE X - FRONT
#    NEGATIVE X - BACK
#    POSITIVE Y - RIGHT
#    NEGATIVE Y - LEFT
#    POSITIVE Z - UP
#    NEGATIVE Z - DOWN

# USING PYTHON DICTIONARY FORMAT
FACES = {
    'f': ('front', 'px'),
    'b': ('back', 'nx'),
    'r': ('right', 'py'),
    'l': ('left', 'ny'),
    'u': ('up', 'pz'),
    'd': ('down', 'nz')
    }

class Cube:
    
    def __init__(self, cube_str: str):
        
        self.cube_str = cube_str
        
        # based on cube numbering from slides
        front_offset = 0
        back_offset = 18
        right_offset = 9
        left_offset = 27
        up_offset = 36
        down_offset = 45
        
        # rubik's cube is a 3x3x3
        self.cube = [[[Brick() for _ in range(3)] for _ in range(3)] for _ in range(3)]
        
        front = self.front()
        back = self.back()
        right = self.right()
        left = self.left()
        up = self.up()
        down = self.down()
        
        for i in range(9):
            front[i // 3][i % 3].pos_x = cube_str[i + front_offset]
            back[i // 3][i % 3].neg_y = cube_str[i + back_offset]
            right[i // 3][i % 3].pos_x = cube_str[i + right_offset]
            left[i // 3][i % 3].neg_x = cube_str[i + left_offset]
            up[i // 3][i % 3].pos_z = cube_str[i + up_offset]
            down[i // 3][i % 3].neg_z = cube_str[i + down_offset]
        
    def __str__(self) -> str:
        return (
            "".join(str(cuboid.pos_y) for row in self.front() for cuboid in row)
            + "".join(str(cuboid.pos_x) for row in self.right() for cuboid in row)
            + "".join(str(cuboid.neg_y) for row in self.back() for cuboid in row)
            + "".join(str(cuboid.neg_x) for row in self.left() for cuboid in row)
            + "".join(str(cuboid.pos_z) for row in self.up() for cuboid in row)
            + "".join(str(cuboid.neg_z) for row in self.down() for cuboid in row)
        )
        
    def rotate(self, face: str, offset: int = 0, rotations: int = 1) -> None:
        if not FACES.get(face.lower()):
            raise ValueError("The face specified for rotation is not present in " + str(list(FACES.keys())))
        if offset < 0 or offset >= 3:
            raise ValueError(f"The offset specified must be between 0 <= offset < {3}")
        if rotations < 0:
            raise ValueError("The rotation specified must be greater than 0")
        
        normal = FACES.get(face.lower())[1]
        layer = getattr(self, FACES.get(face.lower())[0])(offset)
        clockwise = face.isupper()
        
        for _ in range(rotations):
            for x in range(0, 3 // 2):
                for y in range(x, 3-x-1):
                    temp = deepcopy(layer[x][y].rotate(normal, clockwise))
                    if clockwise:
                        layer[x][y].replace(layer[3-y-1][x].rotate(normal, clockwise))
                        layer[3-y-1][x].replace(layer[3-x-1][3-y-1].rotate(normal, clockwise))
                        layer[3-x-1][3-y-1].replace(layer[y][3-x-1].rotate(normal, clockwise))
                        layer[y][3-x-1].replace(temp)
                    else:
                        layer[x][y].replace(layer[y][3-x-1].rotate(normal, clockwise))
                        layer[y][3-x-1].replace(layer[3-x-1][3-y-1].rotate(normal, clockwise))
                        layer[3-x-1][3-y-1].replace(layer[3-y-1][x].rotate(normal, clockwise))
                        layer[3-y-1][x].replace(temp)
                        
    def is_solved(self) -> bool:
        return (
            len(set(str(cuboid.pos_y) for row in self.front() for cuboid in row))
            + len(set(str(cuboid.pos_x) for row in self.right() for cuboid in row))
            + len(set(str(cuboid.neg_y) for row in self.back() for cuboid in row))
            + len(set(str(cuboid.neg_x) for row in self.left() for cuboid in row))
            + len(set(str(cuboid.pos_z) for row in self.up() for cuboid in row))
            + len(set(str(cuboid.neg_z) for row in self.down() for cuboid in row))
        ) == 6
        
    def is_adjacency_safe(self) -> bool:
        if 3 % 2 != 1:
            raise ValueError("The parity of the cube's nth degree must be odd to perform an adjacency check")

        mid = 3 // 2
        invalid_colors = {}

        front, back = self.cube[mid][3-1][mid].pos_y, self.cube[mid][0][mid].neg_y
        invalid_colors[front], invalid_colors[back] = back, front
        left, right = self.cube[mid][mid][0].neg_x, self.cube[mid][mid][3-1].pos_x
        invalid_colors[left], invalid_colors[right] = right, left
        up, down = self.cube[3-1][mid][mid].pos_z, self.cube[0][mid][mid].neg_z
        invalid_colors[up], invalid_colors[down] = down, up

        for plane in self.cube:
            for row in plane:
                for cubelet in row:
                    cubelet = set(cubelet.__dict__.values())
                    for color in cubelet:
                        if color and invalid_colors.get(color, None) in cubelet:
                            return False
        return True

    def front(self, offset: int = 0):
        return self.xz_plane(3 - 1 - offset)[::-1]

    def right(self, offset: int = 0):
        return [row[::-1] for row in self.yz_plane(3 - 1 - offset)[::-1]]

    def back(self, offset: int = 0):
        return [row[::-1] for row in self.xz_plane(0 + offset)[::-1]]

    def left(self, offset: int = 0):
        return self.yz_plane(0 + offset)[::-1]

    def up(self, offset: int = 0):
        return self.xy_plane(3 - 1 - offset)

    def down(self, offset: int = 0):
        return self.xy_plane(0 + offset)[::-1]

    def xy_plane(self, z):
        return self.cube[z]

    def yz_plane(self, x):
        return [[row[x] for row in plane] for plane in self.cube]

    def xz_plane(self, y):
        return [plane[y] for plane in self.cube]

# smaller cubes making up big cube
class Brick:
    
    def __init__(self):
        self.pos_x = ''
        self.neg_x = ''
        self.pos_y = ''
        self.neg_y = ''
        self.pos_z = ''
        self.neg_z = ''
        
    def rotate(self, normal: str, clockwise: bool) -> 'Brick':
        clockwise = clockwise if normal[0] == "p" else not clockwise
        normal = normal[1]
        if normal == "x":
            if clockwise:
                self.pos_z, self.neg_y, self.neg_z, self.pos_y = self.pos_y, self.pos_z, self.neg_y, self.neg_z
            else:
                self.pos_z, self.neg_y, self.neg_z, self.pos_y = self.neg_y, self.neg_z, self.pos_y, self.pos_z
        elif normal == "y":
            if clockwise:
                self.pos_z, self.neg_x, self.neg_z, self.pos_x = self.neg_x, self.neg_z, self.pos_x, self.pos_z
            else:
                self.pos_z, self.neg_x, self.neg_z, self.pos_x = self.pos_x, self.pos_z, self.neg_x, self.neg_z
        elif normal == "z":
            if clockwise:
                self.neg_y, self.pos_x, self.pos_y, self.neg_x = self.neg_x, self.neg_y, self.pos_x, self.pos_y
            else:
                self.neg_y, self.pos_x, self.pos_y, self.neg_x = self.pos_x, self.pos_y, self.neg_x, self.neg_y
        return self
    
    def replace(self, other: "Brick") -> None:
        for attr in self.__dict__.keys():
            setattr(self, attr, getattr(other, attr))
    