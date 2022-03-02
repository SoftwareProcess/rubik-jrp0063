from rubik.check import _check
from rubik.cube import Cube

# NOTES:
#    use all() to check if a string contains certain characters

ROTATION_CHARACTERS = set('FfRrBbLlUuDd')

def _solve(parms):
    
    if (cube_result := _check(parms)).get('status') != 'ok':
        return cube_result
    
    result = {}
    rotations = parms.get('rotate')
    # rotate defaults to 'F' if missing
    if rotations is '':
        rotations = 'F'
    
    #
    if not isinstance(rotations, str):
        result['status'] = ''
    #
    elif not rotations.isalpha():
        result['status'] = ''
    #
    elif not all(rotations in ROTATION_CHARACTERS for rotation in rotations):
        result['status'] = ''
    else:
        cube = Cube(parms.get('cube'))
        for rotation in rotations:
            cube.rotate(rotation)
        result['status'] = 'ok'
        result['cube'] = str(cube)
    return result
            