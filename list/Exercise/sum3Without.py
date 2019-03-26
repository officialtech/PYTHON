
def sum3(_list):
    if len(_list) < 3:
        return "array length should be greater than or equall to 3"
    else:
        sm = 0
        for jb in _list:
            sm = sm + jb
        return sm

print("1.", sum3([1,2,3]))
print("2.", sum3([1,2,3,4,6]))
print("3.", sum3([1,2,-1,9]))
print("4.", sum3([1,2]))