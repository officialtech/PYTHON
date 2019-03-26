

def has2_3(_list):
    if _list[0] == 2 or _list[0] == 3 or _list[-1] == 2 or _list[-1] == 3:
        return True
    else:
        return False

print(has2_3([2,5]))
print(has2_3([4,3]))
print(has2_3([4,5]))