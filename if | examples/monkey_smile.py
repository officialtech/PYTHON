

def smiling_monkey(a, b):
    if (a == 'y' and b == 'y') or (a == 'n' and b == 'n'):
        print("-- you are in trouble --", end = "")
        return True
    return False


a = input("Is monkey 'A' is Smiling (y/n): ").lower().strip()
b = input("Is monkey 'B' is Smiling (y/n): ").lower().strip()

print(smiling_monkey(a, b))
