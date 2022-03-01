import rubik.check as check

def _solve(parms):
    if (cube_result := check(parms)).get('status') != 'ok':
        return cube_result