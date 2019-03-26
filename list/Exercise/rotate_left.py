


def rotate_left3(_list):
    new_list = _list[1:] + _list[0:1]
    return new_list

print("1.", rotate_left3([1,2,3]))
print("2.", rotate_left3([5,11,9]))
print("3.", rotate_left3([7,0,0]))

