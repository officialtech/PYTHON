

'''We have a loud talking parrot.
The "hour" parameter is the current hour time in the range 0 to 23.
We are in trouble if the parrot is talking and the hour is before 7 or after 20.
Return True if we are in trouble.'''




def parrot():
    talk = input("Is Parrot Talking(y/n):\n")
    if talk == 'y':
        hour = float(input("What's time now (20 to 7):\n"))
        if 20.0 < hour <= 23.59 or hour < 7.0:
            return True
    return False

print(parrot())

