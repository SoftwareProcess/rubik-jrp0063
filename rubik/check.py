import rubik.cube as rubik
import collections

def _check(parms):
    
    result={}
    encodedCube = parms.get('cube', None)
    
    # encodedCube is empty    
    if encodedCube is None:
        result['status'] = 'error: cube missing'
        
    # encodedCube is a string
    elif not isinstance(encodedCube, str):
        result['status'] = 'error: not a string'
        
    # encodedCube is alphanumeric
    elif not encodedCube.isalnum():
        result['status'] = 'error: invalid characters'
    
    # encodedCube is 54 characters
    elif len(encodedCube) != 54:
        result['status'] = 'error: invalid size'
        
    # encodedCube contains 6 colors
    elif len(collections.Counter(encodedCube)) != 6:
        result['status'] = 'error: number of colors'
        
    # encodedCube color centers are at indices 4, 13, 22, 31, 40, and 49
    elif len(set(encodedCube[i] for i in [4, 13, 22, 31, 40, 49])) != 6:
        result['status'] = 'error: invalid centers'
    
    # encodedCube contains 9 of each color
    elif any([i != 9 for i in collections.Counter(encodedCube).values()]):
        result['status'] = 'error: amount of each color'

    # valid
    else:
        result['status'] = 'ok'
        
    return result
