

def sameFirstLast(_list):
    if _list[0] == _list[-1]:
        return True
    else:
        return False

print("1.",sameFirstLast([1,2,3]))
print("2.",sameFirstLast([1,2,3,1]))
print("3.",sameFirstLast([1,2,1]))