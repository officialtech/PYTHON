# jb

pos = 0
neg = 0
for y in range(1,11):
    no = int(input("Enter Number: "))

    if no > 0:
        pos += 1
    elif no < 0:
        neg += 1
print("Number of positive no's is =", pos)
print("Number of negative no's is =", neg)
