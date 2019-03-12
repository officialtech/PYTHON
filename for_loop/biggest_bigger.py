# Thank-you 

big_number = 0
next_number = 0

for x in range(5):
    number = int(input("Number: "))
    
    if number > big_number:
        next_number = big_number
        big_number = number

    else:
        if number > next_number:
            next_number = number
            
print("Biggest Number: ", big_number)
print("Bigger Number", next_number)
