from rubik.check import _check
from rubik.cube import Cube

# NOTES:
#    use all() to check if a string contains certain characters

ROTATION_CHARACTERS = set('FfRrBbLlUuDd')

def _solve(parms):
    
    result = {}
    rotations = parms.get('rotate')
    
    # import checkTest cases
    if (check_result := _check(parms)).get('status') != 'ok':
        return check_result
    
    # test_solve_05_rotate_empty
    if ''.__eq__(rotations):
        rotations = 'F'
    
    # test_solve_06_rotate_missing
    elif rotations is None:
        rotations = 'F'
    
    # test_solve_04_rotate_notletter
    if not rotations.isalpha():
        result['status'] = 'error: rotation characters must be alphabetical'
    
    # test_solve_07_rotate_invalidchars
    elif not all(rotations in ROTATION_CHARACTERS for rotation in rotations):
        result['status'] = 'error: invalid rotation characters'
    
    else:
        cube = Cube(parms.get('cube'))
        for rotation in rotations:
            cube.rotate(rotation)
        result['status'] = 'ok'
        result['cube'] = str(cube)
    
    return result
            