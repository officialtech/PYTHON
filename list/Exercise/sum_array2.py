

def sum2(_list):
    if len(_list) < 2:
        return "Atleast 2 elements should be there!"
    else:
        return _list[0] + _list[1]

print("1.", sum2([1,2,3]))
print("1.", sum2([1,1]))
print("1.", sum2([1,1,3,7,8]))