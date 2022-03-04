
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

# JONATHON FIX THIS IT'S UGLY
NAMES = {'f': 'front', 'r': 'right', 'b': 'back', 'l': 'left', 'u': 'up', 'd': 'down'}
JUST_NAMES = list(NAMES.values())
OFFSETS = {'f': 0, 'r': 9, 'b': 18, 'l': 27, 'u': 36, 'd': 45}

EDGES = {
    list(NAMES)[0]: ((43, 44, 45), (10, 13, 16), (46, 47, 48), (30, 33, 36)),
    list(NAMES)[1]: ((45, 42, 39), (19, 22, 25), (48, 51, 54), (3, 6, 9)),
    list(NAMES)[2]: ((39, 38, 37), (28, 31, 34), (46, 47, 48), (18, 15, 12)),
    list(NAMES)[3]: ((37, 40, 43), (1, 4, 7), (46, 48, 52), (27, 24, 21)),
    list(NAMES)[4]: ((21, 20, 19), (12, 11, 10), (3, 2, 1), (30, 29, 28)),
    list(NAMES)[5]: ((7, 8, 9), (16, 17, 18), (25, 26, 27), (34, 35, 36))
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
        for i in name:
            offset = OFFSETS[i]
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
        for i in name:
            for a, b, c, d in zip(*EDGES[i]):
                temp = self[a]
                if direction == TRUE:
                    self[a] = self[d]
                    self[d] = self[c]
                    self[c] = self[b]
                    self[b] = temp
                else:
                    self[a] = self[b]
                    self[b] = self[c]
                    self[c] = self[d]
                    self[d] = temp
        