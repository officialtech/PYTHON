

def max_end3(_list):
    m = max(_list)
    new_list = []
    for jb in _list:
        new_list.append(m)
    return new_list

print("1.", max_end3([1,2,3]))
print("2.", max_end3([1,2,3,7]))
print("3.", max_end3([11,5,9]))