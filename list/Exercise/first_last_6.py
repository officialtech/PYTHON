

def first_last6(_list):
    if _list[0] == 6 or _list[-1] == 6:
        return True
    else:
        return False

print("1",first_last6([1,2,6]))
print("2",first_last6([6,1,2,3]))
print("3",first_last6([13,6,1,2,3]))