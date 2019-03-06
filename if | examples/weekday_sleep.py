

def vacation_weekday(wd, v):
    if wd == 'n' and v == 'n':
        return True
    elif wd == 'y' and v == 'n':
        return False
    elif wd == 'n' and v == 'y':
        return True
    else:
        return 'Invalid!'


wd = input("Is it a Weekday (y/n):\n")
v = input("Are you in Vacation (y/n):\n")
print(vacation_weekday(wd, v))