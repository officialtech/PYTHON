
n1 = int(input("First number: "))
n2 = int(input("Second number: "))
n3 = int(input("Third number: "))


def num2(n1, n2):
    if n1 > n2:
        return n1
    return n2

def num3(n1, n2, n3):
    return num2(n1, num2(n2, n3))


num2(n1, n2)
print(num3(n1, n2, n3))
