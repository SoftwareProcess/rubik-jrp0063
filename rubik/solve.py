from rubik.cube import Cube
from rubik.check import _check

# NOTES:
#    use all() to check if a string contains certain characters

ROTATION_CHARACTERS = set('FfRrBbLlUuDd')

def _solve(parms):
    
    # import cube error tests from check
    check_result = _check(parms)
    if (check_result).get('status') != 'ok':
        return check_result
    
    result = {}
    encodedRotations = parms.get('rotate')
    cube = Cube(parms.get('cube'))
    
    # test_solve_01_rotate_missing
    if encodedRotations is None:
        result['status'] = 'ok'
        cube.solveCube()
        
    # test_solve_02_rotate_empty
    elif ''.__eq__(encodedRotations):
        result['status'] = 'ok'
        cube.solveCube()
    
    # test_solve_04_rotate_notletter
    elif not encodedRotations.isalpha():
        result['status'] = 'error: must be alphabetical'
    
    # test_solve_05_rotate_invalidchar
    elif not all(_ in ROTATION_CHARACTERS for _ in encodedRotations):
        result['status'] = 'error: invalid rotation character'
    
    else:
        result['status'] = 'ok'
        for rotation in encodedRotations:
            cube.rotate(rotation)
    
    result['cube'] = str(cube)
    result['solution'] = ''.join(cube.solution)
    return result
