
'''Given an int n,
return True if it is within 10 of 100 or 200.
 Note: abs(num) computes the absolute value of a number.'''


number = int(input("Number: "))

def hundred_near(number):
    if 100 >= number >= 90 or 200 >= number >= 190:
        return True
    return False

print(hundred_near(number))