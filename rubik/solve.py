from rubik.check import _check

def _solve(parms):
    if (cube_result := _check(parms)).get('status') != 'ok':
        return cube_result