

"""
Given 2 int values, return True if one is negative and one is positive.
 Except if the parameter "negative" is True,
 then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
 """


def positive_negative(int1, int2, negative):
    if int1 > 0 and int2 < 0:
        if negative == 'False':
            return True
        else:
            return False
    elif int1 < 0 and int2 > 0:
        if negative == 'False':
            return True
        else:
            return False
    elif int1 < 0 and int2 < 0:
        if negative == 'False':
            return False
        else:
            return True
    else:
        return False