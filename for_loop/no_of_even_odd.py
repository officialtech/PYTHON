#jb

odd_c = 0
even_c = 0
for x in range(10):
    no = int(input("Enter Number: "))
    if no%2 == 0:
        even_c += 1
    elif no % 2 == 1:
        odd_c += 1
print("Number of odd's is =", odd_c)
print("Number of even's is =", even_c)
