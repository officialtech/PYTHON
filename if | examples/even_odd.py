
def even_odd(nun):
    if nun % 2 == 0:
        print("Even")
    else:
        print("Odd")
    print(15*"*")
    return "Sukrana"

nun = int(input("Positive integer: "))
print(even_odd(nun))