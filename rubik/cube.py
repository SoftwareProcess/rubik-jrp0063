
# NOTES:
#    __init__(self [,...])          instance = MyClass(arg1, arg2)    called on instance creation
#    __getitem__(self, key)         self[key]                         accessing an item using an index
#    __setitem__(self, key, val)    self[key] = val                   assigning to an item using an index
#    __str__(self)                  str()                             produce human readable output 
#
#    a leading underscore is used to indicate a private method/attribute
#    unused loop variables can be replaced with an underscore
#    : str is a parameter annotation
#    -> is a return value annotation

NAMES = {'f': 'front', 'r': 'right', 'b': 'back', 'l': 'left', 'u': 'up', 'd': 'down'}
JUST_NAMES = list(NAMES.values())
OFFSETS = {'f': 0, 'r': 9, 'b': 18, 'l': 27, 'u': 36, 'd': 45}
EDGES = {
    list(NAMES)[0]: ((42, 43, 44), (9, 12, 15), (47, 46, 45), (35, 32, 29)),
    list(NAMES)[1]: ((44, 41, 38), (18, 21, 24), (53, 50, 47), (8, 5, 2)),
    list(NAMES)[2]: ((38, 37, 36), (27, 30, 33), (51, 52, 53), (17, 14, 11)),
    list(NAMES)[3]: ((36, 39, 42), (0, 3, 6), (45, 48, 51), (26, 23, 20)),
    list(NAMES)[4]: ((20, 19, 18), (11, 10, 9), (2, 1, 0), (29, 28, 27)),
    list(NAMES)[5]: ((6, 7, 8), (15, 16, 17), (24, 25, 26), (33, 34, 35))
}

class Cube:
    def __init__(self, cube_str):
        
        self.faces = {
            name: [
                [cube_str[offset + 0], cube_str[offset + 1], cube_str[offset + 2]],
                [cube_str[offset + 3], cube_str[offset + 4], cube_str[offset + 5]],
                [cube_str[offset + 6], cube_str[offset + 7], cube_str[offset + 8]],
            ]
            for name, offset in zip(NAMES.values(), OFFSETS.values())
        }
            
    def __setitem__(self, key, val):
        self.faces[JUST_NAMES[key // 9]][key % 9 // 3][key % 3] = val
        
    def __getitem__(self, key):
        return self.faces[JUST_NAMES[key // 9]][key % 9 // 3][key % 3]
        
    def __str__(self):
        result = ''.join(f'{i[0][0]}{i[0][1]}{i[0][2]}{i[1][0]}{i[1][1]}{i[1][2]}{i[2][0]}{i[2][1]}{i[2][2]}' for i in (self.faces[j] for j in NAMES.values()))
        return result
        
    def rotate(self, rotation):
        # upper case - clockwise, lower case - counterclockwise
        direction = rotation.isupper()
        self._rotate_face(rotation.lower(), direction)
        self._rotate_edges(rotation.lower(), direction)
        
    def _rotate_face(self, name, direction):
        offset = OFFSETS[name]
        for x in range(0, 1):
            for y in range(x, 2 - x):
                temp = self[offset + (x * 3 + y)]
                if direction == True:
                    self[offset + (x * 3 + y)] = self[offset + ((2 - y) * 3 + x)]
                    self[offset + ((2 - y) * 3 + x)] = self[offset + ((2 - x) * 3 + (2 - y))]
                    self[offset + ((2 - x) * 3 + (2 - y))] = self[offset + (y * 3 + (2 - x))]
                    self[offset + (y * 3 + (2 - x))] = temp
                else:
                    self[offset + (x * 3 + y)] = self[offset + (y * 3 + (2 - x))]
                    self[offset + (y * 3 + (2 - x))] = self[offset + ((2 - x) * 3 + (2 - y))]
                    self[offset + ((2 - x) * 3 + (2 - y))] = self[offset + ((2 - y) * 3 + x)]
                    self[offset + ((2 - y) * 3 + x)] = temp
                    
    def _rotate_edges(self, name, direction):
        for a, b, c, d in zip(*EDGES[name]):
            temp = self[a]
            if direction:
                self[a] = self[d]
                self[d] = self[c]
                self[c] = self[b]
                self[b] = temp
            else:
                self[a] = self[b]
                self[b] = self[c]
                self[c] = self[d]
                self[d] = temp
        