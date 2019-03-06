

number = int(input("Number: "))
def absolute_diff(number):
    if number <= 19:
        print(19 - number)
    elif number > 19:
        print((number-19) ** 2)
    else:
        return "Invalid!"
    return "THanKs"

print(absolute_diff(number))

