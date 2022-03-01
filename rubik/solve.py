from rubik.check import _check

ROTATION_CHARACTERS = set('FfRrBbLlUuDd')

def _solve(parms):
    
    result = {}
    rotate = parms.get('rotate')
    if rotate is None:
        rotate = 'F'
    
    if not isinstance(rotate, str):
        result['status'] = ''