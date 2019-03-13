
# we will deal with four digit number

n4 = int(input("Four Digit Number: "))
storage = 0

for r in range(4):
    # last_no = n4 % 10
    # storage = last_no + storage * 10
    storage = (n4 % 10) + (storage * 10)
    n4 //= 10
print(storage)
