
prime = int(input("Number: "))
if prime > 1:
    for p in range(2, prime):
        if prime % p == 0:
            print("Not a Prime number")
            break
    else:
         print(prime, "is prime")
else:print("You are really...Try again\nless than or = 1 is not prime number")
