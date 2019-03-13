

n = input("Any length Number: ")
j = 0
for x in range(len(n)):
    i = int(n)%10
    j = 10*j + i
    n = int(n) // 10

print(j)
