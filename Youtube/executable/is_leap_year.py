
def is_leap(year):
    '''Print leap year or not
    '''

    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return f"{year} is Leap year"
    else:
        return f"{year} is not leap year"