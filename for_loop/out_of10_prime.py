

prime = 0 # 0, 1

for r in range(10): # 0
    _n = int(input("Give Number: ")) # 7
    
    if _n > 1: # 7 > 1 True
        
        for j in range(2, _n): # (2 to 7) 2,3, 4, 5, 6
            if _n % j == 0: # (7%2==0 False) (7%3==0 False) (7%4==0 False) (7%5==0 False) (7%==0 False)
                break
        
        else: # above for statement fully execute so now control will come to here
            prime += 1 #prime number is equall to prime number + 1 (means counting)

print("Awesome", prime, " Prime Number/s")


