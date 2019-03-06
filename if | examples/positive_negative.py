

"""
Given 2 int values, return True if one is negative and one is positive.
 Except if the parameter "negative" is True,
 then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
 """



def positive_negative(int1, int2, negative):
    if negative:
        return (int1 < 0 and int2 < 0)
    return ((int1 > 0 and int2 < 0) or (int1 < 0 and int2 > 0))


int1 = int(input("Number 1(+/-): "))
int2 = int(input("Number 2(+/-): "))
negative = input("True or False: ").capitalize().strip()

print(positive_negative(int1, int2, negative))

