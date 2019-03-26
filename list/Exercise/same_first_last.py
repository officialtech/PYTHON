


_list1 = [1,2,3]
_list2 = [7,3,2]

if  _list1 == [] or _list2 == []:
    print("Array shouldn't Empty!")
else:
    def sameFirstLast(_list1, _list2):
        if _list1[0] == _list2[0] or _list1[-1] == _list2[-1]:
            return True
        else:
            return False

print(sameFirstLast(_list1, _list2))

