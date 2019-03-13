# Thank-you 

big_number = 0
next_number = 0

for x in range(10):
    number = int(input("Number: "))
    
    if number > big_number:
        next_number = big_number
        big_number = number

    else:
        if number > next_number:
            next_number = number
            
print("Biggest Number: ", big_number)
print("Bigger Number", next_number)



# explained
'''
big_number = 0 # 7 , 10
next_number = 0 # 6 ,

for x in range(10):
    number = int(input("Number: ")) # 7 , 6 , 10
    if number > big_number: #7 > 0 = True, 6 > 7 = False, 10 > 7 = True
        next_number = big_number # 0 = 0, 6 = 7
        big_number = number #7=0 big_number = 7 , 7 = 10 big_number 10

    else:
        if number > next_number:  # 6 > 0
            next_number = number # 0 = 6 next_number = 6
print("Biggest Number: ", big_number)
print("Bigger Number", next_number)
'''
