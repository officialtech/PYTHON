    x 
   x x 
  x x x 
 x x x x 
x x x x x



for row in range(1,6):
    for column in range(5,row,-1):
        print(" ", end="")
    for col in range(row):
        print("x", end=" ")
    print()
