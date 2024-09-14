"""
Zain Saeed
CS 211
2.5.24
"""

Waldo = 'W'
Other = '.'

def all_row_exists_waldo(doob: list[list]) -> bool:
    for row in doob:
        if Waldo not in row:
            return False
    return True
#DONE
def all_col_exists_waldo(doob: list[list]) -> bool:
    if len(doob) == 0:
        return True
    for col in range(len(doob[0])):
        var = False
        for row in range(len(doob)):
            if doob[row][col] == Waldo:
                var = True
                break
        if not var:
            return False
    return True

    
    """for row in doob:
        for col in row:
            if Waldo not in col:
                return False
            else:
                return True"""
#FIX
def all_row_all_waldo(doob: list[list]) -> bool:
    if len(doob) == 0:
        return True
    pass
    for row in doob:
        for col in row:
            if Waldo != col:
                return False
    return True

def all_col_all_waldo(doob: list[list]) -> bool:

    for row in range(len(doob)):
        for col in range(len(doob)):
            if Other in doob[row][col]:
                return False
    return True
    #Done i think?

def exists_row_all_waldo(doob: list[list]) -> bool:
    for row in doob:
        if Other not in row:
            return True
    return False

def exists_col_all_waldo(doob: list[list]) -> bool:
    if len(doob) == 0:
        return False
    for col in range(len(doob[0])):
        var = True
        for row in range(len(doob)):
            if doob[row][col] != Waldo:
                var = False
        if var:
            return True
    return False

""" if Other not in col:
            var = True"""
def exists_row_exists_waldo(doob: list[list]) -> bool:
    for row in doob:
        if Waldo in row:
            return True
    return False
#DONE
def exists_col_exists_waldo(doob: list[list]) -> bool:
    for row in doob:
        for col in row:
            if Waldo in col:
                return True
    return False
#DONE