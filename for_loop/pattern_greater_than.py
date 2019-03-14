

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

for row in range(5):
    for column in range(row+1):
        print("*", end=" ")
    print()
    
# after finishing above statement it will come below statement

for row in range(5):
    for r in range(4,row,- 1):
        print("*", end=" ")
    print()



