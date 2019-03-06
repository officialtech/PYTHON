

def double_same_sum(n1, n2):
    if n1 == n2:
        return ((n1+n2)*2)

    return n1+n2



n1 = int(input("Number: \n"))
n2 = int(input("Number: \n"))
print(15*"-")
print(double_same_sum(n1, n2))