


n = int(input("Four Digit Number: "))           # 9444, 944

sum = 0                 # 0, 4, 8

for x in range(4):      # 0<4, 1<4, 
    l = n % 10          # 9444%10=4, 944%10=4,  
    sum += l            # 0+4=4, 4+4=8
    n //= 10            # 9444//10=944, 944//10=94

print(sum)
